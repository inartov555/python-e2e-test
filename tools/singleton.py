class Singleton(type):
    """
    MultiClass singleton. It creates unique single instance for every inherited class.
    Is used in ServiceAPI and OpenAPI

    Note:
        os.environ.get("API_REPLACE_INSTANCE", "true") is used in the integration tests
    """
    _instance = dict()

    def __call__(cls, *args, **kwargs):
        instance_name = str(cls)
        Singleton._instance.setdefault(instance_name, None)
        if Singleton._instance[instance_name] is None:
            Singleton._instance[instance_name] = super(Singleton, cls).__call__(*args, **kwargs)
        return Singleton._instance[instance_name]
