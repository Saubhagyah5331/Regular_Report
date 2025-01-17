# Create a base class called Animal with a method speak() that prints "Animal speaks." Create a derived class called Dog that overrides the speak() method to print "Dog barks." Create an object of both classes and call their speak() methods.

class Animal:

    def speak(self):
        print("Animal speaks")

class Dog(Animal):

    def speak(self):
        print("Dog Barks.")

a1 = Animal()
a1.speak()

d1 = Dog()
d1.speak()

# This is also a method overriding