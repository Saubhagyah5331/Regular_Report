# Removing Elements from List
# We can remove elements from a list using:

# remove(): Removes the first occurrence of an element.
# pop(): Removes the element at a specific index or the last element if no index is specified.
# del statement: Deletes an element at a specified index.

a = ["Hello", 3 , 4, 5]

print(a)
a.remove(3)
print(a)
a.pop()
print(a)
del(a[0])
print(a)