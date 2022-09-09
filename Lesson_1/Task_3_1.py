quater = int(input('Введите номер четверти: '))

if(quater == 1):
	print('x >= 0, y >= 0')
elif(quater == 2):
	print('x <= 0, y >= 0')
elif(quater == 3):
	print('x <= 0, y <= 0')
else:
	print('x >= 0, y <= 0')