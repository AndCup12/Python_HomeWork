# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# "20" -> [2, 2, 5]

num = int(input('Введите число: '))
decomposition_list = []

def decomposition_num(x, arr):
	count = 2
	while x >= count:
		if x % count == 0:
			arr.append(count)
			x = x // count
			count = 2
		else:
			count += 1
			if x // count == 0:
				arr.append(count)	
	return arr	
res = decomposition_num(num, decomposition_list)

print(f'{num} --> {res}')

