class Grandparent:
    def intro(self):
        print("I am the Grandfather")
class Parent(Grandparent):
    def intro(self):
        super().intro()
        print("I am the Father")
class Child(Parent):        
    def intro(self):
        super().intro()
        print("I am the Son")
c = Child()    
c.intro()