
class A(object):
    def __init__(self):
        self.x = 'Hello'

    def method_a(self, foo):
        print self.x + ' ' + foo


instance = A()               # We do not pass any argument to the __init__ method
instance.method_a('Sailor!') # We only pass a single argument

 # ... the self variable represents the instance of the object itself.
 # Most object-oriented languages pass this as a hidden parameter to the methods defined on an object; Python does not. You have to declare it explicitly.
 # When you create an instance of the A class and call its methods, it will be passed automatically, as in ...


 # The __init__ method is roughly what represents a constructor in Python.
 # When you call A() Python creates an object for you, and passes it as the first parameter to the __init__ method.
 # Any additional parameters (e.g., A(24, 'Hello')) will also get passed as arguments--in this case causing an exception to be raised, since the constructor isn't expecting them.

 # It is important to use the self parameter inside an object's method if you want to persist the value with the object.
