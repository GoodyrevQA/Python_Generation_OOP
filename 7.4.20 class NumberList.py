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



# INPUT DATA:

# TEST_1:
numberlist = NumberList([1, 2])

numberlist.append(3)
numberlist.extend([4, 5])
numberlist.insert(0, 0)
print(numberlist)

# TEST_2:
numberlist = NumberList([0, 1.0])

numberlist[1] = 1
numberlist = numberlist + NumberList([2, 3])
numberlist += NumberList([4, 5])
print(numberlist)

# TEST_3:
try:
    numberlist = NumberList(['a', 'b', 'c'])
except TypeError as error:
    print(error)

# TEST_4:
numberlist = NumberList([1, 2, 3])

try:
    numberlist.append('4')
except TypeError as error:
    print(error)

# TEST_5:
numberlist = NumberList([1, 2])

try:
    numberlist += [3, '4']
except TypeError as e:
    print(e)

# TEST_6:
numberlist1 = NumberList([1, 2])

try:
    numberlist2 = numberlist1 + [3, '4']
except TypeError as e:
    print(e)

# TEST_7:
data = [1, 2, 3]
numberlist = NumberList(data)

print(numberlist)

data.extend([4, 5, 6])
print(data)
print(numberlist)

# TEST_8:
numberlist = NumberList([1, 2])
try:
    numberlist.insert(0, [5, 4, 3])
except TypeError as e:
    print(e)

# TEST_9:
numberlist = NumberList([1, 2])
try:
    numberlist.extend([5, '4', 3])
except TypeError as e:
    print(e)

# TEST_10:
n = NumberList([1, 2, 3])

try:
    n[1] = '5'
except TypeError as e:
    print(e)
