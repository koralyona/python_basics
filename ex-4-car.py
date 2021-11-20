# author is Alyona Koryagina
# 20-11-2021
# python basics course
# lesson 6, exercise 4
# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police


    def go(self):
        print('Go')

    def stop(self):
        print('Stop')

    def turn(self, direction):
        print(f'Turn {direction}')

    def show_speed(self):
        print(f'Current speed is {self.speed}')

class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Over the speed limit 60!')

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('Over the speed limit 40!')

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


town_car = TownCar(70, 'black', 'town')
sport_car = SportCar(100, 'black', 'sport')
work_car = WorkCar(50, 'black', 'work')
police_car = PoliceCar(90, 'black', 'police')

town_car.show_speed()
print(town_car.is_police)
sport_car.show_speed()
work_car.show_speed()
police_car.show_speed()
print(police_car.is_police)


work_car.go()
work_car.speed = 30
work_car.show_speed()
work_car.turn('Right')
work_car.stop()

