
import json

a = {
    'name': 'saubhagya',
    'age': 23
}

# by using dumps it convert any data type to json string
y = json.dumps(a)

# the type of json is json string

print(type(y))
print(y)
