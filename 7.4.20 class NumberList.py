# region description
"""
Класс NumberList
Реализуйте класс NumberList, наследника класса UserList, описывающий список, элементами которого могут быть лишь числа.
При создании экземпляра класс должен принимать один аргумент:
iterable — итерируемый объект, определяющий начальный набор элементов экземпляра класса NumberList.

Если хотя бы один элемент переданного итерируемого объекта не является числом, должно быть возбуждено исключение TypeError с текстом:
Элементами экземпляра класса NumberList должны быть числа

Итерируемый объект может быть не передан, в таком случае начальный набор элементов считается пустым
При изменении экземпляра класса NumberList с помощью индексов, операций сложения (+, +=)
и методов append(), extend() и insert() должна производиться проверка на то, что добавляемые элементы являются числами,
в противном случае должно возбуждаться исключение TypeError с текстом:
Элементами экземпляра класса NumberList должны быть числа
"""
# endregion

from collections import UserList

class NumberList(UserList):

    @staticmethod      
    def is_number(item):
        if isinstance(item, int | float) is False:
            raise TypeError('Элементами экземпляра класса NumberList должны быть числа')
        return True

    def __init__(self, iterable=()):
        for item in iterable:
            NumberList.is_number(item)
        super().__init__(iterable)

    def __setitem__(self, index, item):
        NumberList.is_number(item)
        self.data[index] = item

    def append(self, item):
        NumberList.is_number(item)
        self.data.append(item)

    def insert(self, index, item):
        NumberList.is_number(item)
        self.data.insert(index, item)

    def extend(self, other):
        if isinstance(other, type(self)):
            self.data.extend(other)
        else:
            for item in other:
                NumberList.is_number(item)
            self.data.extend(other)

    def __add__(self, other):
        for item in other:
            NumberList.is_number(item)
        return super().__add__(other)

    def __iadd__(self, other):
        for item in other:
            NumberList.is_number(item)
        super().__iadd__(other) 
        return self
