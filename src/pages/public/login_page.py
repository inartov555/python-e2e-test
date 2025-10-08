"""
Login page
"""

from __future__ import annotations

from tools.logger.logger import Logger
from src.core.app_config import AppConfig
from src.core.ui_driver import UIDriver
from src.pages.base_page import BasePage
from src.components.login_form import LoginForm


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
        self.login_form_root = self.locator('form[id="loginForm"')
        self.allow_all_cookies_button = self.locator('button[class="_a9-- _ap36 _asz1"]')

    def login(self, username: str, password: str) -> None:
        """
        Log in
        """
        login_form = LoginForm(self.login_form_root, self)
        login_form.login(username, password)

    def expect_error_login(self) -> None:
        """
        Verifying if error test is shown when login failed due to incorrect credentials
        """
        login_form = LoginForm(self.login_form_root, self)
        login_form.expect_error_login()

    def expect_loaded(self) -> None:
        """
        Verifying if the Log in page is shown
        """
        log.info("Verifying if the Log in page is shown")
        login_form = LoginForm(self.login_form_root, self)
        login_form.expect_loaded()

    def allow_all_cookies_if_shown(self) -> None:
        """
        Confirming the allow cookies overlay, if shown
        """
        log.info("Confirming the allow cookies overlay, if shown")
        if self.allow_all_cookies_button.is_visible():
            self.allow_all_cookies_button.click()
