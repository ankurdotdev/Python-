class Shape:
    def area(self):
        print("Area not defined")
        
class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth 
    
    def area(self):
        print(f"Area of Rectangle is > {self.length * self.breadth}") 
        
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        print(f"Area of Circle > {3.14*(self.radius ** 2)}") 
        
r = Rectangle(10, 5)
c = Circle(7)

r.area()
c.area()                         
