

from random import randint

a = randint(1, 10)
b = randint(1, 15)

c = int(input('{} * {} = '.format(a, b)))

if c == (a * b):
	print('To`g`ri')
else:
	print('Xato!')

# year = int(input('Kabisa yili: '))

# if year % 400 == 0:
#     print("this is kabisa 400")
# elif year % 100 == 0:
#     print("this is  not a kabisa 100")
# elif year % 4 == 0:
#     print("this is kabisa 4")
# else:
#     print("Kabisa yili emas")
