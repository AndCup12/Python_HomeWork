# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 10.01] => 0.19

list = [1.1, 1.2, 3.1, 10.01]
new_list = []
for i in range(len(list)):
	rigth = str(list[i]).split('.')
	new_list.append(rigth[1])

res = 0
def result(arr):
	for i in arr:
		res = max(arr[i]) - min(arr[i])


result(int(new_list))
print(res)