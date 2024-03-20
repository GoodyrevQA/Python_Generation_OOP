# region description
'''
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
'''
# endregion

class ProtectedObject:

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __getattribute__(self, attr):
        if hasattr(self, attr) and attr.startswith('_'):
            raise AttributeError('Доступ к защищенному атрибуту невозможен')
        object.__getattribute__(self, attr)

    def __setattr__(self, k, v):
        if hasattr(self, k) and k.startswith('_'):
            raise AttributeError('Доступ к защищенному атрибуту невозможен')
        object.__setattr__(self, k, v)

    def __delattr__(self, k):
        if hasattr(self, k) and k.startswith('_'):
            raise AttributeError('Доступ к защищенному атрибуту невозможен')
        object.__delattr__(self, k)


user = ProtectedObject(login='PG_kamiya', _password='alreadybanned')

try:
    print(user.login)
    print(user.password)
except AttributeError as e:
    print(e)

print(user.__dict__)