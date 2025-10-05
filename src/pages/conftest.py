import pytest
from playwright.sync_api import Playwright, sync_playwright, Browser, BrowserContext, Page

from src.pages.public.landing_page import LandingPage
from src.pages.public.login_page import LoginPage
from src.pages.public.signup_page import SignupPage
from src.pages.private.home_feed_page import HomeFeedPage
from tools.logger.logger import Logger


log = Logger(__name__)


@pytest.fixture(autouse=False, scope="function")
def setup_elements_for_test(request):
    request.cls.app_config = request.getfixturevalue("app_config")
    request.cls.landing_page = LandingPage(request.cls.app_config.base_url, request.cls.page)
    request.cls.signup_page = SignupPage(request.cls.app_config.base_url, request.cls.page)
    request.cls.login_page = LoginPage(request.cls.app_config.base_url, request.cls.page)
    request.cls.home_page = HomeFeedPage(request.cls.app_config.base_url, request.cls.page)
