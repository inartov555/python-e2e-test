from __future__ import annotations

from playwright.sync_api import Locator, expect

from tools.logger.logger import Logger
from src.pages.base_page import BasePage


class PostCard:
    """
    Represents a post in the home feed.
    """
    log = Logger(__name__)
    def __init__(self, root: Locator, page_class: BasePage):
        self.root = root
        self.page_class = page_class
        self.like_button = self.root.locator('div[role="button"]:has(svg[aria-label="Like"])').first
        self.unlike_button = self.root.locator('div[role="button"]:has(svg[aria-label="Unlike"])').first
        self.save_button = self.root.locator('div[role="button"]:has(svg[aria-label="Save"])').first
        self.remove_button = self.root.locator('div[role="button"]:has(svg[aria-label="Remove"])').first
        self.comment_button = self.root.locator('div[role="button"]:has(svg[aria-label="Comment"])').first
        self.liked_by_link = self.root.locator('a[href*="/liked_by/"]').first

    def scroll_to_element_liked_by(self) -> None:
        self.liked_by_link.scroll_into_view_if_needed()

    def like(self) -> None:
        self.page_class.take_a_screenshot()
        if self.like_button.is_visible():
            self.like_button.dispatch_event("click")
            expect(self.unlike_button).to_be_visible()

    def unlike(self) -> None:
        self.page_class.take_a_screenshot()
        if self.unlike_button.is_visible():
            self.unlike_button.dispatch_event("click")
            expect(self.like_button).to_be_visible()

    def save(self) -> None:
        self.page_class.take_a_screenshot()
        if self.save_button.is_visible():
            self.save_button.dispatch_event("click")
            expect(self.remove_button).to_be_visible()

    def remove(self) -> None:
        self.page_class.take_a_screenshot()
        if self.remove_button.is_visible():
            self.remove_button.dispatch_event("click")
            expect(self.save_button).to_be_visible()

    def open_comments(self) -> None:
        self.page_class.take_a_screenshot()
        if self.comment_button.is_visible():
            self.comment_button.dispatch_event("click")

    def expect_comment_button_visible(self) -> None:
        self.page_class.take_a_screenshot()
        expect(self.comment_button).to_be_visible()
