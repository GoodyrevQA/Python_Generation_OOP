# region description
"""
Будем считать атрибут защищенным, если его имя начинается с символа нижнего подчеркивания (_).
Например, _password, __email и __dict__.

Реализуйте класс ProtectedObject.
При создании экземпляра класс должен принимать произвольное количество именованных аргументов.
Все передаваемые аргументы должны устанавливаться создаваемому экземпляру в качестве атрибутов.

Класс ProtectedObject должен запрещать получать и изменять значения защищенных атрибутов своих экземпляров,
а также удалять эти атрибуты.
При попытке получить или изменить значение защищенного атрибута, а также попытке удалить атрибут,
должно возбуждаться исключение AttributeError с текстом:
Доступ к защищенному атрибуту невозможен
"""
# endregion


class ProtectedObject:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            object.__setattr__(self, k, v)

    def __getattribute__(self, attr):
        if attr.startswith("_"):
            raise AttributeError("Доступ к защищенному атрибуту невозможен")
        return object.__getattribute__(self, attr)

    def __setattr__(self, k, v):
        if k.startswith("_"):
            raise AttributeError("Доступ к защищенному атрибуту невозможен")
        object.__setattr__(self, k, v)

    def __delattr__(self, k):
        if k.startswith("_"):
            raise AttributeError("Доступ к защищенному атрибуту невозможен")
        object.__delattr__(self, k)
