

# Python decorator is a function that helps to add some additional functionalities to an already defined function. 
# Python decorator is very helpful to add functionality to a function that is implemented before without making any 
# change to the original function. Decorator is very efficient when want to give an updated code to an existing code.

# ref- https://hackernoon.com/decorators-in-python-8fd0dce93c08
#python decorator is nothing but a decorator that decorates a function.

# example of decorator

# In python everything is object, In Python, everything is object. Functions in Python are first-class objects which 
# means that they can be referenced by a variable, added in the lists, passed as arguments to another function etc.


# Functions can be referred by variables

def say_hello(): 
  print("Hello")
  
say_hello_again = say_hello
#Output: Hello
# say_hello_again()

# Functions can be passed as arguments to another function


# def say_hey(function):
# 	print("Hey")
# 	function()

# def say_bye():
# 	print("bye")


# say_hey(say_bye)


# Functions can be defined inside another function

# def say_hey():
# 	print("Hey")
	
# 	def say_bye():
# 		print("bye")

# 	say_bye()

# say_hey()



# Functions can return references to another function

# def say_hey(argument):
# 	print("Hey")
	
# 	def say_bye():
# 		print("bye " + argument )

# 	return say_bye


# say_bye = say_hey('Divyanshu')
# say_bye()



# Decorators are callable objects which are used to modify functions or classes.



# def decorator_func(some_func):
#   # define another wrapper function which modifies some_func
#   def wrapper_func():
#     print("Wrapper function started")
    
#     some_func()
    
#     print("Wrapper function ended")
    
#   return wrapper_func # Wrapper function add something to the passed function and decorator returns the wrapper function
    
# def say_hello():
#   print ("Hello")
  
# say_hello = decorator_func(say_hello)

# say_hello()

# Output:
#  Wrapper function started
#  Hello
#  Wrapper function started



# def say_hey(fn):
# 	def print_hey():
# 		print 'hey'
# 		fn()
# 	return print_hey

# def say_bye():
# 	print 'bye'


# say_bye = say_hey(say_bye);

def decorator_func(fun):
	def wrapper_func():
		print("Wrapper function started")
		fun()
		print("Given function decorated")
		# Wrapper function add something to the passed function and decorator 
        # returns the wrapper function
	return wrapper_func

@decorator_func
def say_bye():
	print("bye!!")

say_bye()



# say_bye()

# This is a common construct and for this reason, Python has a syntax to simplify this.


def decorate_me(func):
    def inner():
        print("I got decorated")
        func()
    return inner

@decorate_me
def ordinary():
    print("I am ordinary")

# ordinary = decorate_me(ordinary)

# ordinary()


def let_divide(func):
	def divide_number(x,y):
		print("Divide Number's")

		if(y == 0):
			print('Not Possible')

		return func(x,y)
	return divide_number

@let_divide
def call(x,y):
	return x/y

print call(8,4)


