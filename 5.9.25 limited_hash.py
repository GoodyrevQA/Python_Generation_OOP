# region description
"""
Реализуйте функцию limited_hash(), которая принимает три аргумента в следующем порядке:
left — целое число
right — целое число
hash_function — хеш-функция, по умолчанию равняется встроенной функции hash()

Функция должна возвращать новую функцию, которая принимает в качестве аргумента произвольный объект,
вычисляет его хеш-значение с помощью функции hash_function(), преобразует его в число,
принадлежащее диапазону [left; right], и возвращает полученный результат.

Если вычисленное хеш-значение уже принадлежит диапазону [left; right], то функция должна возвращать его без преобразования.
Если вычисленное хеш-значение равняется right + 1, то функция перед возвратом должна преобразовать его в left,
если right + 2 — в left + 1, если right + 3 — в left + 2, и так далее.
Аналогичные преобразования, но в другую сторону, должны выполняться для хеш-значений, которые меньше left.
Преобразования должны выполняться циклично при очередном выходе из диапазона.
"""
# endregion


def limited_hash(left, right, hash_function=hash):
    def new_function(obj):
        dif = right - left + 1
        row_ans = hash_function(obj)

        if row_ans > right:
            shift = row_ans - right

            while shift > dif:
                shift -= dif

            return left + shift - 1

        elif row_ans < left:
            shift = left - row_ans
            if shift > dif:
                shift = shift % dif
            return right - shift + 1

        return row_ans

    return new_function


# region foreign solutions
def limited_hash(left, right, hash_function=hash):
    def inner_hash_function(x):
        return left + (hash_function(x) - left) % (right - left + 1)

    return inner_hash_function


def limited_hash(left, right, hash_function=hash):
    def inner_hash_function(obj):
        hash_value = hash_function(obj)
        if hash_value < left:
            hash_value = right - (left - hash_value - 1) % (right - left + 1)
        elif hash_value > right:
            hash_value = left + (hash_value - right - 1) % (right - left + 1)
        return hash_value

    return inner_hash_function


# endregion
