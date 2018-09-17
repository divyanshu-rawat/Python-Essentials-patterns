

# Though classmethod and staticmethod are quite similar, there's a slight difference in usage for both entities: 
# "classmethod must have a reference to a class object as the first parameter"


# whereas staticmethod can have no parameters at all.


class Date(object):

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

# let's look more carefully at the above implementation, and review what advantages we have here:
# We've implemented date string parsing in one place and it's reusable now.
# Encapsulation works fine here (if you think that you could implement string parsing as a single function elsewhere, this solution fits 
# the OOP paradigm far better).
# cls is an object that holds the class itself, not an instance of the class. It's pretty cool because if we inherit our Date class, all 
# children will have from_string defined also.

    @classmethod
    def from_string(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        date1 = cls(day, month, year) #cls is an object that holds the class itself,
        return date1

    @staticmethod
    def is_date_valid(date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        return day <= 31 and month <= 12 and year <= 3999 #This task is also logically bound to the Date class we've used so far, but doesn't require instantiation of it.


# print Date.from_string('11-09-2012').is_date_valid('11-09-2012')
# print Date.is_date_valid('11-09-2012')

# So, as we can see from usage of staticmethod, we don't have any access to what the class is---it's basically just a function, called 
# syntactically like a method.
# but without access to the object and its internals (fields and another methods), while classmethod does.

# class_instance = Date()
# print class_instance.day




 # I thought I could highlight one other reason you should choose @classmethod over @staticmethod when you are creating additional 
 # constructor.


 # In the example above, we have used the @classmethod from_string as a Factory to create Date objects from otherwise unacceptable 
 # parameters. The same can be done with @staticmethod as is shown in the code below


 # @staticmethod means: when this method is called, we don't pass an instance of the class to it (as we normally do with methods). This 
 # means you can put a function inside a class but you can't access the instance of that class (this is useful when your method does not 
 # use the instance).


# @classmethod means: when this method is called, we pass the class as the first argument instead of the instance of that class (as we n
# normally do with methods). This means you can use the class and its properties inside that method rather than a particular instance.



# Conclusion :: @staticmethod function is nothing more than a function defined inside a class.


# USE CASE 2:


class Date(object): # superclass
  def __init__(self, month, day, year):
    self.month = month
    self.day   = day
    self.year  = year


  def display(self):
    return "{0}-{1}-{2}".format(self.month, self.day, self.year)


  @staticmethod
  def millenium(month, day):
    return Date(month, day, 2000)

  # @classmethod
  # def millenium(cls,month, day):
  #   return cls(month, day, 2000) Got it ;) 

new_year = Date(1, 1, 2013)               # Creates a new Date object
millenium_new_year = Date.millenium(1, 1) # also creates a Date object. 

# Proof:
new_year.display()           # "1-1-2013"
millenium_new_year.display() # "1-1-2000"

isinstance(new_year, Date) # True
isinstance(millenium_new_year, Date) # True


class DateTime(Date): # subclass
  def display(self):
      return "{0}-{1}-{2} - 00:00:00PM".format(self.month, self.day, self.year)


datetime1 = DateTime(10, 10, 1990)
datetime2 = DateTime.millenium(10, 10)

print isinstance(datetime1, DateTime) # True
print isinstance(datetime2, DateTime) # False

# @classmethod function also callable without instantiating the class, but its definition follows Sub class, not Parent class, via i
# nheritance, can be overridden by subclass. That’s because the first argument for @classmethod function must always be cls (class).

# Factory methods, that are used to create an instance for a class using for example some sort of pre-processing.


