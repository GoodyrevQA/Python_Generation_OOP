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

array = [8022, 530.602391530928, 'lycmfojREEBSKNcNoIjM', False, {'написать': False, 'собеседник': True},
         (1448, True, -3913.85417440914, True),
         [True, True, 554, 'FCLRrFheVhkrubirMUts', -33242154218.4859, 885507704053.121]]

# for obj in array:
#     print(hash_function(obj))


print(hash_function([1, 2, 3, 'python']))


