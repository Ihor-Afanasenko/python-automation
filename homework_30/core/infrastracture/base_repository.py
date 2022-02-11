from ...core import Singleton, Config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session


class BaseRepository(Singleton):
    def __init__(self) -> None:
        self.__config = Config()
        self.__engine = create_engine(
            f"{self.__config.driver_name}://"
            f"{self.__config.user}:"
            f"{self.__config.password}@"
            f"{self.__config.host}:"
            f"{self.__config.port}/"
            f"{self.__config.database}")

        self._session: Session = sessionmaker(self.__engine, autocommit=True)()
