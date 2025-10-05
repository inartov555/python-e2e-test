from __future__ import annotations

from playwright.sync_api import Locator, expect

from ..base_page import BasePage
from tools.logger.logger import Logger


class SignupPage(BasePage):
    def __init__(self, url: str, page: Page, request):
        """
        /accounts/emailsignup/ - URI path

        Args:
            url (str): web site URL
            page (playwright.sync_api._generated.Page): page fixture
            request (_pytest.fixtures.SubRequest): request fixture
        """
        super().__init__(url, "/accounts/emailsignup/", page, request)
        self.log = Logger(__name__)

    @property
    def email_or_phone(self) -> Locator:
        return self.locator('input[name="emailOrPhone"]')

    @property
    def full_name(self) -> Locator:
        return self.locator('input[name="fullName"]')

    @property
    def username(self) -> Locator:
        return self.locator('input[name="username"]')

    @property
    def password(self) -> Locator:
        return self.locator('input[name="password"]')

    @property
    def submit_button(self) -> Locator:
        return self.locator('button[type="submit"]')

    @property
    def login_link(self) -> Locator:
        return self.locator('a[href="/accounts/login/?source=auth_switcher"]')

    def go_to_login(self) -> None:
        self.log.info("Go to log in")
        self.take_a_screenshot()
        self.login_link.click()

    def expect_loaded(self) -> None:
        self.log.info("Verifying if the Log in screen is shown")
        self.take_a_screenshot()
        expect(self.email_or_phone).to_be_visible()
        expect(self.full_name).to_be_visible()
        expect(self.username).to_be_visible()
        expect(self.password).to_be_visible()
