# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

list = [2, 3, 5, 6]
res_list = []
res = 1
length = len(list)
if (length % 2 != 0):
	for i in range(int(len(list)/2)+1):
		res = list[i] * list[(len(list)-1)- i]
		res_list.append(res)
else:
	for i in range(int(len(list)/2)):
		res = list[i] * list[(len(list)-1)-i]
		res_list.append(res)

print(res_list)