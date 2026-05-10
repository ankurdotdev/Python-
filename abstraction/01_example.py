class Car:
    
    def __init__(self):
        # Internal states of the car controls (hidden from user)
        self.acc = False
        self.brk = False
        self.clutch = False
        
    def start(self):
        # Abstraction:
        # User only calls start(), without knowing
        # what internal steps are required to start the car
        self.acc = True
        self.clutch = True
        print("Car started...")


# User creates the car object
c1 = Car()

# User simply calls start()
# The internal working (accelerator, clutch) is hidden
c1.start()