##simplest way a list can be passed as an argument
def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)
    
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)