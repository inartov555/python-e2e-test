from __future__ import annotations
from typing import Optional

from playwright.sync_api import Page, Locator, expect

from tools.logger.logger import Logger


class BasePage:
    def __init__(self, url: str, page: Page, request):
        """
        Args:
            url (str): web site URL
            page (playwright.sync_api._generated.Page): page fixture
            request (_pytest.fixtures.SubRequest): request fixture
        """
        self.page = page
        self.url = url

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
