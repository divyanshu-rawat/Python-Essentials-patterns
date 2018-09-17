


# The hasattr() method returns true if an object has the given named attribute and false if it does not.
# hasattr(object, name)

class parking():
	def __init__(self):
		self.y = 'Porsche' 

	def park(self,x):
		print 'Park Vehicle: ' + x 

class processor():
	def __init__(self):
		self.parking = parking()

	def process_command(self):
		print hasattr(self.parking, 'park')
		command_function = getattr(self.parking, 'park')
		command_function('Audi')

process = processor()
process.process_command()