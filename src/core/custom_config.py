from dataclasses import dataclass

from tools.logger.logger import Logger


@dataclass(frozen=True)
class CustomConfig:
    action_timeout: int = None
    navigation_timeout: int = None
    assert_timeout: int = None
    take_screenshot: bool = None
    browser: str = None
    base_url: str = None
    is_headless: bool = None
    width: int = None
    height: int = None
    username: str = None
    password: str = None

    def __init__(self):
        raise NotImplemented("This class is static and so creating a new instance is not allowed")

    @staticmethod
    def change_variables(**kwargs):
        """
        Call it only when reading *.ini config file
        """
        log = Logger(__name__)
        log.info("Changing variable value for CustomConfig")
        for key in kwargs:
            setattr(CustomConfig, key, kwargs[key])


custom_config_global = CustomConfig
