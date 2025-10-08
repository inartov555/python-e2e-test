"""
Tests for an authorized user
"""

import pytest

from tools.logger.logger import Logger
# pylint: disable=unused-import
from src.pages.private.conftest import \
    # pylint: disable=unused-import
    setup_cleanup_signin_signout, cleanup_remove_first, \
    cleanup_unlike_first
from src.pages.conftest import setup_elements_for_test


log = Logger(__name__)


class TestFeedAuth:
    """
    Tests for an authorized user
    """

    @pytest.mark.auth
    @pytest.mark.usefixtures('setup_cleanup_signin_signout')
    @pytest.mark.usefixtures('setup_elements_for_test')
    def test_feed_shows_posts(self):
        """
        Open the Home tab -> get the 1st visible post -> check if comment button is visible
        """
        self.home_page.go_to_home_tab()
        self.home_page.expect_feed_visible()
        first_post = self.home_page.first_post
        first_post.scroll_to_element_liked_by()
        first_post.expect_comment_button_visible()

    @pytest.mark.auth
    @pytest.mark.usefixtures('cleanup_unlike_first')
    @pytest.mark.usefixtures('setup_cleanup_signin_signout')
    @pytest.mark.usefixtures('setup_elements_for_test')
    def test_can_like_first_post(self):
        """
        Open the Home tab -> get the 1st visible post -> like the 1st post
        """
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
        """
        Open the Home tab -> get the 1st visible post -> save the 1st post
        """
        self.home_page.go_to_home_tab()
        first_post = self.home_page.first_post
        first_post.scroll_to_element_liked_by()
        first_post.expect_comment_button_visible()
        first_post.save()
