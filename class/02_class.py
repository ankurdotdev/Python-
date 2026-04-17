class Rectangle():
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    
    def area(self):
        return self.length*self.breadth
        
a1 = Rectangle(4, 5)
a2 = Rectangle(7,3)

print("Area of rectange is =", a1.area())
print("Area of rectange is =", a2.area())
        