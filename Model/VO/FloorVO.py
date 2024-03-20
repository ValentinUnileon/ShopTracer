

class FloorVO:

    floorID=None
    number=None
    image=None

    def __init__(self):
        pass
     
    #Getters
        
    def getFloorID(self):
        return self.floorID
    
    def getFloorNumber(self):
        return self.number
    
    def getFloorImage(self):
        return self.image
    
    #Setters

    def setFloorID(self, newID):
        self.floorID=newID

    def setFloorNumber(self, newNumber):
        self.number=newNumber
    
    def setFloorImage(self, newImage):
        self.image=newImage