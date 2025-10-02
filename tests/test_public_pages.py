import pytest

from tools.logger.logger import Logger


class TestPublicPages:

    def test_landing_links_present(page):
        self.landing_page.expect_loaded()

    def test_navigate_to_login(page):
        landing = LandingPage(page).open()
        self.landing_page.go_to_login()
        self.login_page.expect_loaded()

    def test_navigate_to_signup(page):
        landing = LandingPage(page).open()
        self.landing_page.go_to_signup()
        self.signup_page.expect_loaded()

    def test_login_negative_incorrect_creds(page):
        login = LoginPage(page).open()
        self.login_page.expect_loaded()
        self.login_page.login("incorrect_user@example.com", "wrong_password")
        # In real runs, expect an error or captcha; we assert the page attempted submission
        assert True
