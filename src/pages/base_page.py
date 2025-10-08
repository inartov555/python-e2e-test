"""
Base methods that can be used by derived pages
"""

from __future__ import annotations
from typing import Optional

from playwright.sync_api import Page, Locator, expect

from tools.logger.logger import Logger
from tools.file_utils import FileUtils
from src.core.app_config import AppConfig
from src.core.ui_driver import UIDriver


log = Logger(__name__)


class BasePage:
    """
    Base methods that can be used by derived pages
    """
    def __init__(self, app_config: AppConfig, uri_path: str, ui_driver: UIDriver):
        """
        Args:
            app_config (AppConfig): app config passed in ini config file
            uri_path (str): e.g. /accounts/login/
            ui_driver (UIDriver): e.g., PlaywrightDriver adapter
        """
        self.app_config = app_config
        self.base_url = self.app_config.base_url
        self.uri_path = uri_path
        self.full_url = self.base_url + self.uri_path
        self.ui_driver = ui_driver

    def open(self) -> "BasePage":
        """
        Opening a page
        """
        log.info(f"Opening {self.full_url} URL")
        self.ui_driver.goto(self.full_url, wait_until="load", timeout=20000)
        self.ui_driver.wait_for_function("document.readyState === 'complete'", timeout=20000)
        return self

    def locator(self, selector: str) -> Locator:
        """
        Get a locator
        """
        return self.ui_driver.locator(selector)

    def click(self, selector: str) -> None:
        """
        Clicking a locator
        """
        self.locator(selector).click()

    def type(self, selector: str, text: str, clear: bool = True) -> None:
        """
        Typing text in a locator
        """
        loc = self.locator(selector)
        if clear:
            loc.fill("")
        loc.type(text)

    def wait_visible(self, selector: str, timeout: int = 5000) -> Locator:
        """
        Waiting for locator to be visible
        """
        loc = self.locator(selector)
        expect(loc).to_be_visible(timeout=timeout)
        return loc
