class Singleton(type):
    """
    It creates unique single instance for every inherited class.
    """
    _instance = dict()

    def __call__(cls, *args, **kwargs):
        instance_name = str(cls)
        Singleton._instance.setdefault(instance_name, None)
        if Singleton._instance[instance_name] is None:
            Singleton._instance[instance_name] = super(Singleton, cls).__call__(*args, **kwargs)
        return Singleton._instance[instance_name]
