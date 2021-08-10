#reading entire content of a file

#using with because it deals with the file properly
#with open('pi_digits.txt') as file_object:
#    contents = file_object.read()
#    print(contents)

#making a list with lines
filename="C:/Users/jfcjardiel/Desktop/Treinamentos/PYTHON/GETTING_START/cap10_files_and_exceptions/pi_digits.txt"
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))

