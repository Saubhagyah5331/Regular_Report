#converting json to python

import json
a = '{"name":"saubhagya", "age": 21}' 

y = json.loads(a)

print(type(a))
print(a)
print(type(y))
print(y)