# Basic Example of Inheritance
# Inheritance allows us to define a class that inherits all the methods and properties from another class.

class A:
    def speak(self):
        print("The Dog Bark")
    
class B(A):
    def speak(self):
        print("The cat Meow")

B1 = B()
print(B.speak())
