##You can have an instance as an attribute to another class!
class Battery():
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=70):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

class ElectricCar():
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        self.make = make
        self.model =  model
        self.year = year
        ##HERE IS THE INSTANCE PASSING AS AN ATTRIBUTE TO ANOTHER CLASS!
        self.battery = Battery()

    def get_descriptive_name(self):
        """Just describing the name"""
        print("This car is " + str(self.make) + " " + self.model + " from " + str(self.year))

my_tesla = ElectricCar('tesla', 'model s', 2016)
my_tesla.get_descriptive_name()
##calling the instance inside the instance!
my_tesla.battery.describe_battery()