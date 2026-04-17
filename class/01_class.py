# class Student():
#     name ="Anshu"
#     age = "22"
    
#     def display(self):
#         print(f"The age of the student is {self.age}. The name of the student is {self.name}")
# obj = Student()   
# obj.display()  
class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")    

s1 = Student("Anshu", 22)
s2 = Student("Anku", 22)

s1.display()
s2.display()