# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

num = int(input('Введите число: '))
list = []

for i in range(num):
	if i == 0:
		list.append(1)
	else:
		list.append(list[i - 1] * (i+1))

print(f'N = {num}, тогда {list}')