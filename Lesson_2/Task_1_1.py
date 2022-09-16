# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 0,56 -> 11

num = input('Введите число: ')

list = num.split('.')
sum = 0

list_num = list[1]
number = [int(i) for i in list_num]
sum = 0
for i in range(len(number)):
	sum += number[i]

print(f'{num} --> {sum}')
