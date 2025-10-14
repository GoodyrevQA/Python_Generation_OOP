"""
Реализуйте класс HtmlTag. При создании экземпляра класс должен принимать два аргумента в следующем порядке:
tag — HTML тег
inline — булево значение, по умолчанию равняется False

Экземпляр класса HtmlTag должен являться реентерабельным контекстным менеджером,
который позволяет генерировать HTML-код с правильными отступами и глубиной вложенности тегов.
Параметр inline должен определять положение тегов и их содержимого.
Если он имеет значение True, теги и содержимое должны располагаться на одной строке, если False — на разных строках.

Класс HtmlTag должен иметь один метод экземпляра:
print() — метод, принимающий в качестве аргумента содержимое тега и выводящий его в рамках этого тега
"""

class HtmlTag:
    level = -1

    def __init__(self, tag, inline=False):
        self.tag = tag
        self.inline = inline
        
    def __enter__(self):
        self.__class__.level += 1
        self.tiger = '  ' * self.__class__.level
        if self.inline is False:
            print(f'{self.tiger}<{self.tag}>')
        else:
            print(f'{self.tiger}<{self.tag}>', end='')
        return self
        
    def __exit__(self, exc_type, exc_value, traceback):
        if self.inline is False:
            print(f'{self.tiger}</{self.tag}>')
        else:
            print(f'</{self.tag}>')
        self.__class__.level -= 1
        
    def print(self, text):
        if self.inline is False:
            print('  ' + self.tiger + text)
        else:
            print(text, end='')
            