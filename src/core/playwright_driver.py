"""
The adapter for the Playwright driver
"""

from typing import Optional
from playwright.sync_api import Page, Locator

from src.core.ui_driver import UIDriver, WaitState
from src.core.app_config import AppConfig


class PlaywrightDriver(UIDriver):
    """
    The adapter for the Playwright driver
    """
    def __init__(self, app_config: AppConfig, page: Page) -> None:
        """
        app_config (AppConfig): app config from ini config file
        page (Page): playwright page object
        """
        self.page = page
        self.app_config = app_config

    def _timeout(self, t: Optional[int]) -> int:
        """
        Timeout
        """
        return t if t is not None else self.app_config.action_timeout

    def goto(self, url: str, wait_until: str, timeout: int) -> None:
        """
        Go to a page
        """
        self.page.goto(url, wait_until=wait_until, timeout=timeout)

    def click(self, sel: str, timeout_ms: Optional[int] = None) -> None:
        """
        Click a locator
        """
        self.page.locator(sel).click(timeout=self._timeout(timeout_ms))

    def type(self, sel: str, text: str, delay_ms: Optional[int] = None, timeout_ms: Optional[int] = None) -> None:
        """
        Type some text in a locator
        """
        loc = self.page.locator(sel)
        # Consistent behavior: start clean
        loc.fill("", timeout=self._timeout(timeout_ms))
        loc.type(text, delay=delay_ms, timeout=self._timeout(timeout_ms))

    def fill(self, sel: str, text: str, timeout_ms: Optional[int] = None) -> None:
        """
        Fill in a locator with text
        """
        self.page.locator(sel).fill(text, timeout=self._timeout(timeout_ms))

    def text(self, sel: str, timeout_ms: Optional[int] = None) -> str:
        """
        Get inner locator's text
        """
        loc = self.page.locator(sel)
        # Ensure at least one match (better error than inner_text on empty set)
        if loc.count() == 0:
            raise AssertionError(f"No elements match selector: {sel}")
        return loc.first.inner_text(timeout=self._timeout(timeout_ms)).strip()

    def is_visible(self, sel: str, timeout_ms: Optional[int] = None) -> bool:
        """
        Is a locator visible
        """
        return self.page.locator(sel).is_visible(timeout=self._timeout(timeout_ms))

    def wait_for(self, sel: str, state: WaitState = "visible", timeout_ms: Optional[int] = None) -> None:
        """
        Wait for locator
        """
        self.page.locator(sel).wait_for(state=state, timeout=self._timeout(timeout_ms))

    def screenshot(self, path: str, full_page: bool = True) -> None:
        """
        Take a screenshot
        """
        self.page.screenshot(path=path, full_page=full_page, timeout=self.app_config.action_timeout)

    def attr(self, sel: str, name: str, timeout_ms: Optional[int] = None) -> Optional[str]:
        """
        Get locator attribute
        """
        return self.page.locator(sel).get_attribute(name, timeout=self._timeout(timeout_ms))

    def count(self, sel: str, timeout_ms: Optional[int] = None) -> int:
        """
        Playwright doesn't expose timeout on count(); do an existence wait first
        """
        self.page.locator(sel).first.wait_for(state="attached", timeout=self._timeout(timeout_ms))
        return self.page.locator(sel).count()

    def wait_for_function(self, js_code: str, timeout: int) -> None:
        """
        Wait for JavaScript function to finish
        """
        self.page.wait_for_function(js_code, timeout=timeout)

    def locator(self, loc: str) -> Locator:
        """
        Get locator
        """
        return self.page.locator(loc)

    def get_by_text(self, text: str) -> Locator:
        """
        Get element by text
        """
        return self.page.get_by_text(text)
