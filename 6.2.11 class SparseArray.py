# region description
'''
Разреженный массив (список) — абстрактное представление обычного массива (списка),
в котором данные представлены не непрерывно, а фрагментарно:
большинство его элементов принимает одно и то же значение по умолчанию, обычно 0 или None.
В разреженном массиве возможен доступ к неопределенным элементам, в этом случае массив вернет некоторое значение по умолчанию.

Реализуйте класс SparseArray, описывающий разреженный массив. При создании экземпляра класс должен принимать один аргумент:
default — значение по умолчанию для неопределенных элементов разреженного массива
Экземпляр класса SparseArray должен позволять получать и изменять значения своих элементов с помощью индексов.
При попытке получить значение элемента по несуществующему индексу должно быть возвращено значение по умолчанию.
'''
# endregion

class SparseArray:

    def __init__(self, default):
        self.default = default
        self.dct = {}
        
    def __len__(self):
        return len(self.dct)
        
    def __getitem__(self, ind):
        if not isinstance(ind, int):
            raise TypeError
        if ind in self.dct:
            return self.dct[ind]
        else:
            return self.default   
        
    def __setitem__(self, ind, val):
        if not isinstance(ind, int):
            raise TypeError
        self.dct[ind] = val