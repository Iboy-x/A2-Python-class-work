# car  = > vehicleID, registeration, dateOfRegisteration, engineSize, purchasePrice
# PRIVATE => __attributeName
# constructor => __init__()
# self => used to refer to the calling object 
# self is always the first parameter of any method defined within the class 
# self.attributeName
# self.methodName


class Car: 
    # Constrcutor 
    # __ : PRIVATE 
    # self : for self references

    # ASSIGIN DATA TYPES ---------------
    #self.__vehicleID : STRING
    #self.__registeration : STRING
    #self.__dateOfRegisteration :DATE
    #self.__engineSize : INTEGER
    #self.__purachasePrice : REAL 
    def __init__(self, pVID, pES ):
        # in python use constructor to declare/ initialize all attribute
        self.__vehichleID = pVID
        self.__registeration = "" # none can be used here as well
        self.__dateOfRegisteration = None
        self.__engineSize = pES
        self.__purchasePrice = 0.0
    
    def setRegisteration(self, r):
        self.__registeration = r
    def setDateOfRegisteration(self, dor):
        self.__dateOfRegisteration = dor
    def setPurchasePrice(self, pp):
        self.__purchasePrice = pp
    

    def getVehichleID(self):
        return self.__vehichleID
    def getRegistertion(self):
        return self.__registeration
    def getDateOfRegisteration(self):
        return self.__dateOfRegisteration
    def getEngineSize(self):
        return self.__engineSize
    def getPurchasePrice(self):
        return self.__purchasePrice
    
myCar = Car("ABC123", 2500 )
myCar.setPurchasePrice(100000000)
var = myCar.getPurchasePrice()
print(var) 
print(myCar.getVehichleID())