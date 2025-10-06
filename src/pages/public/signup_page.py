from __future__ import annotations

from playwright.sync_api import Locator, expect

from ..base_page import BasePage
from tools.logger.logger import Logger
from src.core.app_config import AppConfig
from src.core.ui_driver import UIDriver


log = Logger(__name__)


class SignupPage(BasePage):
    def __init__(self, app_config: AppConfig, ui_driver: UIDriver):
        """
        /accounts/emailsignup/ - URI path

        Args:
            app_config (AppConfig): app config passed in ini config file
            ui_driver (UIDriver): e.g., PlaywrightDriver adapter
        """
        super().__init__(app_config, "/accounts/emailsignup/", ui_driver)
        self.email_or_phone = self.locator('input[name="emailOrPhone"]')
        self.full_name = self.locator('input[name="fullName"]')
        self.username = self.locator('input[name="username"]')
        self.password = self.locator('input[name="password"]')
        self.submit_button = self.locator('button[type="submit"]')
        self.login_link = self.locator('a[href="/accounts/login/?source=auth_switcher"]')

    def go_to_login(self) -> None:
        log.info("Go to log in")
        self.login_link.click()

    def expect_loaded(self) -> None:
        log.info("Verifying if the Log in screen is shown")
        expect(self.email_or_phone).to_be_visible()
        expect(self.full_name).to_be_visible()
        expect(self.username).to_be_visible()
        expect(self.password).to_be_visible()
