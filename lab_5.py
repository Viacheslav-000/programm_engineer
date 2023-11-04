# 1)
# a = {'apple', 'banana', 'kiwi', 'orange','grapefruit'}
# b = {'blueberry', 'kiwi', 'starwberry', 'banana'}
# print(a-b)

# 2)
# a = set('12345')
# print(a)
# for i in range(1, 4):
#     a.add(i)
# print(a)
#
# b = frozenset('12345')
# print(b)
# for z in range(1, 4):
#     b.add(z)
# print(b)

# 3)
# lst = [1, 2, 3, 4, 5]
# first = lst[0]
# lst[0] = lst[-1]
# lst[-1] = first
# print(lst)

# 4)
# lst = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# print(lst[2:6])

# 5)
# def useless(lst):
#     return max(lst) / len(lst)
#
# print(useless([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
# print(useless([25, 355, 48, 862, 653, 6]))
# print(useless([1332, 7962, 566, 233, 426, 486]))

# 6)
#sup = ['Человек-паук', 'Железный человек', 'Капитан Америка']
#Slava, Stepa, Dima = sup
#
#print('Slava - ', Slava)
#print('Stepa - ', Stepa)
#print('Dima - ', Dima)

#7)
# lst = [2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 1]
# lst.sort()
# print(f"Отсортированный список: {lst}")
# lst.pop(0)
# print(f"отсортированный список без наименьшего элемента: {lst}")

#8)
# from random import randint
# def lst():
#     a = [randint(1, 100) * randint(3, 10)]
#     return a
#
#
# if __name__ == '__main__':
#     res = []
#     for i in range(randint(1, 5)):
#         res.append((lst()))
#     print(res)

#9)
# def superset(set_1, set_2):
#     if set_1 > set_2:
#         print(f'Объект {set_1} Является чистым супермножеством')
#     elif set_1 < set_2:
#         print(f'Объект {set_2} Является чистым супермножеством')
#     elif set_1 == set_2:
#         print('Множества равны')
#     else:
#         print("Супермножество НЕ обнаружено")
#
# if __name__ == '__main__':
#     superset({1, 2, 3, 4, 5}, {4, 5})
#     superset({1, 2, 3, 4, 5}, {5, 3, 1, 4, 2})
#     superset({4, 5}, {5, 3, 1, 4, 3})
#     superset({10, 50}, {5, 6})

#10)
# lst = [1, 2, 3, 4, 5]
# print(lst[::-1])

