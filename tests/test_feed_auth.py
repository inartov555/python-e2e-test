import pytest

from tools.logger.logger import Logger


class TestFeedAuth:

    @pytest.mark.auth
    def test_feed_shows_posts(self):
        feed = self.home_page.open()
        feed.expect_feed_visible()
        feed.first_post.expect_visible()

    @pytest.mark.auth
    def test_can_like_and_save_first_post(self):
        feed = self.home_page.open()
        post = feed.first_post
        post.expect_visible()
        post.like()
        post.save()
