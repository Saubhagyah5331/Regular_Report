# Problem:
# Create a base class called Shape with a method area() that prints "Undefined area." Create two subclasses:

# Circle with an attribute radius and an overridden area() method to calculate and print the area of a circle.
# Rectangle with attributes width and height and an overridden area() method to calculate and print the area of a rectangle.
# Use the formula:

# Circle area = π × radius²
# Rectangle area = width × height
# Create objects of Circle and Rectangle and call their area() methods.

# Example Input:

# Circle with radius 3
# Rectangle with width 4 and height 5

class Shape:
    pi = 3.14
    def area(self):
        print("Undefined area.")

class Circle(Shape):
    def area(self, radius):
        self.radius = radius
        area = self.pi * self.radius**2

        return area
    
class Rect(Shape):
    def area(self, width, height):
        self.width = width
        self.height = height

        area = self.width * self.height

        return area

c1 = Circle()
r1 = Rect()

temp = False
while temp != True:
    choice = int(input("*******Menu*********\n1 --> Area of Circle.\n2. --> Area of Rectangle\n3. --> Exit\n\nEnter the Choice: "))

    if choice == 1:
        radius = float(input("Please Enter the Radius: "))
        print(f"Area of Circle: {c1.area(radius)}\n\n")

    elif choice == 2:
        width = int(input("Enter the Width: "))
        height = int(input("Enter the Height: "))
        print(f"Area of Rectangle: {r1.area(width, height)}\n\n")

    elif choice == 3:
        temp = True
    
    else:
        print("Invalid Choice!!\n\n")

