

# Stackoverflow:
# Reference - https://stackoverflow.com/questions/448271/what-is-init-py-for

# Files named __init__.py are used to mark directories on disk as Python package directories. If you have the files

# mydir/spam/__init__.py
# mydir/spam/module.py
# and mydir is on your path,

# you can import the code in module.py as import spam.module 
# or
# from spam import module

# If you remove the __init__.py file, Python will no longer look for submodules inside that directory, so attempts to import the module will fail.

# The __init__.py file is usually empty, but can be used to export selected portions of the package under more convenient name,
# hold convenience functions, etc. Given the example above, the contents of the init module can be accessed as

# import spam

# For convenience: the other users will not need to know your functions' exact location in your package hierarchy.

# Example :

# your_package/
#   __init__.py
#   file1.py/
#   file2.py/
#     ...
#   fileN.py

# in __init__.py

# from file1 import *
# from file2 import *
# ...
# from fileN import *

# in file1.py
# def add():
#     pass


# from your_package import add
# without knowing file1, 
# instead of doing this -> from your_package.file1 import add
