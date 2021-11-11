#Basic Ship Object

"""-------------------------------SHIP-OBJECT-------------------------------------"""

class Ship:
    spaceEntity = 'shipObject'
    ammount = 0
    shiptype = 'CIV'
    shipStats = {
        "FP": 0, "ACC": 10, "EVA": 10, "SPD": 15,
        "RDR": 3, "LCK": 10
    }

    def __init__(self, hullnumber, name):
        Ship.ammount += 1
        self.command = 'ASCS'
        self.name = name
        self.hullnumber = hullnumber
        self.vesselID = ''.join([self.shiptype, '-', str(self.hullnumber)])
        self.placeSpace = []
        self.radar = []
        self.primaryBattery = []
        self.secondaryBattery = []
        self.broadsideBattery = []
        self.defenses = {'ShieldType': [], 'ArmorType': []}

        print("New Ship Launched", end=': ')
        print(self.command, '-', name, sep='', end=', ')


    #damage function that takes in a value 
    def takeDamage(self, damageNum):
        if self.shields > damageNum:
            damageS = self.defenses['ShieldType'][0].shieldDamage(damageNum)
            self.shields -= damageS
            return damageS
        elif self.hull > damageNum:
            damageH = self.defenses['ArmorType'][0].armorDamage(damageNum) - self.shields
            self.shields = 0
            self.hull -= damageH
            return damageH
        else: 
            print(self.vesselID, self.command, self.name, "has been destryed!")
            del self



    #full self repair
    def selfRepair(self):
        self.hull = self.__class__.hull
        print(self.name, "Repaired!")


    #find targets in minimum range 
    def findTargets(self, specifics = False):
        readyGunsRange = self.gunsReady()
        readyRanges = []
        for w in readyGunsRange:
            readyRanges.append(w.gunStats['RNG'])

        if not specifics:
            targets = self.radar.findRadarTargets(max(readyRanges), self.placeSpace)
            return targets

        elif specifics:
            primaryRanges = []
            secondaryRanges = []
            boradsideRanges = []
            for x in self.primaryBattery:
                primaryRanges.append(x.gunStats['RNG'])
            for y in self.secondaryBattery:
                secondaryRanges.append(y.gunStats['RNG'])
            for z in self.broadsideBattery:
                boradsideRanges.append(z.gunStats['RNG'])
            return primaryRanges, secondaryRanges, boradsideRanges


    def gunInRange(self, gunBattery, targetShip):
        if not self.radar.findGunTargets(gunBattery.gunStats['RNG'], self.placeSpace, targetShip):
            return False 
        else:
            return True
    

    #chech all guns ready to fire
    def gunsReady(self):
        gunsPrimed = []
        for x in self.primaryBattery:
            if x.gunLoadTime == x.gunStats['RLD']:
                gunsPrimed.append(x)
        for y in self.secondaryBattery:
            if y.gunLoadTime == y.gunStats['RLD']:
                gunsPrimed.append(y)
        for z in self.broadsideBattery:
            if z.gunLoadTime == z.gunStats['RLD']:
                gunsPrimed.append(z)
        
        return gunsPrimed


    #reload all guns
    def reloadGuns(self):
        for x in self.primaryBattery:
            x.reloadGun()
        for y in self.secondaryBattery:
            y.reloadGun()
        for z in self.broadsideBattery:
            z.reloadGun()
            

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
        for x in self.primaryBattery:
            print(x.gunName, "in Turret", x.batteryID)
        print("Ship Defenses:")
        print(self.defenses['ArmorType'][0].armorName)
        print(self.defenses['ShieldType'][0].shieldName)
        print("Shield Capcity at", "%.2f%%" % ((self.shields / self.__class__.shields) * 100.0), end=', ')
        print("with", self.shields // 1, "out of", self.__class__.shields, "remaining")
        print("Hull Integrity at", "%.2f%%" % ((self.hull / self.__class__.hull) * 100.0), end=', ')
        print("with", self.hull // 1, "out of", self.__class__.hull, "remaining")
        print("--<->---------------------------------------------------------------------<->--")
