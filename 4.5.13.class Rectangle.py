"""
https://stepik.org/lesson/796462/step/13?unit=799267
Реализуйте класс Rectangle, описывающий прямоугольник. При создании экземпляра класс должен принимать два аргумента в следующем порядке:

length — длина прямоугольника
width — ширина прямоугольника
Экземпляр класса Rectangle должен иметь два атрибута:

length — длина прямоугольника
width — ширина прямоугольника
Класс Rectangle должен иметь два свойства:

perimeter — свойство, доступное только для чтения, возвращающее периметр прямоугольника
area — свойство, доступное только для чтения, возвращающее площадь прямоугольника
"""
# endregion


class Rectangle:
    
    def __init__(self, length, width):
        self._width = width       # настоящие атрибуты экземпляра защищенные
        self._length = length
        
    def get_length(self):
        return self._length
    
    def set_length(self, l):
        self._length = l
    
    def get_width(self):
        return self._width
    
    def set_width(self, w):
        self._width = w
        
    def get_perimeter(self):
        return (self.length + self.width) * 2    # здесь вызываются свойства length и width
    
    def get_area(self):
        return (self.length * self.width)    # здесь вызываются свойства length и width
    
    length = property(fget=get_length, fset=set_length)
    width = property(fget=get_width, fset=set_width)
    perimeter = property(fget=get_perimeter)
    area = property(fget=get_area)
