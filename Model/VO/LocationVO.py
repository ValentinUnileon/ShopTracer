

class LocationVO:

    locationID = None
    icon = None

    def __init__(self):
        pass

    #Getters

    def getLocationID(self):
        return self.locationID
    
    def getLocationIcon(self):
        return self.icon
    
    #Setters

    def setLocationID(self, newLocationID):
        self.locationID=newLocationID

    def setLocationIcon(self, newLocationIcon):
        self.icon=newLocationIcon

