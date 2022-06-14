# summa = input('Summani kiriting: ')

# if summa.isdigit() and int(summa) > 0 and int(summa) < 10000000:
# 	print('Tashakkur )') 
# else:
# 	print('Xatolik bor!')

# ism = input('Ismingizni kiriting: ')
# fam = input('Familiyangizni kiriting: ')

# if ism or fam:
# 	print('Tashakkur :)')
# else:
# 	print('Ism yoki Familiyangizni kiriting!')


son = input('1 dan 10 gacha son kiriting: ')
if son.isdigit():
	son = int(son)
	if son > 0 and son < 30:
		qoldiq = son % 10 
		letter = ''
		if qoldiq == 1:
			letter += 'bir'
		elif qoldiq == 2:
			letter += 'ikki'
	    elif qoldiq == 3:
	    	letter += 'uch'
	    elif qoldiq == 4:
	    	letter += 'to`rt'
	    elif qoldiq == 5:
	    	letter += 'besh'
	    elif qoldiq == 6:
	    	letter += 'olti'

print(letter)
else:
	print('1 dan 10 gacha sondan birini kiriting!')
else:
	print('Son kiritish kerak!')


