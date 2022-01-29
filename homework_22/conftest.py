import pytest

from human import Human
from nationality import Nationality


@pytest.fixture
def american() -> Nationality:
    yield Nationality("American")


@pytest.fixture
def british() -> Nationality:
    yield Nationality("British")


@pytest.fixture
def japan() -> Nationality:
    yield Nationality("Japan")


@pytest.fixture
def john_american(american) -> Human:
    human = Human("John", 23, "male", american)
    yield human


@pytest.fixture
def john_british(british) -> Human:
    yield Human("John", 23, "male", british)


@pytest.fixture
def mia_japan(japan) -> Human:
    yield Human("Mia", 25, "female", japan)
