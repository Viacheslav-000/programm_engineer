# 1)
# from functools import lru_cache
#
#
# @lru_cache(None)
# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# if __name__ == '__main__':
#     print(fibonacci(100))

# 2)
# def check(input_func):
#     def output_func(*args):
#         name, age = args[0], args[1]
#         if age < 0 or age > 130:
#             age = 'Недопустимый возраст'
#         input_func(name, age)
#
#     return output_func
#
#
# @check
# def personal_info(name, age):
#     print(f"Name: {name} Age: {age}")
#
#
# if __name__ == '__main__':
#     personal_info("Вячеслав", 20)
#     personal_info("Стёпа", -15)
#     personal_info("Дима", 151, 50, 1)

# 3)
# def data(*args):
#     try:
#         for i in range(len(*args)):
#             try:
#                 res = (args[0][i] * 15) // 10
#                 print(res)
#
#             except Exception as ex:
#                 print(ex)
#
#     except Exception as ex:
#         print(ex)
#     finally:
#         print('Вся информация обработана')
#
#
# if __name__ =='__main__':
#     data([1, 10, 'h', 'i', 'try', 20, 30])

# 4)
# class Ex(Exception):
#     pass
#
#
# def check(name, name2):
#
#     if len(name) > 20 or len(name2) > 20:
#         raise Ex('Длина более 20 символов')
#     else:
#         print('Успешня регистраця')
#
#
# if __name__ == '__main__':
#     name = 'Вячеслав'
#     name2 = 'Перевозчиков'
#     check(name,name2)

# 5)
# class Checker:
#     def __init__(self, func):
#         print('> Класс Checker метод __init__ успешный запуск')
#         self.func = func
#
#     def __call__(self):
#         print('> Проверка перед запуском', self.func.__name__)
#         self.func()
#         print('> Проверка безопасности выключена')
#
#
# @Checker
# def site():
#     print('Усердная работа сайта')
#
#
# if __name__ == '__main__':
#     print('>> Сайт запущен')
#     site()
#     print('>> Сайт выключен')


