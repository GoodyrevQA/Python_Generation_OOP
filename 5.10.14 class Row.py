# region description
"""
Реализуйте класс Row, описывающий объект, содержащий произвольный набор атрибутов.
При создании экземпляра класс должен принимать произвольное количество именованных аргументов
и устанавливать их в качестве атрибутов создаваемому экземпляру.

Класс Row должен запрещать устанавливать новые атрибуты своим экземплярам.
Помимо этого класс должен запрещать изменять значения уже имеющихся атрибутов, а также удалять их.
При попытке установить новый атрибут должно возбуждаться исключение AttributeError с текстом:

Установка нового атрибута невозможна
При попытке изменить значение уже имеющегося атрибута должно возбуждаться исключение AttributeError с текстом:
Изменение значения атрибута невозможно

При попытке удалить атрибут должно возбуждаться исключение AttributeError с текстом:
Удаление атрибута невозможно

Экземпляр класса Row должен иметь следующее формальное строковое представление:
Row(<имя 1-го атрибута>=<значение 1-го атрибута>, <имя 2-го атрибута>=<значение 2-го атрибута>, ...)
Также экземпляры класса Row должны поддерживать между собой операции сравнения с помощью операторов == и !=.
Два экземпляра класса Row считаются равными, если их наборы атрибутов полностью совпадают,
то есть совпадает их количество, позиции, имена и соответствующие значения.

Наконец, при передаче экземпляра класса Row в функцию hash() должно возвращаться его хеш-значение.
Алгоритм вычисления хеш-значения может быть произвольным, однако он должен учитывать все атрибуты экземпляра,
их позиции, имена и соответствующие значения
"""
# endregion


class Row:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __setattr__(self, k, v):
        if k in self.__dict__:
            raise AttributeError("Изменение значения атрибута невозможно")
        raise AttributeError("Установка нового атрибута невозможна")

    def __delattr__(self, k):
        if k in self.__dict__:
            raise AttributeError("Удаление атрибута невозможно")
        object.__delattr__(self, k)

    def __repr__(self):
        lst = [f"{k}={repr(v)}" for k, v in self.__dict__.items()]
        s = ", ".join(lst)
        return f"{__class__.__name__}({s})"

    def __eq__(self, other):
        if isinstance(other, Row):
            return tuple(self.__dict__.items()) == tuple(other.__dict__.items())
        return NotImplemented

    def __hash__(self):
        return hash(tuple(self.__dict__.items()))
