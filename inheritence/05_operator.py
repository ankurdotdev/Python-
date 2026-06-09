# Operator Overloading Example

class Number:
    # Constructor: stores the value inside the object
    def __init__(self, n):
        self.n = n
        
    # Overloading + operator
    # This tells Python what to do when we use: obj1 + obj2
    def __add__(self, other):
        # self -> first object
        # other -> second object
        return self.n + other.n    


# Creating two objects
n1 = Number(1)
n2 = Number(2)

# Using + operator (calls __add__ internally)
print(n1 + n2)

# Directly calling the dunder method (same result)
print(n1.__add__(n2))