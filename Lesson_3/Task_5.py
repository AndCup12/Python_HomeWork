# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
list_fibbonaci = []
x = int(input('Введите число: '))
res_list_fibbonaci = [0]
def fibbonaci(x):
	if x in (1, 2):
		return 1
	return fibbonaci(x - 1) + fibbonaci(x - 2)

for i in range(x + 1):
	if i == 0:
		list_elem = 0
	else:
		list_elem = fibbonaci(i)
		list_fibbonaci.append(list_elem)
		res_list_fibbonaci.append(list_elem)



for i in range(len(list_fibbonaci)):
	if i % 2 != 0:
		res_list_fibbonaci.insert(0, int(list_fibbonaci[i])* (-1))
	else:
		res_list_fibbonaci.insert(0,list_fibbonaci[i])

print(res_list_fibbonaci) 