# Accessing of Tuples
# We can access the elements of a tuple by using indexing and slicing, similar to how we access elements in a list. Indexing starts at 0 for the first element and goes up to n-1, where n is the number of elements in the tuple. Negative indexing starts from -1 for the last element and goes backward.

tup = (1, 2, 3, "Hello")

print(tup[0])

print(tup[1:4])
print(tup[1:])
print(tup[:3])
print(tup[::-1])
