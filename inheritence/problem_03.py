class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)   # constructor chaining
        self.subject = subject

    def introduce(self):  # method overriding
        super().introduce()  # call parent method
        print(f"I teach {self.subject}.")


t = Teacher("Ankur", 22, "DSA")
t.introduce()