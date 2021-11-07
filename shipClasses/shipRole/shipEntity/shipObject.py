#Basic Ship Object

"""-------------------------------SHIP-OBJECT-------------------------------------"""

class Ship:
    spaceEntity = 'shipObject'
    ammount = 0
    shiptype = 'CIV'
    shipStats = {
        "FP": 0, "ACC": 10, "EVA": 10, "SPD": 15,
        "armor": 1, "luck": 10
    }

    def __init__(self, hullnumber, name):
        Ship.ammount += 1
        self.command = 'ASCS'
        self.name = name
        self.hullnumber = hullnumber
        self.vesselID = ''.join([self.shiptype, '-', str(self.hullnumber)])
        self.placeSpace = []
        self.primaryBattery = []
        self.defenses = {'ShieldType': [], 'ArmorType': []}

        print("New Ship Launched", end=': ')
        print(self.command, '-', name, sep='', end=', ')

    #damage function that takes in a value 
    def takeDamage(self, damageNum):
        if self.shields > damageNum:
            damageS = self.defenses['ShieldType'][0].shieldDamage(damageNum)
            self.shields -= damageS
        elif self.hull > damageNum:
            damageH = self.defenses['ArmorType'][0].armorDamage(damageNum) - self.shields
            self.shields = 0
            self.hull -= damageH
        else: 
            print(self.name, "has been destryed!")

    #full self repair
    def selfRepair(self):
        self.hull = self.__class__.hull
        print(self.name, "Repaired!")

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

print("shipObject")