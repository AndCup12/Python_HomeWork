# Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
# [1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4]

list = [1, 1, 2, 3, 4, 5, 5]
res_list =[]

for i in range(len(list)-1):
	if i == 0:
		if list[0] != list[i+1]:
			res_list.append(list[i])
		else:
			continue
	elif (list[i] != list[i-1]) and (list[i] != list[i+1]):
		res_list.append(list[i])
	else:
		continue

print(res_list)
