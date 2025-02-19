# region description
"""
https://stepik.org/lesson/796462/step/14?unit=799267
Реализуйте класс HourClock, описывающий часы с одной лишь часовой стрелкой.
При создании экземпляра класс должен принимать один аргумент:

hours — количество часов. Если hours не является целым числом,
принадлежащим диапазону [1; 12], должно быть возбуждено исключение ValueError с текстом:
Некорректное время
Класс HourClock должен иметь одно свойство:

hours — свойство, доступное для чтения и записи, возвращающее текущее количество часов.
При изменении свойство должно проверять, что новое значение является целым числом, принадлежащим диапазону [1; 12],
в противном случае должно быть возбуждено исключение ValueError с текстом:
Некорректное время
"""
# endregion

class HourClock:

    def __init__(self, hours):
        self.hours = hours    # здесь self.hours - это свойство, а hours - принимаемый аргумент

    def get_hours(self):
        return self._hours    # self._hours - защищенный атрибут
    
    def set_hours(self, h):
        if isinstance(h, int) and h in range(1, 13):
            self._hours = h
        else:
            raise ValueError('Некорректное время')
        
    hours = property(get_hours, set_hours)
