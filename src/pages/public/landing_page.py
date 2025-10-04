from __future__ import annotations

from playwright.sync_api import Locator, expect

from ..base_page import BasePage
from tools.logger.logger import Logger


class LandingPage(BasePage):
    def __init__(self, url: str, page: Page, request):
        """
        Args:
            url (str): web site URL
            page (playwright.sync_api._generated.Page): page fixture
            request (_pytest.fixtures.SubRequest): request fixture
        """
        super().__init__(url, page, request)
        self.url = self.url + "/"

    @property
    def signup_link(self) -> Locator:
        return self.locator('a[href="/accounts/emailsignup/"]')

    @property
    def username_input(self) -> Locator:
        return self.locator('input[name="username"]')

    @property
    def password_input(self) -> Locator:
        return self.locator('input[name="password"]')

    @property
    def submit_button(self) -> Locator:
        return self.locator('button[type="submit"]')

    @property
    def error_text(self) -> Locator:
        return self.locator('[role="alert"], #slfErrorAlert, div:has-text("incorrect")')

    @property
    def forgot_password_link(self) -> Locator:
        return self.locator('a[href="/accounts/password/reset/"]')

    def go_to_signup(self) -> None:
        self.signup_link.click()

    def expect_loaded(self) -> None:
        expect(self.signup_link.or_(self.login_link)).to_be_visible()
