file = open('RLE_data.txt')
content_file = file.read()
file.close()

list_content_file = list(content_file)
print(list_content_file)

def get_char(arr):
	res = []
	for i in range(len(arr)):
		if '0' < arr[i] < '9':
			continue
		else:
			res.append(arr[i])
	return res

def get_index(arr):
	res = []
	for i in range(len(arr)-2):
		if '0' < arr[i] < '9':
			if '0' < arr[i+1] < '9':
				res_char = (arr[i])+(arr[i+1])
				res.append(int(res_char))
			else:
				res.append(int(arr[i]))
	return res

def get_result_list(arr_char, arr_num):
	res = []
	for i in range(len(arr_char)):
		res.append(arr_char[i] * arr_num[i])
	return res

def get_result_string(arr):
	res =''
	for i in range(len(arr)):
		res += arr[i]
	return res

result_char_list = get_char(list_content_file)
print(result_char_list)
result_num_list = get_index(list_content_file)
print(result_num_list)
result_list = get_result_list(result_char_list, result_num_list)
print(result_list)
result_string = get_result_string(result_list)
print(result_string)


