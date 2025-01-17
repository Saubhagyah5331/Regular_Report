# Positional-Only Arguments
# You can specify that a function can have ONLY positional arguments, or ONLY keyword arguments.

# To specify that a function can have only positional arguments, add , / after the arguments:


def pos_fuction(x, /):
    print(x)

pos_fuction(3)

pos_fuction(x = 3) #through error