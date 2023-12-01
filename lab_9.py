# 1)
# class Slava:
#     __slots__ = ['name']
#
#     def __init__(self, name):
#         if name == 'Слава':
#             self.name = f'Да, я {name}'
#         else:
#             self.name = f'Я не {name}, а Слава'
#
# per1 = Slava('Стёпа')
# per2 = Slava('Слава')
# print(per1.name)
# print(per2.name)
#
# per2.surname = 'Перевозчиков'

# 2)
# class Icecream:
#     def __init__(self, ingredient=None):
#         if isinstance(ingredient, str):
#             self.ingredient = ingredient
#         else:
#             self.ingredient = None
#
#     def composition(self):
#         if self.ingredient:
#             print(f'Мороженое с {self.ingredient}')
#         else:
#             print('Мороженое обычное')
#
# icecream = Icecream()
# icecream.composition()
# icecream = Icecream('Карамелью')
# icecream.composition()

# 3)
# class MyClass:
#     def __init__(self, value):
#         self._value = value
#
#     def set_value(self, value):
#         self._value = value
#
#     def get_value(self):
#         return self._value
#
#     def del_value(self):
#         del self._value
#
#     value = property(get_value, set_value, del_value,'Свойство value')
#
# obj = MyClass(50)
# print(obj.get_value())
# obj.set_value(60)
# print(obj.get_value())
# obj.set_value(90)
# print(obj.get_value())
# obj.del_value()
# print(obj.get_value())

# 4)
# class Mammal:
#     className = 'Mammal'
#
# class Dog(Mammal):
#    species = 'Canine'
#    sounds = 'Wow-wow...'
#
# class Cat(Mammal):
#     species = 'Feline'
#     sounds = 'Miay...'
#
# dog = Dog()
# print(f'Dog is "{dog.className}" and they say "{dog.sounds}"')
# cat = Cat()
# print(f'Cat is "{cat.className}" and they say "{cat.sounds}"')

# 5)
# class Russian:
#     @staticmethod
#     def greeting():
#         print('Добрый день!')
#
# class English:
#     @staticmethod
#     def greeting():
#         print('Good day!')
#
# def greet(language):
#     language.greeting()
#
# Слава = Russian()
# greet(Слава)
# Slava = English()
# greet(Slava)