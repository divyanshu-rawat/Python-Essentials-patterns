# zip takes n number of iterables and returns list of tuples. ith element of the tuple is created using the ith element from each of the iterables.

# list_a = [1, 2, 3, 4, 5]
# list_b = ['a', 'b', 'c', 'd', 'e']

# zipped_list = zip(list_a, list_b)

# print zipped_list # [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]

# If the length of the iterables are not equal, zip creates the list of tuples of length equal to the smallest iterable.


# list_a = [1, 2, 3]
# list_b = ['a', 'b', 'c', 'd', 'e']

# zipped_list = zip(list_a, list_b)

# print zipped_list # [(1, 'a'), (2, 'b'), (3, 'c')]

# Unzip a list of tuples

zipper_list = [(1, 'a'), (2, 'b'), (3, 'c')]
 
list_a, list_b = zip(*zipper_list)

print list_a # (1, 2, 3)
print list_b # ('a', 'b', 'c')