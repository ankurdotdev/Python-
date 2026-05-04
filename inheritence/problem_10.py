# Overload * for Rectangle Area
# * should multiply areas of two rectangles

class Rectangle:
    # Constructor: stores width and height of rectangle
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    # Method to calculate area of rectangle
    def area(self):
        return self.height * self.width     
        
    # Operator overloading for *
    # This tells Python what to do when we write r1 * r2
    def __mul__(self, other):
        # Multiply area of first rectangle with area of second
        return self.area() * other.area()
        

# Creating two rectangle objects
r1 = Rectangle(4, 5)   # Area = 20
r2 = Rectangle(2, 3)   # Area = 6

# Calling area method directly
print (r1.area())
print (r2.area())

# Using * operator (calls __mul__ internally)
print(r1 * r2)   # Output: 120

# or 

# print(r1.__mul__(r2))