from __future__ import annotations
from dataclasses import dataclass
import os
from dotenv import load_dotenv

load_dotenv()

@dataclass(frozen=True)
class ConfigCustom:
    base_url: str = os.getenv("BASE_URL", "https://www.instagram.com")
    headless: bool = os.getenv("HEADLESS", "false").lower() == "true"
    storage_state: str | None = os.getenv("STORAGE_STATE") or None
    viewport_width: int = int(os.getenv("VIEWPORT_WIDTH", "1920"))
    viewport_height: int = int(os.getenv("VIEWPORT_HEIGHT", "1080"))

    @property
    def has_auth(self) -> bool:
        return bool(self.storage_state and os.path.exists(self.storage_state))

config_custom = ConfigCustom()
