class Vehicle:
    def __init__(self,type):
        self.type = type
        
    def start(self):    
        print(f"{self.type} is started")
        
class Bike(Vehicle):
    def wheelie(self):
        super().start()
        print(f"he is doing a wheelie on {self.type}")    
        
b = Bike("Bullet")
b.wheelie()            