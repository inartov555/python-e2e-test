from dataclasses import dataclass


@dataclass(frozen=True)
class SharedVariables:
    def __init__(self):
        raise NotImplementedError("This class is static and so creating a new instance is not allowed")

    page_obj = None  # playwright.sync_api._generated.Page, page fixture
