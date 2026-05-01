class Employee():
    def work(self):
        print("Employee is working on tasks")
        
class Manager(Employee):
    def work(self):
        super().work()  
        print("Manager is managing the team")     

m = Manager()
m.work()
        