from __future__ import annotations

from playwright.sync_api import Locator, expect

from ..base_page import BasePage
from tools.logger.logger import Logger
from src.core.app_config import AppConfig
from src.core.playwright_driver import PlaywrightDriver


log = Logger(__name__)


class LandingPage(BasePage):
    def __init__(self, app_config: AppConfig, pw_driver: PlaywrightDriver):
        """
        / - URI path

        Args:
            app_config (AppConfig): app config passed in ini config file
            pw_driver (PlaywrightDriver): adapter
        """
        super().__init__(app_config, "/", pw_driver)

    @property
    def signup_link(self) -> Locator:
        return self.locator('a[href="/accounts/emailsignup/"]')

    @property
    def username_input(self) -> Locator:
        return self.locator('input[name="username"]')

    @property
    def password_input(self) -> Locator:
        return self.locator('input[name="password"]')

    @property
    def submit_button(self) -> Locator:
        return self.locator('button[type="submit"]')

    @property
    def error_text(self) -> Locator:
        return self.locator('[role="alert"], #slfErrorAlert, div:has-text("incorrect")')

    @property
    def forgot_password_link(self) -> Locator:
        return self.locator('a[href="/accounts/password/reset/"]')

    @property
    def landing_image(self) -> Locator:
        return self.locator('img[src="/images/assets_DO_NOT_HARDCODE/lox_brand/landing-2x.png"]')

    def go_to_signup(self) -> None:
        log.info("Go to the Sign up page")
        self.signup_link.click()

    def expect_loaded(self) -> None:
        log.info("Verifying if the Log in page's landing image is shown")
        expect(self.landing_image).to_be_visible()
