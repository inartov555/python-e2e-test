import os
# from __future__ import annotations
from dataclasses import dataclass
from dotenv import load_dotenv


load_dotenv()

# @dataclass(frozen=True)
class ConfigCustom:
    storage_state: str | None = os.getenv("STORAGE_STATE") or None

    @property
    def has_auth(self) -> bool:
        return bool(self.storage_state and os.path.exists(self.storage_state))

config_custom = ConfigCustom
