class Calculator():
    def __init__(self, n):
        self.n = n
        
    def square(self):
        return f"Square: {self.n*self.n}"    
    def cube(self):
        return f"Cube: {self.n*self.n*self.n}"    
    def squareroot(self):
        return f"Squareroot: {self.n**1/2}"    
    
c = Calculator(4)
print(c.square())    
print(c.cube())    
print(c.squareroot())    