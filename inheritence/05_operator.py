#operator overloading

class Number:
    def __init__(self, n):
        self.n = n
        
    def __add__(self, other):
        return self.n + other.n    
    
n1 = Number(1)
n2 = Number(2)

print (n1 + n2)
print (n1.__add__(n2))