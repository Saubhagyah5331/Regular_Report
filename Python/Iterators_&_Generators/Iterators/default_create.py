# An iterator in Python is an object that holds a sequence of values and provide sequential traversal through a collection of items such as lists, tuples and dictionaries. . The Python iterators object is initialized using the iter() method. It uses the next() method for iteration.

# __iter__(): __iter__() method initializes and returns the iterator object itself.
# __next__(): the __next__() method retrieves the next available item, throwing a StopIteration exception when no more items are available.

s = "hel"
itr = iter(s)

print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
