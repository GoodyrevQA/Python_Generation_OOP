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
        obj1 = obj
        h = 0
        if len(obj1) % 2 == 1:
            ind_to_del = len(obj1) // 2
            char_to_del= obj1[ind_to_del]
            h += ord(char_to_del)
            obj1 = obj1.replace(char_to_del, '')

        L = 0
        R = len(obj1) - 1
        while R > L:
            h += ord(obj1[L]) * ord(obj1[R])
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

print(hash_function([1, 2, 3, 'python']))