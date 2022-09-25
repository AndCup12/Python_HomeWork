# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

k = int(input('Введите степень k: '))

def rnd():
	return random.randint(0, 101)

result_string = (f'{str(rnd())}x^{k} + {str(rnd())}x + {str(rnd())} or x^{k} + {str(rnd())} = 0 or {str(rnd())}x^{k} = 0')

file = open('result_task_4.txt', 'w')
file.write(result_string)
file.close()

