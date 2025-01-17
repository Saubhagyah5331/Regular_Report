# Problem:
# Create a class called Point with attributes x and y. Overload the + operator to add two Point objects by adding their x and y values.

# Example:

# Point1: (3, 4)
# Point2: (1, 2)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        raise TypeError("The values are not points!!")
    
    def __str__(self):
        return f"({self.x}, {self.y})"

P1 = Point(3,4)
P2 = Point(4,5)

result = P1 + P2

print(f"Point1: ({P1.x},{P1.y})")
print(f"Point2: ({P2.x},{P2.y})")
print(f"Result: ({result.x},{result.y})")


