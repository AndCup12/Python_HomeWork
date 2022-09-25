# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
import random
import re

k = int(input('Введите степень k: '))

def rnd():
	return random.randint(0, 21)

result_polindorm_1 = (f'{str(rnd())}x^{k} + {str(rnd())}x + {str(rnd())}')
result_polindorm_2 = (f'{str(rnd())}x^{k} + {str(rnd())}x + {str(rnd())}')
# print(result_polindorm_1, result_polindorm_2)
file_1 = open('polinormal_1.txt', 'w')
file_1.write(result_polindorm_1)
file_1.close()
file_2 = open('polinormal_2.txt', 'w')
file_2.write(result_polindorm_2)
file_2.close()

with open('polinormal_1.txt') as file:
	polinormal_1 = file.read()
print(polinormal_1)


with open('polinormal_2.txt') as file:
	polinormal_2 = file.read()
print(polinormal_2)

