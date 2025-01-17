# Removing Elements from the Set in Python
# We can remove an element from a set in Python using several methods: remove(), discard() and pop(). Each method works slightly differently :

# Using remove() Method or discard() Method
# Using pop() Method
# Using clear() Method

set = {1, 2, 3, 4, 5, 6, 8, 9}

set.remove(1) #it raise error if the value doesn't exists.
print(set)

set.discard(1) #it doesn't raise error if value doesn't exists.
print(set)

set.pop()
print(set)

set.clear()
print(set)
