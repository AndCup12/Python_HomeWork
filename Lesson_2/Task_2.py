# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных пользователем через пробел позициях.

num = int(input('Введите число: '))
list = []
list_num = -num-1
while list_num < num:
	list_num += 1
	list.append(list_num)
print(list,f' --> {len(list)}')

list_index = input('Введите порядковые номера элементов: ').split(' ')


res = 1
for i in range(len(list_index)):
	res *= list[int(list_index[i])-1]
print(f'Произведение выбранных элементов равен: {res}')