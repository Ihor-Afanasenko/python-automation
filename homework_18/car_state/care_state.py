from enum import Enum


class CarState(Enum):
    LOADING = 0,
    UNLOADING = 1,
    ON_WAY = 2,
    UNDER_REPAIR = 3,
    READY_TO_SHIP = 4,
    REPAIR_REQUIRED = 5,
    SERVICE_NEEDED = 6

