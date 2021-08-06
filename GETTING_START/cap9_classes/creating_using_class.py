## Creating a class!
class Dog():
    """A simple attempt to model a dog."""

    #this is a special function that is called right in the time when the instance is created!
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting.")
    
    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!")
    
#It does not work if one parameter is missing!
my_dog = Dog('willie', 6)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

my_dog.sit()
my_dog.roll_over()

##PYTHON 2.7!!
#class ClassName(object):
#   --snip--
