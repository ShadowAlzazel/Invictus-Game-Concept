#Started 10/23/2021

#Basic Class
class Ship:
    ammount = 0
    shiptype = 'CIV'
    shipStats = {
        "FP": 0, "ACC": 10, "EVA": 10, "SPD": 15,
        "armor": 1, "luck": 10
    }

    def __init__(self, hullnumber, name):
        self.command = 'ASCS'
        self.name = name
        self.hullnumber = hullnumber
        self.vesselID = ''.join([self.shiptype, '-', str(self.hullnumber)])

        print("New Ship Launched", end=': ')
        print(self.command, '-', name, sep='', end=', ')
        Ship.ammount += 1


    def fullInspect(self):
        print("--<->---------------------------------------------------------------------<->--")
        print("Name: ", end='')
        print(self.command,'-' , self.name, sep='')
        print("Vessel Identifier: ", end='')
        print(self.vesselID)
        print("Ship Stats:")
        print(self.shipStats)
        print("Primary Armament:")
        for x in self.mainArm:
            print(x.armaID, x.gunStats)
        print("Shield Capcity at", "%.2f%%" % ((self.shields / self.__class__.shields) * 100.0), end=', ')
        print("with", self.shields // 1, "out of", self.__class__.shields, "remaining")
        print("Hull Integrity at", "%.2f%%" % ((self.hull / self.__class__.hull) * 100.0), end=', ')
        print("with", self.hull // 1, "out of", self.__class__.hull, "remaining")
        print("--<->---------------------------------------------------------------------<->--")


    def takeDamage(self, dmgN):
        if self.shields > dmgN:
            self.shields -= dmgN
        elif self.hull > dmgN:
            truDmgN = dmgN - self.shields 
            self.shields = 0
            self.hull -= truDmgN / self.shipStats["armor"]
        else: 
            print(self.name, "has been destryed!")
            del self


    def selfRepair(self):
        self.hull = self.__class__.hull
        print(self.name, "Repaired!")

"""--------------------------------------------------------------------------------------"""

#Battleship
class Battleship(Ship):
    ammount = 0
    shiptype = 'BB'
    shipStats = {
        "FP": 300, "ACC": 38, "EVA": 30, "SPD": 25,
        "armor": 3, "luck": 10
    }

    shields = 10000 
    hull = 10000

    def __init__(self, hullnumber, name):
        super().__init__(hullnumber, name)

        print(self.shiptype, '-', hullnumber, sep='')
        Battleship.ammount += 1


#Battlecruiser
class Battlecruiser(Ship):
    ammount = 0
    shiptype = 'BC'
    shipStats = {       
        "FP": 250, "ACC": 45, "EVA": 35, "SPD": 29,
        "armor": 2.75, "luck": 10
    }

    shields = 8200
    hull = 7700

    def __init__(self, hullnumber, name):
        super().__init__(hullnumber, name)

        print(self.shiptype, '-', hullnumber, sep='')
        Battlecruiser.ammount += 1


#Strikecruiser
class Strikecruiser(Ship):
    ammount = 0
    shiptype = 'CS'
    shipStats = {
        "FP": 180, "ACC": 38, "EVA": 40, "SPD": 33,
        "armor": 2.5, "luck": 10
    }
    
    shields = 7100
    hull = 5600

    def __init__(self, hullnumber, name):
        super().__init__(hullnumber, name)

        print(self.shiptype, '-', hullnumber, sep='')
        Strikecruiser.ammount += 1


#Heavycrusier
class Heavycruiser(Ship):
    ammount = 0 
    shiptype = 'CA'
    shipStats = {
        "FP": 190, "ACC": 33, "EVA": 30, "SPD": 25,
        "armor": 2.5, "luck": 10
    }
    
    shields = 6700
    hull = 7600

    def __init__(self, hullnumber, name):
        super().__init__(hullnumber, name)

        print(self.shiptype, '-', hullnumber, sep='')
        Heavycruiser.ammount += 1


#Destroyers
class Destroyer(Ship):
    ammount = 0
    shiptype = 'DD'
    shipStats = {
        "FP": 60, "ACC": 45, "EVA": 65, "SPD": 55,
        "armor": 1, "luck": 10
    }
    
    shields = 1200
    hull = 900

    def __init__(self, hullnumber, name):
        super().__init__(hullnumber, name)

        print(self.shiptype, '-', hullnumber, sep='')
        Destroyer.ammount += 1