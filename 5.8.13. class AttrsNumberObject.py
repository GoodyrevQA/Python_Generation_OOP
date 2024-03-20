# region description
'''
Реализуйте класс AttrsNumberObject.
При создании экземпляра класс должен принимать произвольное количество именованных аргументов.
Все передаваемые аргументы должны устанавливаться создаваемому экземпляру в качестве атрибутов.

Экземпляр класса AttrsNumberObject должен иметь один атрибут:
attrs_num — количество атрибутов, которыми обладает экземпляр класса AttrsNumberObject на данный момент,
включая сам атрибут attrs_num
'''
# endregion

class AttrsNumberObject:

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self.attrs_num = len(self.__dict__) + 1

    def __setattr__(self, k, v):
        object.__setattr__(self, k, v)
        object.__setattr__(self, 'attrs_num', len(self.__dict__))

    def __delattr__(self, name):
        object.__delattr__(self, name)
        object.__setattr__(self, 'attrs_num', len(self.__dict__))


