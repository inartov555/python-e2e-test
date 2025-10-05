from __future__ import annotations

from playwright.sync_api import Locator, expect

from ..base_page import BasePage
from tools.logger.logger import Logger


log = Logger(__name__)


class SignupPage(BasePage):
    def __init__(self, base_url: str, page: Page, request):
        """
        /accounts/emailsignup/ - URI path

        Args:
            base_url (str): web site URL
            page (playwright.sync_api._generated.Page): page fixture
            request (_pytest.fixtures.SubRequest): request fixture
        """
        super().__init__(base_url, "/accounts/emailsignup/", page, request)

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
        log.info("Go to log in")
        self.login_link.click()

    def expect_loaded(self) -> None:
        log.info("Verifying if the Log in screen is shown")
        expect(self.email_or_phone).to_be_visible()
        expect(self.full_name).to_be_visible()
        expect(self.username).to_be_visible()
        expect(self.password).to_be_visible()
