from dataclasses import dataclass

from tools.logger.logger import Logger


@dataclass(slots=True)
class AppConfig:
    wait_to_handle_capture_manually: bool
    action_timeout: int
    navigation_timeout: int
    assert_timeout: int
    take_screenshot: bool
    browser: str
    base_url: str
    is_headless: bool
    width: int
    height: int
    username: str
    password: str
