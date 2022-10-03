# Создайте программу для игры в ""Крестики-нолики"".

field = list(range(1,10))
wins_comb = [(1,2,3), (4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]
def draw_board(field):
	print('-' * 12)
	for i in range(3):
		print('|', field[0 + i * 3],'|', field[1 + i * 3],'|', field[2 + i * 3],'|')
		print('-' * 12)

def check_input(token_player):
	while True:
		value = input(f'куда поставить {token_player}?')
		if not (value in '123456789'):
			print('ошибка. Введите значение от 1 до 9')
			continue
		value = int(value)
		if str(field[value - 1]) in 'XO':
			print('Эта ячейка уже занята')
			continue
		else:
			field[value - 1] = token_player
			break
			
def check_win():
	for each in wins_comb:
		if (field[each[0]-1]) == (field[each[1]-1]) == (field[each[2]-1]):
			return field[each[1]-1]
	else:
		return False

def Main():
	count = 0
	while True:
		draw_board(field)
		if count % 2 == 0:
			check_input('X')
		else:
			check_input('O')
		if count > 3:
			winner = check_win()
			if winner:
				draw_board(field)
				print(f'{winner} выйграл!')
				break
		count += 1

		if count > 8:
			draw_board(field)
			print('Ничья!')
			break

Main()