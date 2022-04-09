# Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
class Stationery():
    def __init__(self, title):
        self.title = title
    def draw(self):
        return(f'Запуск отрисовки {self.title}')

class Pen(Stationery):
    def draw(self):
        return(f'Пишет ручка {self.title}')

class Pensil(Stationery):
    def draw(self):
        return(f'Пишет карандаш {self.title}')

class Handle(Stationery):
    def draw(self):
        return(f'Пишет маркер {self.title}')

a = Stationery('Book')
b = Pensil('Серый')
c = Pen('Синяя')
d = Handle('Красный')

stationery = [a, b, c, d]
for i in stationery:
    print(f'{i.draw()}')

