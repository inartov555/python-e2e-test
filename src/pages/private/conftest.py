"""
conftest.py
"""

import time

import pytest

from tools.logger.logger import Logger


log = Logger(__name__)


@pytest.fixture(autouse=False, scope="function")
def setup_cleanup_signin_signout(request) -> None:
    """
    Setup & cleanup. Signin and the sign out
    """
    log.info("Setup. Sign in...")
    request.cls.login_page.open()
    request.cls.login_page.allow_all_cookies_if_shown()
    request.cls.login_page.expect_loaded()
    request.cls.login_page.login(request.cls.login_page.app_config.username,
                                 request.cls.login_page.app_config.password)
    if request.cls.login_page.app_config.wait_to_handle_capture_manually:
        log.warning("Wating 120 seconds after logging in to handle email confirmation or capture manually")
        time.sleep(120)
    request.cls.home_page.expect_home_tab_visible()
    # Let's update the page for the HomePage
    request.cls.home_page.ui_driver = request.cls.login_page.ui_driver
    yield
    log.info("Cleanup. Sign out")
    request.cls.home_page.open()
    request.cls.home_page.open_menu_overlay()
    request.cls.home_page.menu_overlay.log_out()
    request.cls.landing_page.expect_loaded()


@pytest.fixture(autouse=False, scope="function")
def cleanup_remove_first(request) -> None:
    """
    Cleanup. Removing the 1st post from saved ones
    """
    yield
    log.info("Cleanup. Removing the 1st post")
    request.cls.home_page.go_to_home_tab()
    first_post = request.cls.home_page.first_post
    first_post.scroll_to_element_liked_by()
    first_post.remove()


@pytest.fixture(autouse=False, scope="function")
def cleanup_unlike_first(request) -> None:
    """
    Cleanup. Unliking the 1st post
    """
    yield
    log.info("Cleanup. Unliking the 1st post")
    request.cls.home_page.go_to_home_tab()
    first_post = request.cls.home_page.first_post
    first_post.scroll_to_element_liked_by()
    first_post.unlike()
