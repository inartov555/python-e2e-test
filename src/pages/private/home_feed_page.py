from __future__ import annotations

from playwright.sync_api import expect

from ..base_page import BasePage
from ...components.post_card import PostCard
from tools.logger.logger import Logger


class HomeFeedPage(BasePage):
    def __init__(self, url: str, page: Page, request):
        super().__init__(url, page, request)
        self.url = self.url + "/"

    @property
    def first_post(self) -> PostCard:
        root = self.page.locator('article').first
        return PostCard(root)

    @property
    def posts(self) -> list[PostCard]:
        roots = self.page.locator('article')
        count = roots.count()
        return [PostCard(roots.nth(i)) for i in range(count)]

    def expect_feed_visible(self) -> None:
        expect(self.page.locator('article').first).to_be_visible()
