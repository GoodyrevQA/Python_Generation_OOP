# region description
"""
Реализуйте класс MutableString, наследника класса UserString, описывающий изменяемую строку.
Процесс создания экземпляра класса MutableString должен совпадать с процессом создания экземпляра класса UserString.

Класс MutableString должен иметь три метода экземпляра:
lower() — метод, переводящий все символы изменяемой строки в нижний регистр
upper() — метод, переводящий все символы изменяемой строки в верхний регистр
sort() — метод, сортирующий символы изменяемой строки.
Может принимать два необязательных именованных аргумента key и reverse, выполняющих ту же задачу, что и в функции sorted()
"""
# endregion

from collections import UserString

class MutableString(UserString):

    def lower(self):
        self.data = self.data.lower()

    def upper(self):
        self.data = self.data.upper()

    def sort(self, key=None, reverse=False):
        lst = sorted(self.data, key=key, reverse=reverse)
        self.data = ''.join(lst)

    def __setitem__(self, key, value):
        lst = list(self.data)
        lst[key] = value
        self.data = ''.join(lst)

    def __delitem__(self, key):
        lst = list(self.data)
        del lst[key]
        self.data = ''.join(lst)
