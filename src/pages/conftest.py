import pytest
from playwright.sync_api import Playwright, sync_playwright, Browser, BrowserContext, Page

from src.pages.public.landing_page import LandingPage
from src.pages.public.login_page import LoginPage
from src.pages.public.signup_page import SignupPage
from src.pages.private.home_feed_page import HomeFeedPage
from src.core.custom_config import custom_config_global
from tools.logger.logger import Logger


log = Logger(__name__)


@pytest.fixture(autouse=False, scope="class")
def setup_elements_for_test(request):
    request.cls.custom_config = custom_config_global
    request.cls.landing_page = LandingPage(request.cls.custom_config.base_url, request.cls.page, request)
    request.cls.signup_page = SignupPage(request.cls.custom_config.base_url, request.cls.page, request)
    request.cls.login_page = LoginPage(request.cls.custom_config.base_url, request.cls.page, request)
    request.cls.home_page = HomeFeedPage(request.cls.custom_config.base_url, request.cls.page, request)
