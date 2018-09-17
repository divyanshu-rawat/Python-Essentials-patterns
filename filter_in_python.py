
# filter(function_object, iterable)

# Like map function, filter function also returns a list of element. Unlike map function filter function can only have one iterable as input.

even_ = [2,3,4,5,6,7,8]

print map(lambda x: x % 2 == 0,even_)
print filter(lambda x: x % 2 == 0,even_)

dict_a = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}]

print filter(lambda x: x['name'] == 'python', dict_a)