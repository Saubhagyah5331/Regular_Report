# Create a base class called Animal with a method eat() that prints "This animal eats food." Create two subclasses:

# Herbivore with a method diet() that prints "Eats plants."
# Carnivore with a method diet() that prints "Eats meat."
# Create objects of both subclasses and call their eat() and diet() methods.

class Animal:
    def eat(self):
        return "This animal eats food."

class Herbivore(Animal):
    def diet(self):
        return"Eats plants."

class Carnivore(Animal):
    def diet(self):
        return"Eats meat."
    
H1 = Herbivore()
C1 = Carnivore()

print(f"{H1.eat()}\n{H1.diet()}\n\n{C1.eat()}\n{C1.diet()}")