from dataclasses import dataclass

# from tools.singleton import Singleton


@dataclass(frozen=True)
class CustomConfig:
    browser: str = None
    base_url: str = None
    is_headless: bool = None
    width: int = None
    height: int = None

    def __init__(self):
        raise NotImplemented("This class is static and so creating a new instance is not allowed")

    @staticmethod
    def change_variables(**kwargs):
        """
        Call it only when reading *.ini config file
        """
        for key in kwargs:
            setattr(CustomConfig, key, kwargs[key])


custom_config_global = CustomConfig
