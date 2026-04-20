from random import randint, sample

class Bus():
    
    def __init__(self,busNo,fr, to):
        self.busNo = busNo
        self.fr = fr
        self.to = to
        
    def getSeat(self):
        total_seats = 48
        empty_count = randint(1, total_seats)  # random number of empty seats
        empty_seats = sample(range(1, total_seats + 1), empty_count)

        print(f"Empty seats from {self.fr} to {self.to}:")
        for seat in sorted(empty_seats):
            print(f"Seat {seat} is empty")
    
    def getDistance(self):
         print(f"Distance from {self.fr} to {self.to} is {randint(9, 999)} KM ")
    
    def getFare(self):
        print(f"Fare from {self.fr} to {self.to} is {randint(111, 2222)}")
    
b = Bus("HP01G8866","delhi","palampur")   
b.getSeat()
b.getDistance()
b.getFare()       