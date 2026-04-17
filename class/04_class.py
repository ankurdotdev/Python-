class Circle():
    def __init__(self, radius):
        self.radius = radius
    
    def perimeter(self):
        return 2*3.14*self.radius
    
c1 = Circle(2)

print(c1.perimeter())    