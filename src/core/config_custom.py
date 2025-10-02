import os
from __future__ import annotations
from dataclasses import dataclass
from dotenv import load_dotenv


load_dotenv()

@dataclass(frozen=True)
class ConfigCustom:
    pass

config_custom = ConfigCustom
