# 2. Method Decorators:
# Used to decorate methods within a class. They often handle special cases, such as the self argument for instance methods.

def func(newfunc):
    def new(self):
        print("Excecute")
        res = newfunc(self)
        return res
    return new

class A:
    @func
    def say_hello(self):
        print("hello2")

c1 = A()
c1.say_hello()