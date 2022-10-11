import create_file
import interface


def start():
	format = interface.get_format()
	if (format == '.txt') or (format == '1'):
		create_file.create_txt()
	elif (format == '.csv') or (format == '2'):
		create_file.create_csv()
	else:
		create_file.create_csv()
		create_file.create_txt()
