#Basic Ship Object
#"""-------------------------------SHIP-OBJECT-------------------------------------"""

class Ship:
    spaceEntity = 'shipObject'
    ammount = 0
    shiptype = 'CIV'
    shipStats = {
        "FP": 10, "ACC": 10, "EVA": 50, "SPD": 5,
        "RDR": 3, "LCK": 10
    }

    def __init__(self, hullnumber, name):
        Ship.ammount += 1
        self.command = 'ASCS'
        self.name = name
        self.hullnumber = hullnumber
        self.vesselID = ''.join([self.shiptype, '-', str(self.hullnumber)])
        self.placeHex = []  #starSpace object
        self.orientation = 'R'
        self.radar = []  #radar object
        self.armaments = {'primaryBattery': [], 'secondaryBattery': [], 'broadsideBattery': []}
        self.defenses = {'shieldType': [], 'armorType': []}

        print("New Ship Launched", end=': ')
        print(self.command, '-', name, sep='', end=', ')


    #damage function that takes in a value 
    def takeDamage(self, damageNum):
        if self.shields > damageNum:
            damageS = self.defenses['shieldType'][0].shieldDamage(damageNum)
            self.shields -= damageS
            return damageS
        elif self.hull > damageNum:
            damageH = self.defenses['armorType'][0].armorDamage(damageNum) - self.shields
            self.shields = 0
            self.hull -= damageH
            return damageH
        else: 
            print(self.vesselID, self.command, self.name, "has been destryed!")
            del self


    #full self repair
    def shipReset(self):
        self.hull = self.__class__.hull
        self.shields = self.__class__.shields
        print(self.name, "Reset!")


    #find targets in minimum range 
    def findTargets(self):
        gunsReadyInRange = self.gunsReady()
        readyRanges = []
        for w in gunsReadyInRange:
            readyRanges.append(w.gunStats['RNG'])

        #find the max range of all guns loaded
        targets = []
        if readyRanges:
            targets = self.radar.findRadarTargets(max(readyRanges), self.placeHex)
        return targets


    #check if gun in range of a target ship
    def gunInRange(self, gunBattery, targetShip):
        if not self.radar.findGunTargets(gunBattery.gunStats['RNG'], self.placeHex, targetShip):
            return False 
        else:
            return True
    

    #chech all guns ready to fire
    def gunsReady(self):
        gunsPrimed = []
        for b in self.armaments.values():
            for g in b:
                if g.gunLoadTime == g.gunStats['RLD']:
                    gunsPrimed.append(g)
        return gunsPrimed


    #reload all guns
    def reloadGuns(self):
        for b in self.armaments.values():
            for g in b:
                g.reloadGun()


    #inspection function to look at stats
    def fullInspect(self):
        print("--<->---------------------------------------------------------------------<->--")
        print("Name: ", end='')
        print(self.command,'-' , self.name, sep='')
        print("Vessel Identifier: ", end='')
        print(self.vesselID)
        print("Ship Stats:")
        print(self.shipStats)
        print("Primary Armament:")
        for x in self.armaments['primaryBattery']:
            print(x.gunName, "in Turret", x.batteryID)
        print("Ship Defenses:")
        print(self.defenses['ArmorType'][0].armorName)
        print(self.defenses['ShieldType'][0].shieldName)
        print("Shield Capcity at", "%.2f%%" % ((self.shields / self.__class__.shields) * 100.0), end=', ')
        print("with", self.shields // 1, "out of", self.__class__.shields, "remaining")
        print("Hull Integrity at", "%.2f%%" % ((self.hull / self.__class__.hull) * 100.0), end=', ')
        print("with", self.hull // 1, "out of", self.__class__.hull, "remaining")
        print("--<->---------------------------------------------------------------------<->--")
