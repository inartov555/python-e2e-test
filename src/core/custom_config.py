from dataclasses import dataclass

# from tools.singleton import Singleton


@dataclass(frozen=True)
class CustomConfig:
    browser: str = None
    base_url: str = None
    is_headless: bool = None
    width: int = None
    height: int = None

    def __init__(self):
        raise NotImplemented("This class is static and so creating a new instance is not allowed")

    @staticmethod
    def change_variables(**kwargs):
        """
        Call it only when reading *.ini config file
        """
        for key in kwargs:
            setattr(CustomConfig, key, kwargs[key])

'''
@dataclass
class CustomConfig(metaclass=Singleton):
    def __init__(self):
        self._browser: str = None
        self._base_url: str = None
        self._is_headless: bool = None
        self._width: int = None
        self._height: int = None

    def set_parameters(self, param_dict: dict):
        """
        Args:
            param_dict (dict): it should be passed only once when setting parameters from the *.ini file
        """
        self._browser = param_dict.get("browser")
        self._base_url = param_dict.get("base_url")
        self._is_headless = param_dict.get("is_headless")
        self._width = param_dict.get("width")
        self._height = param_dict.get("height")
        # storage_state = os.getenv("STORAGE_STATE") or None

    @property
    def browser(self) -> str:
        """
        Returns:
            str, one of ("chromium", "chrome", "msedge", firefox, "webkit", "safari")
        """
        return self._browser

    @property
    def base_url(self) -> str:
        return self._base_url

    @property
    def is_headless(self) -> bool:
        return self._is_headless

    @property
    def width(self) -> int:
        return self._width

    @property
    def height(self) -> int:
        return self._height
'''

custom_config_global = CustomConfig
