keys = ["Name", "Age", "Male"]
values = ["Saubhagya", 23, True]

dic = {k:v for k,v in zip(keys, values)}

# dic = dict(zip(keys, values))
print(dic)