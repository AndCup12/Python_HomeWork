from interface import set_info as si

info = si()

def create_csv():
	file = r'HomeWork\Lesson_7\Phone_book\phonebook.csv'
	with open (file, 'a+', encoding= 'utf-8') as data_file:
		data_file.write(f'{info[0]};{info[1]};{info[2]};{info[3]}\n') 


def create_txt():
	file = r'HomeWork\Lesson_7\Phone_book\phonebook.txt'
	with open (file, 'a+', encoding = 'utf-8') as data_file:
		data_file.write(f'{info[0]}\n\n{info[1]}\n\n{info[2]}\n\n{info[3]}\n\n')



