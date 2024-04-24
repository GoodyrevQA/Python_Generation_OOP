# region description
'''
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
'''
# endregion

def limited_hash(left, right, hash_function=hash):

    def new_function(obj):
        dif = right - left + 1
        row_ans = hash_function(obj)

        if row_ans > right:
            shift = row_ans % right
            if shift >= dif:
                shift = shift % dif 
            return left + shift 

        elif row_ans < left:
            shift = left - row_ans 
            if shift > dif:
                shift = shift % dif 
            return right - shift + 1

        return row_ans

    return new_function



def hash_function(obj):
    return sum(index * ord(character) for index, character in enumerate(str(obj), start=1))


hash_function = limited_hash(10, 15, hash_function)

array = [1366, -5502567186.7395, 'zZQyrjYzdgcabTZPATPl', False, {'монета': -671699723096.267, 'лететь': 5151},
         (False, True, 897, -844416.51017117, 1101),
         [True, 171664.794743347, True, False, 'UypAaBSjBWYWBYbmRTdN', 4044844490314.56]]

for item in array:
    print(hash_function(item))