# Overload > for Student
# Create class Student:
# Store marks
# Overload > to compare marks

class Student:
    def __init__(self, marks):
        self.marks = marks
        
    def __gt__(self,other):
        return self.marks > other.marks
          
m1 = Student(99)          
m2 = Student(98)    

print(m1.__gt__(m2))      