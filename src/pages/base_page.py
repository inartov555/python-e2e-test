from __future__ import annotations
from typing import Optional

from playwright.sync_api import Page, Locator, expect

from src.core.config_custom import ConfigCustom


class BasePage:
    def __init__(self, page: Page, request):
        self.page = page
        self.url = ConfigCustom.base_url

    def open(self) -> "BasePage":
        print(f"\n\n\n {self.url} \n\n\n")
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
