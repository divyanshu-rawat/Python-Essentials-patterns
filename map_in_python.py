
# map(function_object, iterable1, iterable2,...)

# map functions expects a function object and any number of iterables like list, dictionary, etc.
# It executes the function_object for each element in the sequence and returns a list of the elements modified by the function object.


def multiply(x):
	return x + x


print map(multiply, [1,2,3,4])

print map(lambda x : x*x, [1,2,3,4])

dict_a = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}]
  
map(lambda x : x['name'], dict_a) # Output: ['python', 'java']
  
map(lambda x : x['points']*10,  dict_a) # Output: [100, 80]

map(lambda x : x['name'] == "python", dict_a) # Output: [True, False]


list_a = [1,2,3]
list_b = [4,5,6]

print map(lambda x,y : x + y , list_a, list_b)