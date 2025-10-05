import os
from datetime import datetime
from configparser import ConfigParser, ExtendedInterpolation
from dataclasses import dataclass

import pytest
from playwright.sync_api import Playwright, sync_playwright, Browser, BrowserContext, Page, expect

from src.core.custom_config import custom_config_global
from tools.logger.logger import Logger


log = Logger(__name__)


@pytest.fixture(autouse=True, scope="session")
def add_loggers(request):
    """
    The fixture to configure loggers
    It uses built-in pytest arguments to configure loggigng level and files

    Parameters:
        log_level or --log-level general log level for capturing
        log_file_level or --log-file-level  level of log to be stored to a file. Usually lower than general log
        log_file or --log-file  path where logs will be saved
    """
    artifacts_folder_default = os.getenv("HOST_ARTIFACTS")
    log_level = "DEBUG"
    log_file_level = "DEBUG"
    log_file = os.path.join(timestamped_path("pytest", "log", artifacts_folder_default))
    log.setup_cli_handler(level=log_level)
    log.setup_filehandler(level=log_file_level, file_name=log_file)
    log.info("General loglevel: '{}', File: '{}'".format(log_level, log_file_level))
    log.info("Test logs will be stored: '{}'".format(log_file))


def fill_in_custom_config_from_ini_config(file_path: str):
    log.info(f"Reading config properties from '{file_path}' and storing to a data class")
    result_dict = {}
    cfg = ConfigParser(interpolation=ExtendedInterpolation())
    cfg.read(file_path)
    result_dict["action_timeout"] = cfg.getfloat("pytest", "action_timeout")
    result_dict["navigation_timeout"] = cfg.getfloat("pytest", "navigation_timeout")
    result_dict["assert_timeout"] = cfg.getfloat("pytest", "assert_timeout")
    result_dict["take_screenshot"] = cfg.get("pytest", "take_screenshot")
    result_dict["browser"] = cfg.get("pytest", "browser")
    result_dict["base_url"] = cfg.get("pytest", "base_url")
    result_dict["is_headless"] = cfg.getboolean("pytest", "is_headless")
    result_dict["width"] = cfg.getint("pytest", "width")
    result_dict["height"] = cfg.getint("pytest", "height")
    result_dict["username"] = cfg.get("pytest", "username")
    result_dict["password"] = cfg.get("pytest", "password")
    custom_config_global.change_variables(**result_dict)


def pytest_addoption(parser):
    parser.addoption("--ini-config", action="store", default="pytest.ini", help="The path to the *.ini config file")


@pytest.fixture(scope="session")
def screenshot_dir(pytestconfig):
    # path_from_input_params = pytestconfig.getoption("--screenshot-dir")
    artifacts_folder_default = os.getenv("HOST_ARTIFACTS")
    # if path_from_input_params:
    #    path = path_from_input_params
    # else:
    #    path = artifacts_folder_default
    os.makedirs(artifacts_folder_default, exist_ok=True)
    return artifacts_folder_default


def timestamped_path(file_name, file_ext, path_to_file=os.getenv("HOST_ARTIFACTS")):
    """
    Args:
        file_name (str): e.g. screenshot
        file_ext (str): file extention, e.g., png
        path_to_file (str): e.g. /home/user/test_dir/artifacts/
    """
    ts = datetime.utcnow().strftime("%Y%m%d-%H%M%S.%f")
    screenshot_path = os.path.join(path_to_file, f"{file_name}-{ts}.{file_ext}")
    log.info(f"Screenshot path: {screenshot_path}")
    return screenshot_path


def get_browser(playwright, request) -> Browser:
    """
    Set up a browser and return it
    """
    log.info("Getting a browser basing on the config properties")
    width = custom_config_global.width
    height = custom_config_global.height
    if custom_config_global.browser in ("chromium", "chrome", "msedge"):
        # Chromium Google Chrome, MS Edge
        browser = playwright.chromium.launch(headless=custom_config_global.is_headless,
                                             args=[f"--window-size={width},{height}"])
    elif custom_config_global.browser in ("firefox"):
        # Firefox
        browser = playwright.firefox.launch(headless=custom_config_global.is_headless,
                                            args=[f"--window-size={width},{height}"])
    elif custom_config_global.browser in ("webkit", "safari"):
        # WebKit, Safari
        browser = playwright.webkit.launch(headless=custom_config_global.is_headless)
    else:
        raise ValueError(f"browser config param contains incorrect value: {custom_config_global.browser}")
    context = browser.new_context(viewport={"width": width, "height": height})
    page = context.new_page()
    # Setting default timeouts
    context.set_default_navigation_timeout(custom_config_global.navigation_timeout)
    context.set_default_timeout(custom_config_global.action_timeout)
    page.set_default_navigation_timeout(custom_config_global.navigation_timeout)
    page.set_default_timeout(custom_config_global.action_timeout)
    expect.set_options(timeout=custom_config_global.assert_timeout)
    request.cls.page = page
    log.info(f"{custom_config_global.browser} browser is selected")
    return browser


@pytest.fixture(autouse=True, scope="class")
def browser_setup(playwright, pytestconfig, request):
    ini_config_file = pytestconfig.getoption("--ini-config")
    fill_in_custom_config_from_ini_config(ini_config_file)
    browser = get_browser(playwright, request)
    yield browser
    browser.close()


@pytest.fixture(autouse=False, scope="class")
def setup_cleanup_signin_signout(request):
    log.info("Setup. Sign in...")
    request.cls.login_page.open()
    request.cls.login_page.allow_all_cookies_if_shown()
    request.cls.login_page.expect_loaded()
    request.cls.login_page.login(request.cls.login_page.custom_config.username,
                                 request.cls.login_page.custom_config.password)
    request.cls.home_page.expect_feed_visible()
    yield
    log.info("Cleanup. Sign out")


@pytest.fixture(autouse=False, scope="function")
def inject_test_name(request):
    return request.node.name
