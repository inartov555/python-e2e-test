import pytest
from src.core.config import config

def pytest_collection_modifyitems(config_pytest, items):
    if not config.has_auth:
        skip_marker = pytest.mark.skip(reason="No STORAGE_STATE provided; skipping auth tests.")
        for item in items:
            if 'auth' in getattr(item, 'keywords', {}):
                item.add_marker(skip_marker)
