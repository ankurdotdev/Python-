class Employee:
    company = "Abc tech pvt ltd"
    name = "Default name"
    def show(self):
        print(f"The name of the employee is {self.name} and company is {self.company}")
        
class Programmer(Employee):
    # company = "Xyz tech pvt ltd"        
    name = "ankur"
    def show(self):
        print(f"The name of the employee is {self.name} and company is {self.company}")
        
e = Employee()
p = Programmer()

e.show()
p.show()        