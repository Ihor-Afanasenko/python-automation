from singleton import Singleton


class Logger(metaclass=Singleton):
    """
    Logger inherited metaclass Singleton and implementing singleton pattern
    """
    def log(self, msg: str) -> str:
        return f'Message -> {msg}'
