class Employee():
    def __init__(self, name,salary):
        self.name = name
        self.salary = salary
        
    def annual_salary(self):
        return self.salary*12
    
e1 = Employee("Anshika", 1200)
e2 = Employee("Ankur", 300)  

print(f"Name: {e1.name}, Annual Salary: {e1.annual_salary()}")
print(f"Name: {e2.name}, Annual Salary: {e2.annual_salary()}") 
 