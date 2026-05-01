# Problem:
# Create a base class Person with:

# attributes: name, age
# method: introduce()

# Create a child class Student that:

# adds roll_no
# overrides introduce() to include roll number.

# Goal: Understand constructor chaining and method overriding.

class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def introduce(self):
        print(f"the name of the student is {self.name} and his age is {self.age}")
        
        
class Student(Person):
    
    def __init__(self,name, age, rollNo):
        super().__init__(name, age)
        self.rollNo = rollNo
    
    def introduce(self):
        print(f"the name of the student is {self.name} having roll no. {self.rollNo} and his age is {self.age}")        
        
s1 = Student("Ankur",22,7894)
s1.introduce()
   
        