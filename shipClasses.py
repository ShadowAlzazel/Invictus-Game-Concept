#Started 10/24/2021
from shipTypes import *
from shipArmaments import *

"""--<->----------------------------BATTLESHIPS------------------------------<->--"""

#Essex Class Battleship
class EssexClass(Battleship):
    ammount = 0
    shipStats = {
        "FP": 325, "ACC": 43, "EVA": 30, "SPD": 25,
        "armor": 3, "luck": 10
    }

    shields = 12500
    hull = 10000

    def __init__(self, hullnumber, name):
        super().__init__(hullnumber, name)
        #Nine mainGuns in 3 triple turrets
        turretCases = [''.join([self.vesselID, x]) for x in ['-T1', '-T2', '-T3']]
        self.mainArm = [tripleZeusCannonMKVI(x) for x in turretCases]

        EssexClass.ammount += 1


    """
    def EssexBarrage(self):
        e = self.FP * 200
        print("Essex Barrage! Dmg:", e)
    """

#Amagi Class Battleship
class AmagiClass(Battleship):
    ammount = 0
    shipStats = {
        "FP": 305, "ACC": 44, "EVA": 33, "SPD": 27,
        "armor": 3, "luck": 10
    }

    shields = 11000
    hull = 9500
    
    def __init__(self, hullnumber, name):
        super().__init__(hullnumber, name)
        #Eight mainGuns in 4 double turrets
        turretCases = [''.join([self.vesselID, x]) for x in ['-T1', '-T2', '-T3', '-T4']]
        self.mainArm = [doubleZeusCannonMKVI(x) for x in turretCases]
        
        AmagiClass.ammount += 1

#Vittorio Veneto Class Battleship
class VittorioVenetoClass(Battleship):
    ammount = 0
    shipStats = {
        "FP": 313, "ACC": 43, "EVA": 29, "SPD": 24,
        "armor": 3, "luck": 10
    }

    shields = 10500
    hull = 11000

    def __init__(self, hullnumber, name):
        super().__init__(hullnumber, name)
        #Nine mainGuns in 3 triple turrets
        turretCases = [''.join([self.vesselID, x]) for x in ['-T1', '-T2', '-T3']]
        self.mainArm = [tripleZeusCannonMKVI(x) for x in turretCases]

        VittorioVenetoClass.ammount += 1

#Hood Class Battleship
class HoodClass(Battleship):
    ammount = 0
    shipStats = {
        "FP": 325, "ACC": 46, "EVA": 34, "SPD": 27,
        "armor": 3, "luck": 10
    }

    shields = 10500
    hull = 8500
    
    def __init__(self, hullnumber, name):
        super().__init__(hullnumber, name)
        #Eight mainGuns in 4 double turrets
        turretCases = [''.join([self.vesselID, x]) for x in ['-T1', '-T2', '-T3', '-T4']]
        self.mainArm = [doubleZeusCannonMKVI(x) for x in turretCases]
        
        HoodClass.ammount += 1

#Prince of Wales Class Battleship
class PrinceOfWalesClass(Battleship):
    ammount = 0
    shipStats = {
        "FP": 325, "ACC": 44, "EVA": 32, "SPD": 24,
        "armor": 3, "luck": 10
    }

    shields = 11000
    hull = 10500

    def __init__(self, hullnumber, name):
        super().__init__(hullnumber, name)
        #Eight mainGuns in 2 quadruple turrets
        turretCases = [''.join([self.vesselID, x]) for x in ['-T1', '-T2']]
        self.mainArm = [quadrupleZeusCannonMKVI(x) for x in turretCases]
        
        PrinceOfWalesClass.ammount += 1  

#New Jersey Class Batlleship
class NewJerseyClass(Battleship):
    ammount = 0 
    shipStats = {
        "FP": 356, "ACC": 48, "EVA": 34, "SPD": 29,
        "armor": 3, "luck": 10
    }

    shields = 16200
    hull = 14250

    def __init__(self, hullnumber, name):
        super().__init__(hullnumber, name)
        #nine mainGuns in 3 triple turrets
        turretCases = [''.join([self.vesselID, x]) for x in ['-T1', '-T2', '-T3']]
        self.mainArm = [tripleZeusCannonMKVII(x) for x in turretCases]   

        NewJerseyClass.ammount += 1    


"""--<->--------------------------DESTROYERS---------------------------<->--"""

class JohnstonClass(Destroyer):
    ammount = 0
    shipStats = {
         "FP": 67, "ACC": 48, "EVA": 68, "SPD": 55,
        "armor": 1, "luck": 10
    }
    
    def __init__(self, hullnumber, name):
        super().__init__(hullnumber, name)
        self.mainArm = [quadBPDLaser(''.join([self.vesselID, '-T1']))]

        JohnstonClass.ammount += 1

