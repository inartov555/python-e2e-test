from __future__ import annotations

from playwright.sync_api import Locator, expect

from ..base_page import BasePage
from tools.logger.logger import Logger


class LandingPage(BasePage):
    def __init__(self, url: str, page: Page, request):
        """
        Args:
            url (str): web site URL
            page (playwright.sync_api._generated.Page): page fixture
            request (_pytest.fixtures.SubRequest): request fixture
        """
        super().__init__(url, page, request)
        self.log = Logger(__name__)
        self.url = self.url + "/"

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
        return self.locator('img[href="/images/assets_DO_NOT_HARDCODE/lox_brand/landing-2x.png"]')

    def go_to_signup(self) -> None:
        self.log.info("Go to the Sign up page")
        self.take_a_screenshot()
        self.signup_link.click()

    def expect_loaded(self) -> None:
        self.log.info("Verifying if the Log in page's landing image is shown")
        self.take_a_screenshot()
        expect(self.landing_image).to_be_visible()
