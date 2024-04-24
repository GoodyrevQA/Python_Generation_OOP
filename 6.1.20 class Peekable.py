# region description
'''
Реализуйте класс Peekable. При создании экземпляра класс должен принимать один аргумент:
iterable — итерируемый объект
Экземпляр класса Peekable должен являться итератором,
который генерирует элементы итерируемого объекта iterable в исходном порядке, а затем возбуждает исключение StopIteration.
Класс Peekable должен иметь один метод экземпляра:
peek() — метод, возвращающий следующий элемент итератора аналогично функции next(),
но при этом не сдвигающий итератор.
Если итератор пуст, должно быть возбуждено исключение StopIteration.
Также метод должен уметь принимать один необязательный аргумент default — объект,
который будет возвращен вместо возбуждения исключения StopIteration, если итератор пуст
'''
# endregion

class Peekable:

    def __init__(self, it):
        self._it = it
        self._c = 0
        
    def __iter__(self):
        return self
        
    def __next__(self):
        self._c += 1 
        if self._c > len(list(self._it)):
            raise StopIteration
        return self._it[self._c - 1]
        
    def peek(self, default='$'):
        try:
            return self._it[self._c]
        except Exception:
            if default == '$':
                raise StopIteration
            return default