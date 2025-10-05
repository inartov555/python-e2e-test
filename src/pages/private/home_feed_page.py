from __future__ import annotations

from playwright.sync_api import expect

from ..base_page import BasePage
from ...components.post_card import PostCard
from tools.logger.logger import Logger


class HomeFeedPage(BasePage):
    """
    Authorized Home page
    """
    def __init__(self, url: str, page: Page, request):
        """
        Args:
            url (str): web site URL
            page (playwright.sync_api._generated.Page): page fixture
            request (_pytest.fixtures.SubRequest): request fixture
        """
        super().__init__(url, page, request)
        self.log = Logger(__name__)
        self.url = self.url + "/"

    @property
    def home_tab_active(self) -> Locator:
        """
        After it's clicked
        """
        return self.page.locator('a[href="/"]').first

    @property
    def home_tab_not_selected(self) -> Locator:
        """
        Before clicking
        """
        return self.page.locator('a[href="/?next=%2F"]').first

    @property
    def first_post(self) -> PostCard:
        root = self.page.locator('article').first
        return PostCard(root)

    @property
    def posts(self) -> list[PostCard]:
        roots = self.page.locator('article')
        count = roots.count()
        return [PostCard(roots.nth(i)) for i in range(count)]

    def go_to_home_tab(self) -> None:
        """
        Call this method only if the Home tab is not focused
        """
        self.take_a_screenshot()
        self.home_tab_not_selected.click()

    def expect_home_tab_not_selected_visible(self) -> None:
        self.take_a_screenshot()
        expect(self.home_tab_not_selected).to_be_visible()

    def expect_feed_visible(self) -> None:
        self.take_a_screenshot()
        expect(self.page.locator('article').first).to_be_visible()
