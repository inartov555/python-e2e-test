from __future__ import annotations

from playwright.sync_api import Locator, expect

from ..base_page import BasePage
from tools.logger.logger import Logger


log = Logger(__name__)


class LoginPage(BasePage):
    def __init__(self, base_url: str, page: Page):
        """
        /accounts/login/ - URI path

        Args:
            base_url (str): web site URL
            page (playwright.sync_api._generated.Page): page fixture
        """
        super().__init__(base_url, "/accounts/login/", page)

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

    @property
    def allow_all_cookies_button(self) -> Locator:
        return self.locator('button[class="_a9-- _ap36 _asz1"]')

    @property
    def incorrect_login_error_text(self) -> Locator:
        return self.page.get_by_text("Sorry, your password was incorrect. Please double-check your password.")

    def login(self, username: str, password: str) -> None:
        log.info("Logging in")
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.submit_button.click()

    def expect_loaded(self) -> None:
        log.info("Verifying if the Log in page is shown")
        expect(self.username_input).to_be_visible()
        expect(self.password_input).to_be_visible()

    def allow_all_cookies_if_shown(self) -> None:
        log.info("Confirming the allow cookies overlay, if shown")
        if self.allow_all_cookies_button.is_visible():
            self.allow_all_cookies_button.click()

    def is_error_login_text_shown(self) -> None:
        log.info("Verifying if error log in text is shown")
        expect(self.incorrect_login_error_text).to_be_visible()
