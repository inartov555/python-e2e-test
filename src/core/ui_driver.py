"""
Interface for the Playwright driver
"""

from typing import Protocol, Optional, Literal
from playwright.sync_api import Locator

WaitState = Literal["visible", "hidden", "attached", "detached"]


class UIDriver(Protocol):
    """
    Go to a page
    """
    def goto(self, url: str, wait_until: str, timeout: int) -> None: ...
    """
    Click a locator
    """
    def click(self, sel: str, timeout_ms: Optional[int] = None) -> None: ...
    """
    Type some text in a locator
    """
    def type(self, sel: str, text: str, delay_ms: Optional[int] = None, timeout_ms: Optional[int] = None) -> None: ...
    """
    Fill in a locator with text
    """
    def fill(self, sel: str, text: str, timeout_ms: Optional[int] = None) -> None: ...
    """
    Get inner locator's text
    """
    def text(self, sel: str, timeout_ms: Optional[int] = None) -> str: ...
    """
    Is a locator visible
    """
    def is_visible(self, sel: str, timeout_ms: Optional[int] = None) -> bool: ...
    """
    Wait for locator
    """
    def wait_for(self, sel: str, state: WaitState = "visible", timeout_ms: Optional[int] = None) -> None: ...
    """
    Take a screenshot
    """
    def screenshot(self, path: str, full_page: bool = True) -> None: ...
    """
    Get locator
    """
    def locator(self, loc: str) -> Locator: ...
