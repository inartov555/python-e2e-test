from __future__ import annotations
from playwright.sync_api import Locator, expect

class PostCard:
    """Represents a post in the Instagram home feed."""
    def __init__(self, root: Locator):
        self.root = root
        # Heuristic selectors; Instagram is dynamic and often changes, so these are best-effort.
        self.like_button = root.locator('button[aria-label*="Like"], svg[aria-label="Like"]').first
        self.unlike_button = root.locator('svg[aria-label="Unlike"]').first
        self.save_button = root.locator('button[aria-label*="Save"], svg[aria-label="Save"]').first
        self.comment_button = root.locator('button[aria-label*="Comment"], svg[aria-label="Comment"]').first

    def like(self) -> None:
        if self.like_button.is_visible():
            self.like_button.click()

    def unlike(self) -> None:
        if self.unlike_button.is_visible():
            self.unlike_button.click()

    def save(self) -> None:
        if self.save_button.is_visible():
            self.save_button.click()

    def open_comments(self) -> None:
        if self.comment_button.is_visible():
            self.comment_button.click()

    def expect_visible(self) -> None:
        expect(self.root).to_be_visible()
