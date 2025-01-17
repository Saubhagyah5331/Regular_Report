# Create a class called Dog with an attribute name. Write a method called bark() that prints "Woof!" when called. Create an object of the Dog class with the name "Buddy" and call its bark() method.

class Dog:
    def __init__(self, name):
        self.name = name
    
    @staticmethod
    def bark():
        print("Woof!")


dog1 = Dog("Buddy")
print(dog1.name)
dog1.bark()