# Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и
# 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.
from random import choice
class Car():

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print(f'Новая машина: {color} {name}, едет со скоростью: {speed}, полицейская - {is_police}')

    def go(self):
        print (f'Машина {self.name} поехала')

    def stop(self):
        print (f'Машина {self.name} остановилась')

    def turn(self):
        direction = ['на север', 'на юг', 'на запад', 'на восток', 'на северо-запад', 'на северо-восток', 'на юго-запад',
                     'на юго-восток']
        print(f'Машина {self.name} едет {choice(direction)}')

    def show_speed(self):
        print(f'Ваша скорость: {self.speed}')

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Вы превысили скорость 60км/час')
        else:
            print(f'Ваша скорость: {self.speed} км/час')

class SportCar(Car):
    def get_info(self):
        print('Это спортивная машина')


class WorkCar(Car):

    def get_info(self):
        print('Это рабочая машина')


    def show_speed(self):
        if self.speed > 40:
            print('Вы превысили скорость 40км/час')
        else:
            print(f'Ваша скорость: {self.speed} км/час')


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=True)

    def get_info(self):
        print('Это рабочая машина')

workcar = WorkCar(50,'red', 'Toyota Camry')
policecar = PoliceCar(60,'black', 'Mercedez')
towncar = TownCar(70, 'white', 'Honda')
sportcar = SportCar(100, 'yellow', 'BMW')

cars = [workcar, policecar, towncar, sportcar]

for car in cars:
    car.go()
    car.show_speed()
    car.turn()
    car.stop()
    print()


