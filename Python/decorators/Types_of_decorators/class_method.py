# @classmethod
# The @classmethod decorator is used to define a method that operates on the class itself (i.e., it uses cl). Class methods can access and modify class state that applies across all instances of the class.

class A:
    @classmethod
    def add(cls, x, y):
        cls.x = x
        cls.y = y
        return f"Add : {cls.x + cls.y}"

print(A.add(10, 12))