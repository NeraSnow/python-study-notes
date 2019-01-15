filename = 'pi_digits.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

pi_string = ''
pi_string_tight = ''
for line in lines:
	pi_string += line.rstrip()
	pi_string_tight += line.strip()

print(pi_string)
print(len(pi_string))

print("\n")
print(pi_string_tight)
print(len(pi_string_tight))

