import os
from datetime import datetime
from configparser import ConfigParser, ExtendedInterpolation
from dataclasses import dataclass

import pytest
from playwright.sync_api import Playwright, sync_playwright, Browser, BrowserContext, Page, expect

from src.core.app_config import AppConfig
from tools.temp_encr import decrypt
from tools.logger.logger import Logger
from tools.file_utils import FileUtils


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
    log_file = os.path.join(FileUtils.timestamped_path("pytest", "log", artifacts_folder_default))
    log.setup_cli_handler(level=log_level)
    log.setup_filehandler(level=log_file_level, file_name=log_file)
    log.info("General loglevel: '{}', File: '{}'".format(log_level, log_file_level))
    log.info("Test logs will be stored: '{}'".format(log_file))


def validate_app_config_params(**kwargs) -> None:
    """
    Validation of the config parameters
    """
    if not kwargs.get("username"):
        raise ValueError("username parameter is required for tests")
    if not kwargs.get("password"):
        raise ValueError("password parameter is required for tests")


@pytest.fixture(scope="session")
def app_config(pytestconfig) -> AppConfig:
    ini_config_file = pytestconfig.getoption("--ini-config")
    log.info(f"Reading config properties from '{ini_config_file}' and storing to a data class")
    result_dict = {}
    cfg = ConfigParser(interpolation=ExtendedInterpolation())
    cfg.read(ini_config_file)
    result_dict["wait_to_handle_capture_manually"] = cfg.getboolean("pytest",
                                                                    "wait_to_handle_capture_manually",
                                                                    fallback=False)
    result_dict["action_timeout"] = cfg.getfloat("pytest", "action_timeout", fallback=15000.0)
    result_dict["navigation_timeout"] = cfg.getfloat("pytest", "navigation_timeout", fallback=15000.0)
    result_dict["assert_timeout"] = cfg.getfloat("pytest", "assert_timeout", fallback=15000.0)
    result_dict["browser"] = cfg.get("pytest", "browser", fallback="chrome")
    result_dict["base_url"] = cfg.get("pytest", "base_url", fallback="https://www.instagram.com")
    result_dict["is_headless"] = cfg.getboolean("pytest", "is_headless", fallback=False)
    result_dict["width"] = cfg.getint("pytest", "width", fallback=1920)
    result_dict["height"] = cfg.getint("pytest", "height", fallback=1080)
    result_dict["username"] = cfg.get("pytest", "username")
    result_dict["password"] = cfg.get("pytest", "password")
    validate_app_config_params(**result_dict)
    result_dict["password"] = decrypt(result_dict.get("password"))
    return AppConfig(**result_dict)


def pytest_addoption(parser):
    parser.addoption("--ini-config", action="store", default="pytest.ini", help="The path to the *.ini config file")


@pytest.fixture(scope="session")
def screenshot_dir(pytestconfig):
    artifacts_folder_default = os.getenv("HOST_ARTIFACTS")
    os.makedirs(artifacts_folder_default, exist_ok=True)
    return artifacts_folder_default


def get_browser(playwright, request) -> Browser:
    """
    Set up a browser and return it
    """
    log.info("Getting a browser basing on the config properties")
    app_config = request.getfixturevalue("app_config")
    if app_config.browser in ("chromium", "chrome", "msedge"):
        # Chromium Google Chrome, MS Edge
        if app_config.is_headless:
            args = [f"--window-size={width},{height}"]
        else:
            args = []
        browser = playwright.chromium.launch(headless=app_config.is_headless,
                                             args=args)
    elif app_config.browser in ("firefox"):
        # Firefox
        if app_config.is_headless:
            args = [f"--window-size={width},{height}"]
        else:
            args = []
        browser = playwright.firefox.launch(headless=app_config.is_headless,
                                            args=args)
    elif app_config.browser in ("webkit", "safari"):
        # WebKit, Safari
        browser = playwright.webkit.launch(headless=app_config.is_headless)
    else:
        raise ValueError(f"browser config param contains incorrect value: {app_config.browser}")
    if app_config.browser in ("webkit", "safari") or not app_config.is_headless:
        context = browser.new_context(viewport={"width": app_config.width, "height": app_config.height})
    else:
        context = browser.new_context(viewport=None)
    page = context.new_page()
    # Setting default timeouts
    context.set_default_navigation_timeout(app_config.navigation_timeout)
    context.set_default_timeout(app_config.action_timeout)
    page.set_default_navigation_timeout(app_config.navigation_timeout)
    page.set_default_timeout(app_config.action_timeout)
    expect.set_options(timeout=app_config.assert_timeout)
    request.cls.page = page
    log.info(f"{app_config.browser} browser is selected")
    return browser


@pytest.fixture(autouse=True, scope="function")
def browser_setup(playwright, pytestconfig, request):
    browser = get_browser(playwright, request)
    yield browser
    browser.close()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
