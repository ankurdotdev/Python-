class Employee:
    company = "Abc tech pvt ltd"
    name = "Default name"
    def show(self):
        print(f"The name of the employee is {self.name} and company is {self.company}")
        
class Coder:
    language = "Python"        
        
class Programmer(Employee, Coder):
    # company = "Xyz tech pvt ltd"        
    # name = "ankur"
    def show(self):
        print(f"The name of the employee is {self.name} and company is {self.company} and language used is {self.language}")
        
e = Employee()
p = Programmer()

e.show()
p.show()        