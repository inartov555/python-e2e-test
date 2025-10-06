from __future__ import annotations

from playwright.sync_api import Locator, expect

from ..base_page import BasePage
from tools.logger.logger import Logger
from src.core.app_config import AppConfig
from src.core.ui_driver import UIDriver


log = Logger(__name__)


class LandingPage(BasePage):
    def __init__(self, app_config: AppConfig, ui_driver: UIDriver):
        """
        / - URI path

        Args:
            app_config (AppConfig): app config passed in ini config file
            ui_driver (UIDriver): e.g., PlaywrightDriver adapter
        """
        super().__init__(app_config, "/", ui_driver)
        self.signup_link = self.locator('a[href="/accounts/emailsignup/"]')
        self.username_input = self.locator('input[name="username"]')
        self.password_input = self.locator('input[name="password"]')
        self.submit_button = self.locator('button[type="submit"]')
        self.error_text = self.locator('[role="alert"], #slfErrorAlert, div:has-text("incorrect")')
        self.forgot_password_link = self.locator('a[href="/accounts/password/reset/"]')
        self.landing_image = self.locator('img[src="/images/assets_DO_NOT_HARDCODE/lox_brand/landing-2x.png"]')

    def go_to_signup(self) -> None:
        log.info("Go to the Sign up page")
        self.signup_link.click()

    def expect_loaded(self) -> None:
        log.info("Verifying if the Log in page's landing image is shown")
        expect(self.landing_image).to_be_visible()
