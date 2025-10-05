import pytest

from tools.logger.logger import Logger


log = Logger(__name__)


@pytest.fixture(autouse=False, scope="class")
def setup_cleanup_signin_signout(request):
    log.info("Setup. Sign in...")
    request.cls.login_page.open()
    request.cls.login_page.allow_all_cookies_if_shown()
    request.cls.login_page.expect_loaded()
    request.cls.login_page.login(request.cls.login_page.custom_config.username,
                                 request.cls.login_page.custom_config.password)
    request.cls.home_page.expect_feed_visible()
    yield
    log.info("Cleanup. Sign out")
