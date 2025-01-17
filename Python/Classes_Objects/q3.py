# Problem:
# Create a class called Circle with an attribute radius. Add two methods:

# area() to calculate and return the area of the circle.
# circumference() to calculate and return the circumference of the circle.
# Create an object of the Circle class with a radius of 5 and print its area and circumference.

# Hint: Use the formula:

# Area = π × radius²
# Circumference = 2 × π × radius


class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        area = self.pi * (self.radius**2)
        return area
    
    def Circumference(self):
        circum = 2 * self.pi * self.radius
        return circum
    
circle1 = Circle(2)
print(f"The area of the circle is: {circle1.area()} \nCircumference is: {circle1.Circumference()}")

