# Create a base class called Animal with a method speak() that prints "Animal speaks." Create two subclasses, Dog and Cat, that override the speak() method to print "Dog barks" and "Cat meows," respectively. Create objects of each subclass and call the speak() method.


class Animal:
    def speak(self):
        return "Animal speaks."
    
class Dog(Animal):
    def speak(self):
        return "Dog barks"
    
class Cat(Animal):
    def speak(self):
        return "Cat meows"
    

A1 = Animal()
D1 = Dog()
C1 = Cat()

print(f"{A1.speak()}\n{D1.speak()}\n{C1.speak()}")

