from typing import Type


class Modification:
    """
    Decorator class with parameter - name, and be able to set modification name and
    all modifications to the class that decorating
    """
    def __init__(self, name) -> None:
        self.__name = name
        self.__modification = []

    def __call__(self, _type: Type) -> Type:
        setattr(_type, f'_{_type.__name__}__last_modification', self.__name)
        self.__modification.extend([self.__name])
        if hasattr(_type, f'_{_type.__name__}__modifications'):
            current_modifications = getattr(_type, f'_{_type.__name__}__modifications')
            current_modifications.extend([self.__name])
            setattr(_type, f'_{_type.__name__}__modifications', current_modifications)
        else:
            setattr(_type, f'_{_type.__name__}__modifications', self.__modification)
        return _type
