import pytest
from src.core.config_custom import config_custom


def pytest_addoption(parser):
    parser.addoption("--has-auth", action="store_true", default=False,
                     help="Enable tests that require auth")

def pytest_collection_modifyitems(session, config, items):
    if not config_custom.has_auth:
        skip_marker = pytest.mark.skip(reason="No STORAGE_STATE provided; skipping auth tests.")
        for item in items:
            if 'auth' in getattr(item, 'keywords', {}):
                item.add_marker(skip_marker)
