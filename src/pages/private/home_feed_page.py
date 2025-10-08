"""
Authorized Home page
"""

from __future__ import annotations

from playwright.sync_api import expect

from tools.logger.logger import Logger
from src.components.menu_overlay import MenuOverlay
from src.components.post_card import PostCard
from src.core.app_config import AppConfig
from src.core.ui_driver import UIDriver
from src.pages.base_page import BasePage


log = Logger(__name__)


class HomeFeedPage(BasePage):
    """
    Authorized Home page
    """
    def __init__(self, app_config: AppConfig, ui_driver: UIDriver):
        """
        / - URI path

        Args:
            app_config (AppConfig): app config passed in ini config file
            ui_driver (UIDriver): e.g., PlaywrightDriver adapter
        """
        super().__init__(app_config, "/", ui_driver)
        self.home_tab = self.ui_driver.locator('a[href="/?next=%2F"], a[href="/"]').first
        self.menu_more = self.ui_driver.get_by_text("More").locator("xpath=ancestor::a[@role='link'][1]")

    @property
    def first_post(self) -> PostCard:
        """
        Get the 1st post
        """
        root = self.ui_driver.locator('article').first
        return PostCard(root, self)

    @property
    def posts(self) -> list[PostCard]:
        """
        Get the posts
        """
        roots = self.ui_driver.locator('article')
        count = roots.count()
        return [PostCard(roots.nth(i)) for i in range(count)]

    @property
    def menu_overlay(self) -> MenuOverlay:
        """
        Get the More overlay
        """
        root = self.ui_driver.locator('div[role="dialog"]')
        result = MenuOverlay(root, self)
        return result

    def go_to_home_tab(self) -> None:
        """
        Call this method only if the Home tab is not focused
        """
        log.info("Go to the Home tab")
        self.home_tab.click()

    def open_menu_overlay(self) -> None:
        """
        Open the More overlay
        """
        log.info("Open the menu overlay")
        self.menu_more.click()

    def expect_home_tab_visible(self) -> None:
        """
        Check if the Home tab is visible
        """
        log.info("Verifying if the Home shortcut is visible")
        expect(self.home_tab).to_be_visible()

    def expect_feed_visible(self) -> None:
        """
        Check if the 1st post is visible
        """
        log.info("Verifying if posts are displayed in the Home page")
        expect(self.ui_driver.locator('article').first).to_be_visible()
