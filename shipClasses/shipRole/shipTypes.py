#from . shipEntity import Ship 
from shipClasses.shipRole.shipEntity import Ship

"""---------------------------------------SHIP-TYPES------------------------------------------"""

#Battleship
class Battleship(Ship):
    ammount = 0
    shiptype = 'BB'
    shipStats = {
        "FP": 650, "ACC": 35, "EVA": 30, "SPD": 25,
        "armor": 3, "luck": 10
    }

    shields = 45000 
    hull = 17500

    def __init__(self, hullnumber, name):
        Battleship.ammount += 1
        super().__init__(hullnumber, name)

        print(self.shiptype, '-', hullnumber, sep='')


#Battlecruiser
class Battlecruiser(Ship):
    ammount = 0
    shiptype = 'BC'
    shipStats = {       
        "FP": 500, "ACC": 45, "EVA": 35, "SPD": 29,
        "armor": 2.75, "luck": 10
    }

    shields = 27500
    hull = 12500

    def __init__(self, hullnumber, name):
        Battlecruiser.ammount += 1
        super().__init__(hullnumber, name)

        print(self.shiptype, '-', hullnumber, sep='')


#Strikecruiser
class Strikecruiser(Ship):
    ammount = 0
    shiptype = 'CS'
    shipStats = {
        "FP": 280, "ACC": 38, "EVA": 40, "SPD": 33,
        "armor": 2.5, "luck": 10
    }
    
    shields = 12500
    hull = 8500

    def __init__(self, hullnumber, name):
        Strikecruiser.ammount += 1
        super().__init__(hullnumber, name)

        print(self.shiptype, '-', hullnumber, sep='')


#Heavycrusier
class Heavycruiser(Ship):
    ammount = 0 
    shiptype = 'CA'
    shipStats = {
        "FP": 350, "ACC": 33, "EVA": 30, "SPD": 25,
        "armor": 2.5, "luck": 10
    }
    
    shields = 10000
    hull = 10000

    def __init__(self, hullnumber, name):
        Heavycruiser.ammount += 1
        super().__init__(hullnumber, name)

        print(self.shiptype, '-', hullnumber, sep='')


#Lightcruiser
class Lightcruiser(Ship):
    ammount = 0 
    shiptype = 'CL'
    shipStats = {
        "FP": 200, "ACC": 35, "EVA": 45, "SPD": 35,
        "armor": 2, "luck": 10
    }
    
    shields = 7500
    hull = 7500

    def __init__(self, hullnumber, name):
        Lightcruiser.ammount += 1
        super().__init__(hullnumber, name)

        print(self.shiptype, '-', hullnumber, sep='') 


#Destroyers
class Destroyer(Ship):
    ammount = 0
    shiptype = 'DD'
    shipStats = {
        "FP": 100, "ACC": 45, "EVA": 65, "SPD": 55,
        "armor": 1, "luck": 10
    }
    
    shields = 3500
    hull = 2500

    def __init__(self, hullnumber, name):
        Destroyer.ammount += 1
        super().__init__(hullnumber, name)

        print(self.shiptype, '-', hullnumber, sep='')

print("shipTypes")
