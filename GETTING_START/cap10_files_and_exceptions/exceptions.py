#it is an object that makes the program to go on even if something went wrong.
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

#trying except with else block
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    except ValueError:
        break
    else:
        print(answer)

##fiileNOtFound error

filename = 'alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()

except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."

print(msg)

##failing Silently
filename = 'alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()

except FileNotFoundError:
    #here, the codegoes as if nothing happened
    pass

print(msg)