with open('pi_digits.txt') as file_object:
	contents = file_object.read()
	print(contents)
	print(contents.rstrip())

##################################################

print("Read line by line\n")

filename = 'pi_digits.txt'

with open(filename) as file_object:
	for line_1 in file_object:
                print(line_1.rstrip())

'''
	for line in file_object:
		print(line)
	print("Strip empty line: ")
'''
