
"""
Реализовать класс Stationery (канцелярская принадлежность).
● определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит
сообщение «Запуск отрисовки»;
● создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
● в каждом классе реализовать переопределение метода draw. Для каждого класса
метод должен выводить уникальное сообщение;
● создать экземпляры классов и проверить, что выведет описанный метод для каждого
экземпляра.
"""

class Stationery:
    def __init__(self, title='пишущий инструмент'):
        self.title = title
    def draw(self):
        print(f'Используй любой {self.title}')
class Pen(Stationery):
    def draw(self):
        print(f'Используем {self.title}')
class Pencil(Stationery):
    def draw(self):
        print(f'Используем {self.title}')
class Marker(Stationery):
    def draw(self):
        print(f'Используем {self.title}')

set = Stationery()
set.draw()
pen = Pen('чёрная ручка')
pen.draw()
pencil = Pencil('красный карандаш')
pencil.draw()
marker = Marker('зелёный маркер')
marker.draw()


