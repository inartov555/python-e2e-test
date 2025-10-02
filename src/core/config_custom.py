import os
from dataclasses import dataclass
from dotenv import load_dotenv

from tools.singleton import Singleton


load_dotenv()

# @dataclass(frozen=True)
class CustomConfig(metaclass=Singleton):
    def __init__(self):
        storage_state = os.getenv("STORAGE_STATE") or None

    @property
    def has_auth(self) -> bool:
        return bool(self.storage_state and os.path.exists(self.storage_state))

config_custom = ConfigCustom
