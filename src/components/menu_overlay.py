"""
Represents the menu pane in the home page.
"""

from __future__ import annotations

from playwright.sync_api import Locator, expect

from tools.logger.logger import Logger
from src.pages.base_page import BasePage
from src.components.base_component import BaseComponent


log = Logger(__name__)


class MenuOverlay(BaseComponent):
    """
    Represents the menu pane in the home page.
    """

    def __init__(self, root: Locator, page_class: BasePage):
        """
        Args:
            root (Locator): locator
            page_class (BasePage): the page derived from BasePage
        """
        super().__init__(root, page_class)
        self.logout_elem = self.root.get_by_text("Log out").locator("xpath=ancestor::*[@role='button'][1]")
        self.logging_out_text = self.root.get_by_text("Logging out")

    def log_out(self) -> None:
        """
        Logging out
        """
        log.info("Logging out")
        expect(self.logout_elem).to_be_visible()
        self.logout_elem.dispatch_event("click")
        expect(self.logging_out_text).to_be_visible()

    def is_open(self) -> bool:
        """
        Check if it's open
        """
        pass