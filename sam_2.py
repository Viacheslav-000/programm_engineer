# 1)
a = 7
print(a == 2)

# 2)
a, b, c = 7, 12, 9
print(a, b, c)

# 3)
a = int(input("Введите число: "))
print(a)

# 4)
a = 'ABCD'
print(a * 5)

#5)
day, month, year = 10, 'Октября', 2023
print(f'Сегодня {day} {month} {year} -',end=' Всего хорошего!')

#6)
a, b = 'Hello', 'World!'
print(a, b, sep=' my ')

#7)
sen = 'Hello World'
print(len(sen))

#8)
sen = 'HELLO WORLD'
print(sen.lower())

#9)
a, b = int(input("Введите значение: ")), int(input("Введите значение: "))
print(f'Умножение переменных={a * b}\nВозведение в степень={a ** b}\nНахождение остатка от деления={a % b}')

#10)
a, b, c, d = 'приходи ', 'УЧИТЬСЯ ', 'в ', 'ургэу!'
print(a.title() + b.lower() + c + d.upper())