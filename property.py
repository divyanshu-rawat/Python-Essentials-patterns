
# You will learn about Python @property; pythonic way to use getters and setters.
# Python has a great concept called property which makes the life of an object oriented programmer much simpler.

class Celsius:
    def __init__(self, temperature = 0):
        self._temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value


# class_instance = Celsius()
# class_instance.set_temperature(-283)

# print class_instance.get_temperature()


# The big problem with the above update is that, all the clients who implemented our previous class in their program 
# have to modify their code from obj.temperature to obj.get_temperature() and all assignments like 
# obj.temperature = val to obj.set_temperature(val).


# c = Celsius()
# c.temperature = 45
# c.set_temperature(-294)
# print c.get_temperature()

