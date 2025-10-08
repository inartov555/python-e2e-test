"""
Represents the login form in the landing and login pages.
"""

from __future__ import annotations

from playwright.sync_api import Locator, expect

from tools.logger.logger import Logger
from src.components.base_component import BaseComponent
from src.pages.base_page import BasePage


log = Logger(__name__)


class LoginForm(BaseComponent):
    """
    Represents the login form in the landing and login pages.
    """

    def __init__(self, root: Locator, page_class: BasePage):
        """
        Args:
            root (Locator): locator
            page_class (BasePage): the page derived from BasePage
        """
        super().__init__(root, page_class)
        self.username_input = self.locator('input[name="username"]')
        self.password_input = self.locator('input[name="password"]')
        self.submit_button = self.locator('button[type="submit"]')
        self.error_text = self.locator('[role="alert"], #slfErrorAlert, div:has-text("incorrect")')
        self.forgot_password_link = self.locator('a[href="/accounts/password/reset/"]')
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

    def expect_error_login(self) -> None:
        """
        Verifying if error test is shown when login failed due to incorrect credentials
        """
        log.info("Verifying if error log in text is shown")
        expect(self.incorrect_login_error_text).to_be_visible()    

    def expect_loaded(self) -> None:
        """
        Verifying if the Log in form is shown
        """
        log.info("Verifying if the Log in form is shown")
        expect(self.username_input).to_be_visible()
        expect(self.password_input).to_be_visible()
