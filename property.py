
# You will learn about Python @property; pythonic way to use getters and setters.
# Python has a great concept called property which makes the life of an object oriented programmer much simpler.

class Celsius_dec:
    def __init__(self, temperature = 0):
        self._temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

# We can further go on and not define names get_temperature and set_temperature as they are unnecessary and pollute 
# the class namespace.

# @property

# def property(fun):
# 	def getter_fn:
# 		print("Getter!")
# 		fun()
# 	return inner_fn

#  similar to temperature = property(temperature)


    @property
    def temperature(self):
        print("Getting value")
        return self._temperature


# We can further go on and not define names get_temperature and set_temperature as they are unnecessary and pollute 
# the class namespace.

# The next step would be to extend this property with a setter and a deleter. And this happens with the appropriate 
# methods:
#  @temperature.setter

    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value


class Celsius:
    def __init__(self, temperature = 0):
        self._temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    def get_temperature(self):
        print("Getting value")
        return self._temperature

    def set_temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value

    temperature = property(get_temperature,set_temperature)

# The property() function returns a special descriptor object:

# property().getter
# <built-in method getter of property object at 0x10ff07998>
# property().setter
# <built-in method setter of property object at 0x10ff07940>
# property().deleter
# <built-in method deleter of property object at 0x10ff07998>


class_instance = Celsius()
class_instance.temperature = -273
print class_instance.temperature

# print class_instance.temperature

# print class_instance.get_temperature()


# The big problem with the above update is that, all the clients who implemented our previous class in their program 
# have to modify their code from obj.temperature to obj.get_temperature() and all assignments like 
# obj.temperature = val to obj.set_temperature(val).


# c = Celsius()
# c.temperature = 45
# c.set_temperature(-294)
# print c.get_temperature()


# class C():
#     def __init__(self, y = 0):
#         self._x = y

#     def getx(self):
#         return self._x
#     def setx(self, value):
#         self._x = value
#     def delx(self):
#         del self._x
#     x = property(getx, setx, delx, "I'm the 'x' property.")



# print class_instance.getx()

# class C():
#     def __init__(self):
#         self._x = None

#     @property
#     def x(self):
#         """I'm the 'x' property."""
#         return self._x

#     @x.setter
#     def x(self, value):
#         self._x = value

#     @x.deleter
#     def x(self):
#         del self._x


# class_instance = C()

# class_instance.x()

# USE CASE

# 1 - @property depicts that it's the getter, right can be extended to setter. 
# 2 - makes the function as a property that otherwise it should remain as fuction.





