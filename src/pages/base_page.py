from __future__ import annotations
from typing import Optional

from playwright.sync_api import Page, Locator, expect

from tools.logger.logger import Logger
from conftest import timestamped_path
from src.core.custom_config import custom_config_global


class BasePage:
    def __init__(self, url: str, page: Page, request):
        """
        Args:
            url (str): web site URL
            page (playwright.sync_api._generated.Page): page fixture
            request (_pytest.fixtures.SubRequest): request fixture
        """
        self.log = Logger(__name__)
        self.page = page
        self.url = url
        self.request_fixture = request
        self.custom_config = custom_config_global

    def take_a_screenshot(self) -> None:
        if self.custom_config.take_screenshot:
            test_name = self.request_fixture.node.name
            self.page.screenshot(path=timestamped_path(test_name, "png"))
        else:
            self.log.warning("Taking a screenshot is skipped due to a config param take_screenshot = False")

    def open(self) -> "BasePage":
        self.page.goto(self.url, wait_until="load", timeout=20000)
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
        self.take_a_screenshot()
        loc = self.locator(selector)
        expect(loc).to_be_visible(timeout=timeout)
        return loc

    def assert_url_contains(self, fragment: str) -> None:
        self.take_a_screenshot()
        expect(self.page).to_have_url(lambda u: fragment in u)
