# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

file = open('data.txt')
content_file = file.read()
file.close()

list_content_file = list(content_file)
print(list_content_file)

def rle_algoritm(arr, res_arr):
	count = 1
	char = arr[0]
	for i in range(1, len(arr)):
		if arr[i] == char:
			count += 1
		else:
			res_arr.append(count)
			res_arr.append(char)
			char = arr[i]
			count = 1
	res_arr.append(count)
	res_arr.append(char)
	return res_arr

def remove_number_one(arr):
	result = ''
	for i in range(len(arr)):
		if arr[i] != 1:
			result += str(arr[i])
	return result


list = []
rle_algoritm(list_content_file, list)
result_rle = remove_number_one(list)
print(result_rle)
file = open('RLE_data.txt', 'a') 
file.write('')
file.write(result_rle)
file.close()
