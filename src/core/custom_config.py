import os
from dataclasses import dataclass
from dotenv import load_dotenv

from tools.singleton import Singleton


load_dotenv()

# @dataclass(frozen=True)
class CustomConfig(metaclass=Singleton):
    def __init__(self, param_dict: dict):
        """
        Args:
            param_dict (dict): it should be passed only once when setting parameters from the *.ini file
        """
        self._base_url = param_dict.get("base_url")
        self._is_headless = param_dict.get("is_headless")
        self._viewport_width = param_dict.get("viewport_width")
        self._viewport_height = param_dict.get("viewport_height")
        # storage_state = os.getenv("STORAGE_STATE") or None

    @property
    def is_headless(self) -> bool:
        return self._is_headless

    @property
    def viewport_width(self) -> int:
        return self._viewport_width

    @property
    def viewport_height(self) -> int:
        return self._viewport_height

    @property
    def base_url(self) -> str:
        return self._base_url

config_custom = CustomConfig
