import os
from datetime import datetime

import pytest
from playwright.sync_api import Page

from src.pages.public.landing_page import LandingPage
from src.pages.public.login_page import LoginPage
from src.pages.public.signup_page import SignupPage
from tools.logger.logger import Logger


log = Logger(__name__)


@pytest.fixture(autouse=True, scope="class")
def setup_elements_for_test(request):
    request.cls.landing_page = LandingPage(Page, request)
    request.cls.signup_page = SignupPage(Page, request)
    request.cls.login_page = LoginPage(Page, request)


def pytest_addoption(parser):
    parser.addoption("--headless", action="store", default="false", help="Run headless browser (true/false)")
    parser.addoption("--viewport-width", action="store", default="1920", help="Browser window width")
    parser.addoption("--viewport-height", action="store", default="1080", help="Browser widndow height")


@pytest.fixture(scope="session")
def get_passed_params(request):
    """
    How to add a new parameter:
        1. Get param value using pytestconfig.getoption("--param_name")
        2. Add param to the passed_params obj using setattr(passed_params, "param_name", param_name)
    """

    class PassedParams:
        storage_state: str | None = os.getenv("STORAGE_STATE") or None

        def has_auth(self) -> bool:
            return bool(self.storage_state and os.path.exists(self.storage_state))

    passed_params = PassedParams()

    base_url = request.config.getoption("--base-url", "https://www.instagram.com")
    setattr(passed_params, "base_url", base_url)
    headless = request.config.getoption("--headless").lower() == "true"
    setattr(passed_params, "headless", headless)
    viewport_width = request.config.getoption("--viewport-width")
    setattr(passed_params, "viewport_width", viewport_width)
    viewport_height = request.config.getoption("--viewport-height")
    setattr(passed_params, "viewport_height", viewport_height)

    return passed_params
    


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
