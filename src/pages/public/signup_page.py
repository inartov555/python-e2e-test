from __future__ import annotations
from playwright.sync_api import Locator, expect

from ..base_page import BasePage


class SignupPage(BasePage):
    def __init__(self, url: str, page: Page, request):
        super().__init__(url, page, request)
        self.url = self.url + "/accounts/emailsignup/"

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

    def expect_loaded(self) -> None:
        expect(self.email_or_phone).to_be_visible()
        expect(self.full_name).to_be_visible()
        expect(self.username).to_be_visible()
        expect(self.password).to_be_visible()
