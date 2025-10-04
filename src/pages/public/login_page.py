from __future__ import annotations
from playwright.sync_api import Locator, expect

from ..base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, url: str, page: Page, request):
        super().__init__(url, page, request)
        self.url = self.url + "/accounts/login/"

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

    def login(self, username: str, password: str) -> None:
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.submit_button.click()

    def expect_loaded(self) -> None:
        expect(self.username_input).to_be_visible()
        expect(self.password_input).to_be_visible()

    def allow_all_cookies_if_shown(self) -> None:
        if self.allow_all_cookies_button.is_visible():
            self.allow_all_cookies_button.click()
