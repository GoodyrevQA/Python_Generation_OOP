# region description
'''
https://stepik.org/lesson/805783/step/12?unit=808910
Реализуйте класс RomanNumeral, описывающий число в римской системе счисления.
При создании экземпляра класс должен принимать один аргумент:

number — число в римской системе счисления. Например, IV
Экземпляр класса RomanNumeral должен иметь следующее неформальное строковое представление:

<число в римской системе счисления>
Помимо этого, экземпляр класса RomanNumeral должен поддерживать приведение к типу int,
при приведении к которому его значением должно являться целое число в десятичной системе счисления, которому он соответствует.

Также экземпляры класса RomanNumeral должны поддерживать между собой все операции сравнения с помощью операторов ==, !=, >, <, >=, <=.

Наконец, экземпляры класса RomanNumeral должны поддерживать между собой операции сложения и вычитания
с помощью операторов + и - соответственно:

результатом сложения должен являться новый экземпляр класса RomanNumeral, представляющий сумму исходных
результатом вычитания должен являться новый экземпляр класса RomanNumeral, представляющий разность исходных
'''
# endregion

from functools import total_ordering

@total_ordering
class RomanNumeral:

    @staticmethod
    def roman_to_int(s):
        dct = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        res = 0

        for i in range(len(s) - 1):
            if dct[s[i]] >= dct[s[i+1]]:
                res += dct[s[i]]
            else:
                res -= dct[s[i]]
        res += dct[s[-1]]
        return res


    @staticmethod
    def int_to_roman(n):

        dct = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'
        }

        res = ''

        for arabic in list(dct)[::-1]:
            while n >= arabic:
                res += dct[arabic]
                n -= arabic

        return res


    def __init__(self, number):
        self.number = number

    def __str__(self):
        return self.number

    def __int__(self):
        arabic_number = RomanNumeral.roman_to_int(self.number)
        return arabic_number

    def __eq__(self, other):
        if isinstance(other, __class__):
            return int(self) == int(other)
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, __class__):
            return int(self) < int(other)
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, __class__):
            arabic_sum = int(self) + int(other)
            roman_sum = RomanNumeral.int_to_roman(arabic_sum)
            return __class__(roman_sum)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, __class__):
            arabic_sub = int(self) - int(other)
            roman_sub = RomanNumeral.int_to_roman(arabic_sub)
            return __class__(roman_sub)
        return NotImplemented

