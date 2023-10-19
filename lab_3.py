#1
one = int(input('Введите значение первой переменной: '))
two = int(input('Введите значение второй переменной: '))
if one >= two:
    print('Выполняется')
else:
    print('Не выполняется')

#2
one = int(input("Введите значение первой переменной: "))
if one < 0:
    print("Переменная меньше 0")
elif 0 < one <10:
    print("Переменная больше 0 и меньше 10")
else:
    print("Переменная больше 10")


#3
numbers = [1, 2, 3, 4, 5]
value = int(input("Введите значение переменной: "))
if value in numbers:
    print("Переменная есть в данном массиве")
else:
    print("Переменной нет в данном массиве")


#4
numbers = [11, 24, 37, 48, 61]
value = int(input("Введите значение переменной: "))
if value in numbers:
    if value % 2 == 0:
        print("Переменная четная и есть в массиве")
    else:
        print("Переменная нечетная и есть в массиве")
else:
    print(f'Переменной нет в массиве и она равная {value}')

#5
for i in range(10):
    print('i = ', i)
    if i == 0:
        i += 2
    if i == 1:
        continue
    if i == 2 or i == 3:
        print('Переменная равна 2 или 3')
    elif i in [4, 5, 6]:
        print('Переменная равна 4, 5, 6')
    else:
        break

#6
str = 'Hello World!'
value = input()
for i in str:
    if i == value:
        index = str.find(value)
        print(f'Буква "{value}" есть в строке под {index} индексом')
        break
else:
    print(f"Буквы '{value}' нет в указанной строке")

#7
value = 4
for i in range(20, -10, -1):
    value *= i
    print(i, value)

#8
value = 0
while value < 10000:
    if value == 0:
        value += 100
    elif value // 2 > 1:
        value += 1000
    else:
        value -= 1
    print(value)

#9
value = 0
for i in range(1000):
    for r in range(1000):
        if i != r:
            value += r
        else:
            pass
print(value)

#10
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
flag = False
for value in numbers:
    if value % 2 == 0:
        flag = True
if flag:
    print('В массиве есть число, которое делится на 2')
else:
    print('В массиве нет числа, которое делится на 2')