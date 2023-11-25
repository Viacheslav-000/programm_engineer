# class Animals:
#     def __init__(self, name, nickname):
#         self.name = name
#         self.nickname = nickname
#
#     def pet(self):
#         print(f"It is {self.name}, it's nickname is {self.nickname}")
#
# animals = Animals('Snail', 'Shura')
# print(animals.name)
# animals.pet()
#
# class WildAnimals(Animals):
#     def __init__(self, name, nickname, zoo_location):
#         super().__init__(name, nickname)
#         self.zoo_location = zoo_location
#
#     def wild(self):
#         print(f"It is a {self.name}, it's name is {self.nickname}. {self.nickname} is located in the {self.zoo_location}")
#
# wild_animal = WildAnimals("Giraffe", "Yankee", "Ekaterinburg")
# wild_animal.wild()

# 5)
# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         pass
#
# class Wolf(Animal):
#     def speak(self):
#         return "Awww Awww Awww"
#
# class Monkey(Animal):
#     def speak(self):
#         return "Wa Wa Wa"
#
# def animal_speak(animal):
#     print(animal.speak())
#
# Wolf = Wolf("Woolen")
# Monkey = Monkey("Shaggy")
#
# animal_speak(Wolf)
# animal_speak(Monkey)