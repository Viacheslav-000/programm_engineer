
# class Car:  # Создадим класс с названием "Car"
#     def __init__(self, make, model):  # Проведем инициализацию объекта класса, self - ссылка на объект
#         self.make = make  # Присваиваем значение атрибута "make"
#         self.model = model  # Присваиваем значение атрибута "model"
#
#     def drive(self):
#         print(
#             f"Driving the {self.make} {self.model}")  # Метод класса, выводящий сообщение о вождении машины с атрибутами "make" и "model"
#
# my_car = Car("BMW", "525I")
# my_car.drive()


# class ElectricCar(Car):  # создание класса ElectricCar, который наследует атрибуты и методы класса Car
#     def __init__(self, make, model, battery_capacity):
#         super().__init__(make, model) # вызываем метода родительского класса Car для установки атрибутов make и model.
#         self.battery_capacity = battery_capacity # устанавливаем значение атрибута battery_capacity
#
#     def charge(self):
#         print(f'Charging the {self.make} {self.model} with {self.battery_capacity} kWh')
### Метод класса "ElectricCar", выводящий сообщение о зарядке автомобиля с атрибутами "make", "model" и "battery_capacity"
#
# my_electric_car = ElectricCar("Tesla", "Model X", 50)
# my_electric_car.drive()
# my_electric_car.charge()

# 4)
#class Car:  # Создаем класс "Car"
#     def __init__(self, make, model):  # Проводим инициализацию объекта данного класса, "self" - ссылка на текущий объект
#         self.make = make  # Присваиваем значение атрибута "make"
#         self.model = model  # Присваиваем значение атрибута "model"
#
#     def drive(self):
#             print(f"Driving the {self.make} {self.model}")  # Метод класса "Car", выводимый сообщение о вождении машины с атрибутами "make" и "model"
#
# my_car = Car("BMW", "525I")
# print(my_car.make) # Доступ к защищенному атрибуту
# my_car.drive()

# 5)
# class Shape:
#     def area(self):
#         pass
#
#
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return 3.14 * self.radius * self.radius
#
#
# rec = Rectangle(45, 60)
# cir = Circle(5)
#
# print(rec.area())
# print(cir.area())