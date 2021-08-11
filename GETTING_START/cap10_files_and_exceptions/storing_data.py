#using json
import json

directory = "C:/Users/jfcjardiel/Desktop/Treinamentos/PYTHON/GETTING_START/cap10_files_and_exceptions/"
numbers = [2, 3, 5, 7, 11, 13]
filename = directory + 'numbers.json'

##writing the data into the file
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)

#reading the data from the file
with open(filename) as f_obj:
    numbers = json.load(f_obj)
print(numbers)

##Creating a file that remember information
username = input("What is your name? ")
filename = directory + 'username.json'
with open(filename, 'w') as f_obj:
    json.dump(username, f_obj)
print("We'll remember you when you come back, " + username + "!")

##And now remembering the names
filename = directory + 'username.json'
with open(filename) as f_obj:
    username = json.load(f_obj)

print("Welcome back, " + username + "!")

##Putting everuthing together goes into:

# Load the username, if it has been stored previously.
# Otherwise, prompt for the username and store it.
filename = directory + 'username.json'
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    print("We'll remember you when you come back, " + username + "!")
else:
    print("Welcome back, " + username + "!")
