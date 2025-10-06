from __future__ import annotations

from playwright.sync_api import Locator, expect

from tools.logger.logger import Logger
from src.pages.base_page import BasePage
from src.components.base_component import BaseComponent


log = Logger(__name__)


class PostCard(BaseComponent):
    """
    Represents a post in the home page.
    Some elements do not support regular click, that's why JS click event was dispatched for them.
    """

    def __init__(self, root: Locator, page_class: BasePage):
        super().__init__(root, page_class)
        self.like_button = self.root.locator('div[role="button"]:has(svg[aria-label="Like"])').first
        self.unlike_button = self.root.locator('div[role="button"]:has(svg[aria-label="Unlike"])').first
        self.save_button = self.root.locator('div[role="button"]:has(svg[aria-label="Save"])').first
        self.remove_button = self.root.locator('div[role="button"]:has(svg[aria-label="Remove"])').first
        self.comment_button = self.root.locator('div[role="button"]:has(svg[aria-label="Comment"])').first
        self.liked_by_link = self.root.locator('a[href*="/liked_by/"]').first

    def scroll_to_element_liked_by(self) -> None:
        self.liked_by_link.scroll_into_view_if_needed()

    def like(self) -> None:
        log.info("Liking a post")
        expect(self.like_button).to_be_visible()
        self.like_button.dispatch_event("click")
        expect(self.unlike_button).to_be_visible()

    def unlike(self) -> None:
        log.info("Unliking a post")
        expect(self.unlike_button).to_be_visible()
        self.unlike_button.dispatch_event("click")
        expect(self.like_button).to_be_visible()

    def save(self) -> None:
        log.info("Saving a post")
        expect(self.save_button).to_be_visible()
        self.save_button.click()
        expect(self.remove_button).to_be_visible()

    def remove(self) -> None:
        log.info("Removing a post")
        expect(self.remove_button).to_be_visible()
        self.remove_button.click()
        expect(self.save_button).to_be_visible()

    def open_comments(self) -> None:
        log.info("Opening comments")
        expect(self.comment_button).to_be_visible()
        self.comment_button.dispatch_event("click")

    def expect_comment_button_visible(self) -> None:
        log.info("Verifying if comment button is visible")
        expect(self.comment_button).to_be_visible()
