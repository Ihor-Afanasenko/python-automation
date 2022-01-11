class Singleton:
    """
    Implementation singleton using staticmethod
    """
    __instance = None

    def __init__(self):
        if Singleton.__instance is not None:
            raise Exception('This class has implementation, for call use method getInstance')
        else:
            Singleton.__instance = self

    @staticmethod
    def getInstance() -> type:
        if Singleton.__instance is None:
            Singleton()
        return Singleton.__instance
