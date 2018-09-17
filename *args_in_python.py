
# *args and **kwargs are mostly used in function definitions. *args and **kwargs allow you to pass a variable number of arguments to a 
# function. What does variable mean here is that you do not know before hand that how many arguments can be passed to your function by the 
# user so in this case you use these two keywords

# args is used to send a non-keyworded variable length argument list to the function.
# Here an example to help you get a clear idea:

def test_var_args(f_arg, *argv):
    print "first normal arg:", f_arg
    for arg in argv:
        print "another arg through *argv :", arg

test_var_args('yasoob','python','eggs','test')


class parking():
	def __init__(self):
		self.y = 'Porsche' 

	def park(self,reg_no,color):
		print 'Park Vehicle: ' + reg_no + ' of color ' + color 

class processor():
	def __init__(self):
		self.parking = parking()

	def process_command(self):
		args = ['KA-01-HH-9999', 'White']
		if hasattr(self.parking, 'park'):
			command_function = getattr(self.parking, 'park')
			command_function(*args)

process = processor()
process.process_command()

