# Arbitrary Keyword Arguments, **kwargs
# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.

# This way the function will receive a dictionary of arguments, and can access the items accordingly:

def arb_function(**kargs):
    print("First Name: " + kargs["fname"] + "\nSurname: " + kargs["sname"])

arb_function(fname = "Saubhagya", sname = "Vish", age = 21)
