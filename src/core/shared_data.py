from dataclasses import dataclass

from tools.logger.logger import Logger
from tools.singleton import Singleton


@dataclass(slots=True)
class SharedData(metaclass=Singleton):
    """
    The data that is placed in this class is retrieved in a function-scoped fixture.
    We need this data to be available even when test is finished.
    """
    fixture_name: str = None
    current_test_name: str = None
    current_node_id: str = None
    page_obj: str = None

    @staticmethod
    def change_variables(**kwargs):
        """
        Call it only when a parameter gets changed
        """
        log = Logger(__name__)
        log.info("Changing variable value for SharedData")
        for key in kwargs:
            setattr(SharedData, key, kwargs[key])


shared_data_global = SharedData()
