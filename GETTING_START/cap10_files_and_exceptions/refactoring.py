##Sometimes it is possible to break a code into a lot of fuunctions
##this is called refactoring
import json

##this functions is responsable to get the username from the specific file
##if there is no file, return None
def get_stored_username():
    """Get stored username if available."""
    directory = "C:/Users/jfcjardiel/Desktop/Treinamentos/PYTHON/GETTING_START/cap10_files_and_exceptions/"
    filename = directory + 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    directory = "C:/Users/jfcjardiel/Desktop/Treinamentos/PYTHON/GETTING_START/cap10_files_and_exceptions/"
    filename = directory + 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    ##if username is not None!
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")

greet_user()