from __future__ import annotations

from playwright.sync_api import Locator, expect

from tools.logger.logger import Logger
from src.pages.base_page import BasePage


log = Logger(__name__)


class BaseComponent:
    def __init__(self, root: Locator, page_class: BasePage):
        self.root = root
        self.page_class = page_class
