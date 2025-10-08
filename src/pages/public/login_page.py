"""
Login page
"""

from __future__ import annotations

from playwright.sync_api import Locator, expect

from ..base_page import BasePage
from tools.logger.logger import Logger
from src.core.app_config import AppConfig
from src.core.ui_driver import UIDriver


log = Logger(__name__)


class LoginPage(BasePage):
    """
    Login page
    """
    def __init__(self, app_config: AppConfig, ui_driver: UIDriver):
        """
        /accounts/login/ - URI path

        Args:
            app_config (AppConfig): app config passed in ini config file
            ui_driver (UIDriver): e.g., PlaywrightDriver adapter
        """
        super().__init__(app_config, "/accounts/login/", ui_driver)
        self.username_input = self.locator('input[name="username"]')
        self.password_input = self.locator('input[name="password"]')
        self.submit_button = self.locator('button[type="submit"]')
        self.error_text = self.locator('[role="alert"], #slfErrorAlert, div:has-text("incorrect")')
        self.forgot_password_link = self.locator('a[href="/accounts/password/reset/"]')
        self.allow_all_cookies_button = self.locator('button[class="_a9-- _ap36 _asz1"]')
        self.incorrect_login_error_text = \
            self.ui_driver.get_by_text("Sorry, your password was incorrect. Please double-check your password.")

    def login(self, username: str, password: str) -> None:
        """
        Log in
        """
        log.info("Logging in")
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.submit_button.click()

    def expect_loaded(self) -> None:
        """
        Verifying if the Log in page is shown
        """
        log.info("Verifying if the Log in page is shown")
        expect(self.username_input).to_be_visible()
        expect(self.password_input).to_be_visible()

    def allow_all_cookies_if_shown(self) -> None:
        """
        Confirming the allow cookies overlay, if shown
        """
        log.info("Confirming the allow cookies overlay, if shown")
        if self.allow_all_cookies_button.is_visible():
            self.allow_all_cookies_button.click()

    def expect_error_login(self) -> None:
        """
        Verifying if error test is shown when login failed due to incorrect credentials
        """
        log.info("Verifying if error log in text is shown")
        expect(self.incorrect_login_error_text).to_be_visible()
