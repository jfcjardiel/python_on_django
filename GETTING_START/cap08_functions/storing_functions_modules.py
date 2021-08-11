################## USING IMPORT 

#we are going to import make_pizza function from arbitrary_no_parameters.py
import arbitrary_no_parameters

arbitrary_no_parameters.make_pizza(16, "peperoni")
arbitrary_no_parameters.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

##Import specific functions
from arbitrary_no_parameters import make_pizza
make_pizza(16, "peperoni")
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

## You can use * to import all functions from the file
from arbitrary_no_parameters import *

################# USING AS

##Using AS to give a function an Alias
from arbitrary_no_parameters import make_pizza as pizza
pizza(16, "peperoni")
pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

##Using AS to give a module an Alias
import arbitrary_no_parameters as mp

mp.make_pizza(16, "peperoni")
mp.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

