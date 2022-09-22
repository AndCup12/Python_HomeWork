# Напишите программу, которая будет преобразовывать десятичное число в двоичное 
# (без встроенных функций).
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

binary_num = []
x = int(input('Введите число: '))

while x >= 2:
	binary_num.insert(0, (int(x % 2)))
	x = x / 2
else:
	binary_num.insert(0, (int(x)))

print(binary_num)
