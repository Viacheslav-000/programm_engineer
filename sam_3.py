#1
num = 1
for i in range(2):
    num *= 5
    num += 1
print(num)

#2
mes = 'Hello World'
for let in reversed(mes):
    print(let)

#3
a = int(input())
if 0 <= a <= 10:
    if 0 <= a <= 3:
        print('Число находится в диапозоне 0 - 3 включительно')
    elif 3 <= a < 6:
        print('Число находится в диапозоне 3 - 6 включительно')
    else:
        print('Число находится в диапозоне 6 - 10 включительно')
else:
    print('Число находится в диапозоне 0 - 10 включительно')

#4
a = input('Введите предложение: ')
print(len(a))
print(a.lower())
print(a.count('a'), a.count('e'), a.count('i'), a.count('o'), a.count('u'))
print(a.replace('ugly', 'beauty'))
if a.startswith("The") and a.endswith("end"):
    print("Yes")
else:
    print("No")

#5
memory = 'Hello'
string = 'Hello World'
counter = 0
while counter != 10:
    print(string)
    string, memory = memory, string
    counter += 1
print(string)