from random import randint

class CarRecord: # declaring a lass without other methods 
    def __init__(self): # constrcutor 
        self.vehichleID = ""
        self.Registeration = ""
        self.DateOfRegisteration = None 
        self.EngineSize = 0 
        self.PurchasPrice = 0.00
    
'''myCar = CarRecord()
myCar.vehichleID = "ABC123"
myCar.Registeration = "XYZ"
myCar.EngineSize = 3000
print("Vehichle ID: ", myCar.vehichleID)'''

carArray = [CarRecord() for i in range(100)]
for i in range(100):
    carArray[i].EngineSize = randint(1000, 3000)
for i in carArray:
    print(i.EngineSize)



