# In Python, decorators are a powerful and flexible way to modify or extend the behavior of functions or methods, without changing their actual code. A decorator is essentially a function that takes another function as an argument and returns a new function with enhanced functionality.

def deco(greet):
    def first():
        print("Hello")
        greet()
    return first

@deco
def second():
    print("Hello second")

second()