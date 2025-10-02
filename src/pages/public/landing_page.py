from __future__ import annotations
from playwright.sync_api import Locator, expect
from ..base_page import BasePage


class LandingPage(BasePage):
    def __init__(self):
        self.url = self.url + "/"

    @property
    def signup_link(self) -> Locator:
        return self.locator('a[href="/accounts/emailsignup/"]')

    @property
    def login_link(self) -> Locator:
        return self.locator('a[href="/accounts/login/"]')

    def go_to_signup(self) -> None:
        self.signup_link.click()

    def go_to_login(self) -> None:
        self.login_link.click()

    def expect_loaded(self) -> None:
        expect(self.signup_link.or_(self.login_link)).to_be_visible()
