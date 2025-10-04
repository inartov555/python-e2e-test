import os
from dataclasses import dataclass
from dotenv import load_dotenv

from tools.singleton import Singleton


load_dotenv()

# @dataclass(frozen=True)
class CustomConfig(metaclass=Singleton):
    def __init__(self):
        self._is_headless = None
        self._viewport_width = None
        self._viewport_height = None
        self._base_url = None
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
