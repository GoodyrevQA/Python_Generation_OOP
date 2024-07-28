# region description
"""
Реализуйте класс LoopTracker. При создании экземпляра класс должен принимать один аргумент:
iterable — итерируемый объект

Экземпляр класса LoopTracker должен являться итератором,
который генерирует элементы итерируемого объекта iterable в исходном порядке, а затем возбуждает исключение StopIteration.

Класс LoopTracker должен иметь четыре свойства:

accesses — свойство, доступное только для чтения, возвращающее количество элементов, сгенерированных итератором на данный момент

empty_accesses — свойство, доступное только для чтения, возвращающее количество попыток получить следующий элемент опустевшего итератора

first — свойство, доступное только для чтения, возвращающее первый элемент итератора и не сдвигающее его.
Если итератор не имеет первого элемента, то есть создан на основе пустого итерируемого объекта,
то должно быть возбуждено исключение AttributeError с текстом:
Исходный итерируемый объект пуст

last — свойство, доступное только для чтения, возвращающее последний элемент, сгенерированный итератором на данный момент.
Если итератор еще не сгенерировал ни одного элемента, то должно быть возбуждено исключение AttributeError с текстом:
Последнего элемента нет

Класс LoopTracker должен иметь один метод экземпляра:

is_empty() — метод, возвращающий True, если итератор опустошен, или False в противном случае

Примечание 1. Дополнительная проверка данных на корректность не требуется.
Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Класс LoopTracker должен удовлетворять протоколу итератора,
то есть иметь методы __iter__() и __next__(). Реализация же протокола может быть произвольной.
"""
# endregion


class LoopTracker:
    def __init__(self, it):
        if isinstance(it, dict):
            self._it = list(it.keys())
        else:
            self._it = it
        self._c = 0
        self._empty = 0

    def __iter__(self):
        return self

    def __next__(self):
        self._c += 1
        if self._c > len(list(self._it)):
            self._empty += 1
            raise StopIteration
        self._last = self._it[self._c - 1]
        return self._last

    @property
    def empty_accesses(self):
        return self._empty

    @property
    def accesses(self):
        return self._c - self._empty

    @property
    def first(self):
        try:
            return list(self._it)[0]
        except IndexError:
            raise AttributeError("Исходный итерируемый объект пуст")

    @property
    def last(self):
        if "_last" in self.__dict__:
            return self._last
        else:
            raise AttributeError("Последнего элемента нет")

    def is_empty(self):
        return self._c >= len(list(self._it))


"""
# TEST_6:
False
False
True

# TEST_7:
1
1

# TEST_8:
Исходный итерируемый объект пуст

# TEST_9:
1
1
2
2

# TEST_10:
Последнего элемента нет

# TEST_11:
1000
99000

# TEST_12:
0
1
2
3
0
2
False

# TEST_13:
<class 'AttributeError'>
<class 'AttributeError'>
<class 'AttributeError'>
"""

loop_tracker = LoopTracker([1, 2, 3])

try:
    loop_tracker.accesses = 1
except AttributeError as e:
    print(type(e))

try:
    loop_tracker.first = 1
except AttributeError as e:
    print(type(e))

try:
    loop_tracker.last = 1
except AttributeError as e:
    print(type(e))
