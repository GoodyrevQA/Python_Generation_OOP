# region description
"""
Реализуйте класс DefaultObject.
При создании экземпляра класс должен принимать один именованный аргумент default,
имеющий значение по умолчанию None, а после произвольное количество именованных аргументов.
Аргументы, передаваемые после default, должны устанавливаться создаваемому экземпляру в качестве атрибутов.
При обращении к несуществующему атрибуту экземпляра класса DefaultObject должно возвращаться значение default
"""
# endregion


class DefaultObject:
    def __init__(self, default=None, **kwargs):
        self.default = default
        self.__dict__.update(kwargs)

    def __getattr__(self, attr):
        return self.default
