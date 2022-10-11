def set_info():
	list_info = []
	surname = input('Введите фамилию: ')
	list_info.append(surname)
	name = input('Введите имя: ')
	list_info.append(name)
	tel = int(input('Введите телефон: '))
	list_info.append(tel)
	info = input('Введите описание: ')
	list_info.append(info)
	return list_info

def get_format():
	print('В каком расширении записать данные - .txt(1), .csv(2) или в двух сразу(3)? ')
	res = input('')
	return res