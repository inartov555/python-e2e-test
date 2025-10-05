from dataclasses import dataclass


@dataclass(slots=True)
class SharedData:
    fixture_name: str = None
    current_test_name: str = None
    current_node_id: str = None
