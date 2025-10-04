from __future__ import annotations
from typing import Optional

from playwright.sync_api import Page, Locator, expect

from ..base_page import BasePage


class LoginForm(BasePage):
    """
    Login form is shared between a few pages
    """
    def __init__(self, url: str, page: Page, request):
        self.page = page
        self.url = url

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
    def submit_button(self) -> Locator:
        return self.locator('button[type="submit"]')

    @property
    def login_with_facebook(self) -> Locator:
        return self.locator('button[class=" _aswp _aswq _aswu _asw_ _asx2"] span[class="xvs91rp xwhw2v2 x173jzuc"]')

    @property
    def signup_link(self) -> Locator:
        return self.locator('a[href="/accounts/emailsignup/"]')

    def open(self) -> "BasePage":
        self.page.goto(self.url)
        return self

    def locator(self, selector: str) -> Locator:
        return self.page.locator(selector)

    def click(self, selector: str) -> None:
        self.locator(selector).click()

    def type(self, selector: str, text: str, clear: bool = True) -> None:
        loc = self.locator(selector)
        if clear:
            loc.fill("")
        loc.type(text)

    def wait_visible(self, selector: str, timeout: int = 5000) -> Locator:
        loc = self.locator(selector)
        expect(loc).to_be_visible(timeout=timeout)
        return loc

    def assert_url_contains(self, fragment: str) -> None:
        expect(self.page).to_have_url(lambda u: fragment in u)
