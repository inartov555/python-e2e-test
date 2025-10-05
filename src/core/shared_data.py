from dataclasses import dataclass

from tools.logger.logger import Logger
from tools.singleton import Singleton


@dataclass(frozen=True, slots=True)
class SharedData(metaclass=Singleton):
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
