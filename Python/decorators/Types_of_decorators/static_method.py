# @staticmethod
# The @staticmethod decorator is used to define a method that doesn’t operate on an instance of the class (i.e., it doesn’t use self). Static methods are called on the class itself, not on an instance of the class.
class A: 
    @staticmethod
    def add():
        a = 4
        b = 5
        c = a+b
        return c
a1 = A()
print(a1.add())