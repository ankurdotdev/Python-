class Bird:
    def sound(self):
        print("bird is chirping")

class Parrot(Bird):
    def sound(self):
        super().sound()
        print("parrot talks")  

p = Parrot()
p.sound()             