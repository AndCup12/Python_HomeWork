# Реализуйте алгоритм перемешивания списка.

import random
list = []

for i in range(5):
	list.append(random.randint(1, 9))
print(list)

def mix_list(x):
	num = 0
	for i in range(len(x)-1):
		num = x[i]
		x[i] = x[len(x)-1]
		x[len(x)-1] = num
	return x

print(mix_list(list))
