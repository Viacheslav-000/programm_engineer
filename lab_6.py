# 1)
req = int(input('Введите номер кабинета: '))

dic = {
    100: {'key': 111, 'access': True},
    205: {'key': 252, 'access': True},
    310: {'key': 552, 'access': True},
    415: {'key': 706, 'access': False},
    None: {'key': None, 'access': False}
}

res = dic.get(req)
if not res:
   res = dic[None]
key = res.get('key')
access = res.get('access')

print(key, access)

# 2)
from pprint import pprint
dic = {'first': 'so easy'}

def dict_maker(**kwargs):
    dic.update(**kwargs)

dict_maker(a1=10, a2=20, a3=30, a4=40)
dict_maker(name='Viacheslav', age=20, weight=60, eyes_color='brown')
pprint(dic)

# 3)
inp = 'hello,friend!'
res = tuple(inp)
print(res, list(res), sep='\n')

# 4)
def info(name, age, company='unnamed'):
    print(f'Имя: {name}, Возраст: {age}, Компания: {company}')

tom = ('Viacheslav', 20, 'Not have')
info(*tom)
bob = ("Olga", 35, "Tinkoff")
info(*bob)

# 5)
def tup(tpl):
    for el in tpl:
        if not isinstance(el,int):
            return tpl
    return tuple(sorted(tpl))

if __name__ =='__main__':
    print(tup((1, 3, 5, 2, 4)))
    print(tup((4, 2, 2, '3', 1)))
