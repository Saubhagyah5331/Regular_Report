# Create a class called Person with attributes name and age. Use the __init__ method to initialize these attributes. Create an object of the Person class with the name "Alice" and age 25, then print the name and age of the person.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("Subham", 20)

print(f"Name: {person1.name} \n Age: {person1.age}")
