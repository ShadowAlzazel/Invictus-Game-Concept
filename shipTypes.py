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
        self.vesselID = ''.join([self.shiptype, str(self.hullnumber),'-', self.command, str(Ship.ammount)])

        print("New Ship Launched", end=': ')
        print(self.command, '-', name, sep='', end=', ')
        Ship.ammount += 1


    def inspect(self):
        print(self.command,'-' , self.name, sep='', end=', ')
        print(self.shiptype, '-', self.hullnumber,':', sep='')
        print(self.shipStats)
        print("Shield Capcity at", "%.2f%%" % (self.shields / self.__class__.shields * 100.0))
        print("Hull Integrity at", "%.2f%%" % (self.hull / self.__class__.hull * 100.0))
        print("-<->--------------------------------------<->-")


    def takeDamage(self, dmgN):
        if self.shields > dmgN:
            self.shields -= dmgN
        elif self.hull > dmgN:
            truDmgN = dmgN - self.shields 
            self.shields = 0
            self.hull -= truDmgN // self.shipStats["armor"]
        else: 
            print("Ship Destryed")


#Battleships
class Battleship(Ship):
    ammount = 0
    shiptype = 'BB'
    shipStats = {
        "FP": 300, "ACC": 30, "EVA": 30, "SPD": 25,
        "armor": 3, "luck": 10
    }

    shields = 10000 
    hull = 10000

    def __init__(self, hullnumber, name):
        super().__init__(hullnumber, name)

        print(self.shiptype, '-', hullnumber, sep='')
        Battleship.ammount += 1

    def self_repair(self):
        self.hull = self.__class__.hull
        print(self.name, "Repaired!")


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