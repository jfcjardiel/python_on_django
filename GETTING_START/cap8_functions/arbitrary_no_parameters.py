## THE (*) TELLS PYTHON TO MAKE AN EMPTY TUPLE AND PACK WHATEVER VALUES IT RECEIVES INTO THIS TUPLE
def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

##MIXING POSITIONAL AND ARBITRARY ARGUMENTS
