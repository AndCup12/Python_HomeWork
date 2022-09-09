import math


list = []


for i in range(4):
	value = int(input('Введите значения координат: '))
	list.append(value)
print(list)

distance = math.sqrt(((list[2] - list[0]) ** 2) + (list[3] - list[1]) ** 2)
print(round(distance, 2))