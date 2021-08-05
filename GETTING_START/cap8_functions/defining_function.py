def greet_user():
    """Display a simple greeting."""
    print("Hello!")

greet_user()

#passing information to a function
def greet_user(username):
    """Display a simple greeting."""
    print("Hello, " + username.title() + "!")
greet_user('jesse')

#keyword argument
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

#sem o keyargument, ordem importa
describe_pet('hamster','harry')
describe_pet(pet_name="harry", animal_type="hamster")

#default values
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(pet_name='willie')
describe_pet('willie')
describe_pet(pet_name="willie", animal_type="cat")

##NOTA: Quando se usa default values, colocar parâmetros default no final!!!!
