# Create a base class called Person with attributes name and age. Use the __init__() method to initialize these attributes. Create a subclass called Employee that inherits from Person and adds an attribute salary. Use super() to initialize the name and age attributes in the Employee class. Create an object of Employee and print all its details.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary


E1 = Employee("Saubha", 23, 2344565)

print(f"Name: {E1.name}\nAge: {E1.age}\nSalary: {E1.salary} ₹")