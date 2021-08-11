directory = "C:/Users/jfcjardiel/Desktop/Treinamentos/PYTHON/GETTING_START/cap10_files_and_exceptions/"
filename = 'programming.txt'
file_path = directory+filename

#remember, python can only write strings to a text file
with open(file_path, 'w') as file_object:
    file_object.write("I love my wife.")

##If you want to APPEND data from the file, you should start the file as 'a'
with open(file_path, 'a') as file_object:
    file_object.write("\nMy name is Jardiel.\n")
    file_object.write("And I can write on files.\n")