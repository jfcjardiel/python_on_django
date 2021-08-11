##Starting with the class
class Car():
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        ##setting a default value for an attribute:
        ##this value can be modified after!
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    
    ##Modifying default parameter inside the class!
    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        self.odometer_reading = mileage
    
    ##increasing on attribute's value through a Method
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

##Using the class above as a parent to the class below
##The parent must appear first and it should be pass as a parameter!!
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        #super is a special function that helps Python make connections between the parent and child class
        #This line tells python to call the __init__() method from ElectricCar's parent
        #Super comes from SuperClass (parent class).
        super().__init__(make, model, year)
        ##adding some parameters wich car does not have
        self.battery_size = 70
    
    ##adding methods car does not have
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
    
    ##if you need to override method from the parent class, just define the method with the exact name
    ## inside the subclass
    def fill_gas_tank():
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())

##PYTHON 2.7!!!!
#class Car(object):
#   def __init__(self, make, model, year):
#       --snip--
#
# class ElectricCar(Car):
#   def __init__(self, make, model, year):
#   super(ElectricCar, self).__init__(make, model, year)
