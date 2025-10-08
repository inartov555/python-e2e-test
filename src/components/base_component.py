"""
Base methods for derived components
"""

from __future__ import annotations

from playwright.sync_api import Locator

from tools.logger.logger import Logger
from src.pages.base_page import BasePage


log = Logger(__name__)


class BaseComponent:
    """
    Base methods for derived components
    """
    def __init__(self, root: Locator, page_class: BasePage):
        """
        Args:
            root (Locator): locator
            page_clas (BasePage): a page derived from BasePage
        """
        self.root = root
        self.page_class = page_class
