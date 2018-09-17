
# List comprehensions are used for creating new list from another iterables.

# array = [1,2,3,4]

# array_square = []

# for n in array:
# 	array_square.append(n*n)


# using list_comprehension.

# new_list = [expression for_loop_one_or_more condtions]

# array_square = [n*n for n in array]

# print array_square

list_ = [1,2,3,4]

list__ =[2,3,4,5]

# result_ = []

# for a in list_:
# 	for b in list__:
# 		if(a == b):
# 			result_.append(a)


# print result_

# Using conditions in list comprehensions.


# common_number = [b for a in list_ for b in list__ if a == b]

# print common_number

list_a = ["Hello", "World", "In", "Python"]

small_list_a = [str.lower() for str in list_a]

print(small_list_a) # Output: ['hello', 'world', 'in', 'python']


new_list = [[a*2,a*3] for a in list__]

print new_list

