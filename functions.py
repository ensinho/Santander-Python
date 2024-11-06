# Now lets look at some functions

def greetings():
    print("Woah, hello good sir!")

greetings() # just do what the function does

''' Its possible to add párameters too'''

def greetings(name):
    print("Hello there good person ", {name})

greetings("Enzo") # it will print the greetings to myself! 

''' Functions can too return some values, using return result, for an example'''

#lambda functions
squared = lambda x: x ** 2
print(squared(2)) # it will print the squared of 2 

''' Variables defined in functions, are usable only there, what means, that
it cannot be acessable globally'''

# functions with a variable number of args
def add_numbers(*numbers):
    total = 0
    for number in numbers:
        total +=  number
    return total
''' That means, that i can print and use for instance, add_numbers(1,2,3) or add_numbers(1,2,3,4,5,6,7)'''