# region description
'''
Реализуйте класс Ord. При создании экземпляра класс не должен принимать никаких аргументов.

Экземпляр класса Ord должен выступать в качестве альтернативы функции ord().
При обращении к атрибуту экземпляра, именем которого является одиночный символ,
должна возвращаться его позиция в таблице символов Unicode.
'''
# endregion

class Ord:

    def __getatt__(self, name):
        return ord(name)
