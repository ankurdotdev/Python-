class Employee:
    def __init__(self):
        print("Constructor of Employee")
        self.a = 1
    
class Programmer(Employee):
    def __init__(self):
        super().__init__()
        print("Constructor of Programmer")
        self.b = 1        

class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("Constructor of Manager")
        self.c = 1         
    
# e = Employee()
# print(e.a)
    
# p = Programmer()
# print(p.b, p.b)

m = Manager()
print(m.a, m.b, m.c)
print(Manager.mro())    
print(Programmer.mro())
    