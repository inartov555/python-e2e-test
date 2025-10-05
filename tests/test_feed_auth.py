import pytest

from tools.logger.logger import Logger
from src.pages.private.conftest import setup_cleanup_signin_signout, cleanup_remove_first, \
    cleanup_unlike_first
from src.pages.conftest import setup_elements_for_test


class TestFeedAuth:
    log = Logger(__name__)

    @pytest.mark.auth
    @pytest.mark.usefixtures('setup_cleanup_signin_signout')
    @pytest.mark.usefixtures('setup_elements_for_test')
    def test_feed_shows_posts(self):
        self.home_page.go_to_home_tab()
        self.home_page.expect_feed_visible()
        self.home_page.first_post.expect_visible()

    @pytest.mark.auth
    @pytest.mark.usefixtures('cleanup_unlike_first')
    @pytest.mark.usefixtures('setup_cleanup_signin_signout')
    @pytest.mark.usefixtures('setup_elements_for_test')
    def test_can_like_first_post(self):
        self.home_page.go_to_home_tab()
        first_post = self.home_page.first_post
        first_post.scroll_to_element_liked_by()
        first_post.expect_comment_button_visible()
        first_post.like()

    @pytest.mark.auth
    @pytest.mark.usefixtures('cleanup_remove_first')
    @pytest.mark.usefixtures('setup_cleanup_signin_signout')
    @pytest.mark.usefixtures('setup_elements_for_test')
    def test_can_save_first_post(self):
        self.home_page.go_to_home_tab()
        first_post = self.home_page.first_post
        first_post.scroll_to_element_liked_by()
        first_post.expect_comment_button_visible()
        first_post.save()
