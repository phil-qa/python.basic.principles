'''
This is a functions cheat sheet
add things to it
'''

# how is a function constructed
def a_function():
    print('A function is created using the def keyword')

#a function is called by its name
a_function()

# a function takes arguments
def a_function(an_argument):
    print(f'\nthis function has an argument\nThe argument passed was {an_argument}')

a_function("'this was the thing that is passed'")

#functions can take more than one argument
def a_function(argument1, argument2):
    print(f"\nThis function has more that one argument \nThe function will do something with both\n the first arg"
          f" was '{argument1}' and the second was '{argument2}' using the + operator makes '{argument1 + argument2}'")

a_function("one thing","another thing")

#unctions can be called with the arguments named, this means you can call the function with arguents out of orfder
def a_function(argument_one, argument_two, argument_three):
    print(f"argument 1 is {argument_one}, argument two is {argument_two} argument three is {argument_three}")

#calling a_function without naned arguments
print("\nCalling the function with the arguments just in positions, can cause confusion :")
a_function('three', 'one', 2)
print("but using named arguments can help: ")
a_function(argument_three="three", argument_one="one", argument_two= 2)

#a function can return something
def a_function(thing, another_thing):
    return (thing + another_thing)

print (f"\nFunctions can return the result of an action\nJust be sure that you know what is being passed 3 + 4 = {a_function(3,4)}\n"
       f"'3'+'4' = {a_function('3','4')}")

#a function can have a parameter that is also a function
def small_function(arg1, arg2):
    return arg1+arg2

def a_function(thing_to_print):
    return (thing_to_print)

print(f"\nIN this example I am passing the result of one function as an argument to another function {a_function(small_function('this ','thing'))}")

