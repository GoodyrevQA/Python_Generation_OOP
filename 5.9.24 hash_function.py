# region description
'''
https://stepik.org/lesson/886253/step/24?unit=890908
Реализуйте функцию hash_function(), которая принимает один аргумент:
obj — произвольный объект
Функция должна вычислять хеш-значение объекта obj согласно следующему алгоритму:

1. вычисление значения выражения:
ord(obj[0]) * ord(obj[-1]) + ord(obj[1]) * ord(obj[-2]) + ord(obj[2]) * ord(obj[-3]) + ...
где obj — объект, преобразованный в строку с помощью функции str().
Обратите внимание, что суммироваться должны произведения первого и последнего элементов, второго и предпоследнего,
и так далее до середины.
Если obj имеет нечетное количество символов, то серединный элемент должен прибавляться без перемножения

2. вычисление значения выражения:
ord(obj[0]) * 1 - ord(obj[1]) * 2 + ord(obj[2]) * 3 - ord(obj[3]) * 4 + ...
где obj — объект, преобразованный в строку с помощью функции str()

3. вычисление значения выражения:
(temp1 * temp2) % 123456791
где temp1 — значение, полученное в первом шаге, temp2 — значение, полученное во втором шаге
и возвращать значение, полученное в третьем шаге.
'''
# endregion

def hash_function(obj):
    obj = str(obj)

    def first(obj):
        h = 0
        if len(obj) % 2 == 1:
            mid = len(obj) // 2
            h += ord(obj[mid])

        L = 0
        R = len(obj) - 1
        while R > L:
            h += ord(obj[L]) * ord(obj[R])
            L += 1
            R -= 1
        return h

    def second(obj):
        h = 0
        for i in range(len(obj)):
            if i % 2 == 0:
                h += ord(obj[i]) * (i + 1)
            else:
                h -= ord(obj[i]) * (i + 1)
        return h

    ans = (first(obj) * second(obj)) % 123456791

    return ans


# region foreign solution
class HashFunction:
    def __call__(self, obj):
        self.obj = str(obj)
        return (self._e1(self.obj) * self._e2(self.obj)) % 123456791

    @staticmethod
    def _e1(obj):
        l = len(obj)
        return sum([ord(obj[i]) * ord(obj[-1 - i]) for i in range(l // 2)]) + (0, ord(obj[l // 2]))[l % 2]

    @staticmethod
    def _e2(obj):
        return sum([ord(obj[i]) * (i+1, -i-1)[i % 2] for i in range(len(obj))])


hash_function = HashFunction()
# endregion

