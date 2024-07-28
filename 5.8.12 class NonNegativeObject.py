# region description
"""
Реализуйте класс NonNegativeObject.
При создании экземпляра класс должен принимать произвольное количество именованных аргументов.
Все передаваемые аргументы должны устанавливаться создаваемому экземпляру в качестве атрибутов,
причем если значением атрибута является отрицательное число, оно должно быть взято с противоположным знаком.

Примечание 1. Числами будем считать экземпляры классов int и float.
"""
# endregion


class NonNegativeObject:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __setattr__(self, name, value):
        if isinstance(value, int | float) and value < 0:
            value = -value
        object.__setattr__(self, name, value)
