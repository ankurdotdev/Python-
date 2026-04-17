class Car():
    def __init__(self ,brand,model):
        self.brand = brand
        self.model = model
    
    def info(self):
        print (f"Brand: {self.brand}, Model: {self.model}")
        
        
c1= Car("Tata", "Harrier")        
c2= Car("Mahindra", "Thar")

c1.info()
c2.info()        