# region description
"""
Реализуйте класс CyclicList, описывающий циклический список. При создании экземпляра класс должен принимать один аргумент:
iterable — итерируемый объект, определяющий начальный набор элементов циклического списка.
Если не передан, начальный набор элементов считается пустым

Класс CyclicList должен иметь два метода экземпляра:
append() — метод, принимающий в качестве аргумента произвольный объект и добавляющий его в конец циклического списка
pop() — метод, который принимает в качестве аргумента индекс элемента циклического списка,
возвращает его значение и удаляет из циклического списка элемент с данным индексом.
Если аргумент не передан, возвращаемым и удаляемым элементом считается последний элемент циклического списка

При передаче экземпляра класса CyclicList в функцию len() должно возвращаться количество элементов в нем.
Также экземпляр класса CyclicList должен быть зацикленным итерируемым объектом.
Другими словами, итерация по нему должна происходить бесконечно, и при каждом достижении его последнего элемента она должна начинаться сначала.

Наконец, экземпляр класса CyclicList должен позволять получать значения своих элементов с помощью индексов,
при этом индексы должны работать циклически. Например, в циклическом списке [1, 2, 3] элементом с индексом 4 должно являться число 2.
"""

# endregion
from itertools import cycle


class CyclicList:
    def __init__(self, iterable=None):
        if iterable:
            self.it = list(iterable)
        else:
            self.it = []

    def __iter__(self):
        yield from cycle(self.it)

    def __len__(self):
        return len(self.it)

    def __getitem__(self, ind):
        if not isinstance(ind, int):
            raise TypeError
        if self.it:
            return list(self.it)[ind % len(self.it)]
        else:
            raise IndexErrorError

    def append(self, obj):
        self.it.append(obj)

    def pop(self, indx=-1):
        el = self.__getitem__(indx)
        del self.it[indx]
        return el


# region foreign_solution


from itertools import cycle


# class CyclicList:
#     def __init__(self, iterable=()):
#         self._data = list(iterable) or []

#     def append(self, item):
#         self._data.append(item)

#     def pop(self, index=None):
#         if index is None:
#             return self._data.pop()
#         return self._data.pop(index)

#     def __len__(self):
#         return len(self._data)

#     def __iter__(self):
#         yield from cycle(self._data)

#     def __getitem__(self, index):
#         return self._data[index % len(self._data)]

# endregion
