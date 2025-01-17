# Adding Elements to a Set in Python
# We can add items to a set using add() method and update() method. add() method can be used to add only a single item. To add multiple items we use update() method.

set = {1, 2, 3, 8, 5, 5, 6, 7}

set.add(9)
print(set)

set.update([4, 0])
print(set)