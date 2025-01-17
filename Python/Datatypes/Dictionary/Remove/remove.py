# Removing Dictionary Items
# We can remove items from dictionary using the following methods:

# del: Removes an item by key.
# pop(): Removes an item by key and returns its value.
# clear(): Empties the dictionary.
# popitem(): Removes and returns the last key-value pair.


dic = {"Name": "Saubhagya", "Age": 23, "Male": True, "Town": "JAMNAGAR"}

del dic["Age"]
print(dic)
dic.pop("Name")
print(dic)

dic.popitem()
print(dic)

dic.clear()
print(dic)

