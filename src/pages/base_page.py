from __future__ import annotations
from typing import Optional

from playwright.sync_api import Page, Locator, expect

from tools.logger.logger import Logger
from tools.file_utils import FileUtils


log = Logger(__name__)


class BasePage:
    def __init__(self, base_url: str, uri_path: str, page: Page):
        """
        Args:
            base_url (str): web site URL
            uri_path (str): e.g. /accounts/login/
            page (playwright.sync_api._generated.Page): page fixture
        """
        self.base_url = base_url
        self.uri_path = uri_path
        self.full_url = self.base_url + self.uri_path
        self.page = page

    def open(self) -> "BasePage":
        log.info(f"Opening {self.full_url} URL")
        self.page.goto(self.full_url, wait_until="load", timeout=20000)
        self.page.wait_for_function("document.readyState === 'complete'", timeout=20000)
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
