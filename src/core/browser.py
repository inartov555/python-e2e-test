from __future__ import annotations
import pytest
from playwright.sync_api import Playwright, sync_playwright, Browser, BrowserContext, Page
from .config import config
from .logger import get_logger

logger = get_logger(__name__)

@pytest.fixture(scope="session")
def playwright_instance() -> Playwright:
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="session")
def browser(playwright_instance: Playwright) -> Browser:
    browser = playwright_instance.chromium.launch(headless=config.headless)
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def browser_context(browser: Browser) -> BrowserContext:
    context_args = dict(
        viewport={"width": config.viewport_width, "height": config.viewport_height},
        record_video_dir="artifacts/video",
        base_url=config.base_url,
    )
    if config.has_auth:
        context_args["storage_state"] = config.storage_state  # type: ignore[index]
        logger.info("Using authenticated storage state: %s", config.storage_state)
    ctx = browser.new_context(**context_args)
    yield ctx
    ctx.close()

@pytest.fixture(scope="function")
def page(browser_context: BrowserContext) -> Page:
    page = browser_context.new_page()
    yield page
    page.screenshot(path="artifacts/screenshots/last_page.png", full_page=True)
