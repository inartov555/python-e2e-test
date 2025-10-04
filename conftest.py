import os
from datetime import datetime
from configparser import ConfigParser, ExtendedInterpolation

import pytest

from src.pages.public.landing_page import LandingPage
from src.pages.public.login_page import LoginPage
from src.pages.public.signup_page import SignupPage
from src.pages.private.home_feed_page import HomeFeedPage
from src.core.custom_config import CustomConfig
from tools.logger.logger import Logger


log = Logger(__name__)


def get_pytest_ini_config(file_path: str) -> CustomConfig:
    result_dict = {}
    cfg = ConfigParser(interpolation=ExtendedInterpolation())
    cfg.read(file_path)
    result_dict["browser"] = cfg.get("pytest", "browser")
    result_dict["base_url"] = cfg.get("pytest", "base_url")
    result_dict["is_headless"] = cfg.getboolean("pytest", "is_headless")
    result_dict["viewport_width"] = cfg.getint("pytest", "viewport_width")
    result_dict["viewport_height"] = cfg.getint("pytest", "viewport_height")
    custom_config = CustomConfig(result_dict)
    return custom_config


def pytest_addoption(parser):
    parser.addoption("--ini-config", action="store", default="pytest.ini", help="The path to the *.ini config file")


def get_browser(custom_config: CustomConfig):
    """
    Args:
        browser_type (str): one of (chromium, chrome, msedge, firefox, safari, webkit)
    """
    if custom_config.browser in ("chromium", "chrome", "msedge"):
        # Chromium Google Chrome, MS Edge
        driver = playwright.chromium.launch(headless=custom_config.is_headless)
    elif custom_config.browser in ("firefox"):
        # Firefox
        driver = playwright.firefox.launch(headless=custom_config.is_headless)
    elif custom_config.browser in ("webkit", "safari"):
        # WebKit, Safari
        driver = playwright.webkit.launch(headless=custom_config.is_headless)
    else:
        raise ValueError(f"browser config param contains incorrect value: {custom_config.browser}")
    context = driver.new_context(
        base_url=custom_config.base_url,
        viewport={"width": custom_config.viewport_width,
                  "height": custom_config.viewport_height}
    )
    page = context.new_page()
    return driver


@pytest.fixture(autouse=True, scope="session")
def driver(playwright, pytestconfig):
    ini_config_file = pytestconfig.getoption("--ini-config")
    custom_config = get_pytest_ini_config(ini_config_file)
    driver = get_browser(custom_config)
    yield driver
    driver.close()


@pytest.fixture(autouse=True, scope="function")
def setup_elements_for_test(request, page):
    request.cls.custom_config = CustomConfig()
    request.cls.landing_page = LandingPage(request.cls.custom_config.base_url, page, request)
    request.cls.signup_page = SignupPage(request.cls.custom_config.base_url, page, request)
    request.cls.login_page = LoginPage(request.cls.custom_config.base_url, page, request)
    request.cls.home_page = HomeFeedPage(request.cls.custom_config.base_url, page, request)


def timestamped_path(file_name, file_ext, path_to_file=os.getenv("HOST_ARTIFACTS")):
    """
    Args:
        file_name (str): e.g. screenshot
        file_ext (str): file extention, e.g., png
        path_to_file (str): e.g. /home/user/test_dir/artifacts/
    """
    ts = datetime.utcnow().strftime("%Y%m%d-%H%M%S.%f")
    return os.path.join(path_to_file, f"{file_name}-{ts}.{file_ext}")


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
    log.info("Test's logs will be stored: '{}'".format(log_file))
