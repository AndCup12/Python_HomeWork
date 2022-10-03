import random

count_candy = 2021
player_1 = input('Введите ваше имя: ')
player_2 = "BOT"
count = 0
x = random.randint(1,2)

if x == 1:
	lucky = player_1
	loser = player_2
else:
	lucky = player_2
	loser = player_1
	count = 1 
print(f'{lucky}, твой ход первый!')

while count_candy > 0:
	if count == 0:
		print(f'{player_1} возьми конфеты!')
		step = int(input())
		print(f'{player_1} взял {step} конфет')
		if step > count_candy or step > 28:
			print('За один ход можно взять не больше 28 конфет')
		else:
			count_candy -= step
			print(f'На столе осталось {count_candy} конфет(а)')
			count = 1
	elif count == 1:
		step = random.randint(1,28)
		print(f'{player_2} взял {step} конфет')
		if step > count_candy or step > 28:
			print('За один ход можно взять не больше 28 конфет')
		else:
			count_candy -= step
			print(f'На столе осталось {count_candy} конфет(а)')
			count = 0

if count == 1:
	print(f'Победу одержал {player_1}!')
else:
	print(f'Победу одержал {player_2}!')