# 1. Function Decorators:
# The most common type of decorator, which takes a function as input and returns a new function. The example above demonstrates this type.

def funct1(func2):
    def new():
        print("Hello first")
        func2()
    return new

@funct1
def add():
    print("hello")

add()
