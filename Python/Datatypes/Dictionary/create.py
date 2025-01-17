# A Python dictionary is a data structure that stores the value in key: value pairs. Values in a dictionary can be of any data type and can be duplicated, whereas keys can’t be repeated and must be immutable.

# Example: Here, The data is stored in key:value pairs in dictionaries, which makes it easier to find values.


dic = {"Name": "saubhagya", "Age": 23}
print(dic)

dic2 = dict(Name = "Saubhagya", Age = 34, Male = True)
print(dic2)

print(type(dic), type(dic2))
print(type(dic["Name"]))
print(type(dic["Age"]))
