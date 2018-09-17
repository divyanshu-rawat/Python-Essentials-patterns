
# try() is used in Error and Exception Handling 
# There are two kinds of errors :

# Syntax Error : Also known as Parsing Errors, most basic. Arise when the Python parser is unable to understand a line of code.
# Exception : Errors which are detected during execution. eg – ZeroDivisionError.

# List of Exception Errors :

# IOError : if file can’t be opened
# KeyboardInterrupt : when an unrequired key is pressed by the user
# ValueError : when built-in function receives a wrong argument
# EOFError : if End-Of-File is hit without reading any data
# ImportError : if it is unable to find the module

# How try() works?

# First try clause is executed i.e. the code between try and except clause.
# If there is no exception, then only try clause will run, except clause is finished.
# If any exception occured, try clause will be skipped and except clause will run.


# Python code to illustrate 
# working of try()  
def divide(x, y): 
    try: 
        # Floor Division : Gives only Fractional Part as Answer 
        result = x // y 
        print("Yeah ! Your answer is :", result) 
    except ZeroDivisionError: 
        print("Sorry ! You are dividing by zero ") 
  
# Look at parameters and note the working of Program 
divide(3, 2) 