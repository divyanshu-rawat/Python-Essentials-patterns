
# The global variable, __name__, in the module that is the entry point to your program, is '__main__'. Otherwise, it's the name you import 
# the module by.

# So, code under the if block will only run if the module is the entry point to your program.

# One reason for doing this is that sometimes you write a module (a .py file) where it can be executed directly. Alternatively, it can also 
# be imported and used in another module. By doing the main check, you can have that code only execute when you want to run the module as a 
# program and not have it execute when someone just wants to import your module and call your functions themselves.



# file one.py
def func():
    print("func() in one.py")

print("top-level in one.py")

if __name__ == "__main__":
    print("one.py is being run directly")
else:
    print("one.py is being imported into another module")