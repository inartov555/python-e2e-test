from __future__ import annotations

from playwright.sync_api import Locator, expect

from tools.logger.logger import Logger
from src.pages.base_page import BasePage


class MenuOverlay:
    """
    Represents the menu pane in the home page.
    """
    log = Logger(__name__)

    def __init__(self, root: Locator, page_class: BasePage):
        self.root = root
        self.page_class = page_class
        self.logout_elem = self.root.get_by_text("Log out").locator("xpath=ancestor::*[@role='button'][1]")
        self.logging_out_text = self.root.get_by_text("Logging out")

    def log_out(self) -> None:
        self.log.info("Logging out")
        self.page_class.take_a_screenshot()
        expect(self.logout_elem).to_be_visible()
        self.logout_elem.dispatch_event("click")
        expect(self.logging_out_text).to_be_visible()
