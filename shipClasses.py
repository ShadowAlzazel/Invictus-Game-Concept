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

#New Jersey Class Battleship
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

"""--<->----------------------------BATTLECRUISERS------------------------------<->--"""

#Zenith Class Battlecruiser
class ZenithClass(Battlecruiser):
    ammount = 0
    shipStats = {
        "FP": 297, "ACC": 50, "EVA": 35, "SPD": 30,
        "armor": 3, "luck": 10
    }

    shields = 9100
    hull = 8150

    def __init__(self, hullnumber, name):
        super().__init__(hullnumber, name)
        #seven mainGuns in 1 triple turret and 2 double turrets
        turretCases = [''.join([self.vesselID, x]) for x in ['-T1', '-T2', '-T3']]
        self.mainArm = [doubleArcThrowerMKV(turretCases[0]), doubleArcThrowerMKV(turretCases[1]), tripleZeusCannonMKVI(turretCases[2])]

        ZenithClass.ammount += 1

#Eclipse Class Battlecruiser
class EclipseClass(Battlecruiser):
    ammount = 0
    shipStats = {
        "FP": 277, "ACC": 49, "EVA": 38, "SPD": 31,
        "armor": 3, "luck": 10
    }

    shields = 9400
    hull = 8250

    def __init__(self, hullnumber, name):
        super().__init__(hullnumber, name)
        #seven mainGuns in 1 triple turret and 2 double turrets
        turretCases = [''.join([self.vesselID, x]) for x in ['-T1', '-T2', '-T3']]
        self.mainArm = [doubleZeusCannonMKVI(turretCases[0]), doubleZeusCannonMKVI(turretCases[1]), tripleArcThrowerMKV(turretCases[2])]

        EclipseClass.ammount += 1


"""--<->----------------------------STRIKECRUISERS------------------------------<->--"""

#Voltage Class Strikecruiser
class VoltageClass(Strikecruiser):
    ammount = 0
    shipStats = {
        "FP": 185, "ACC": 43, "EVA": 41, "SPD": 34,
        "armor": 2.5, "luck": 10
    }

    shields = 7350
    hull = 6300

    def __init__(self, hullnumber, name):
        super().__init__(hullnumber, name)
        #eleven mainGuns in 3 triple turrets and 1 double turret
        turretCases = [''.join([self.vesselID, x]) for x in ['-T1', '-T2', '-T3', '-T4']]
        self.mainArm = [tripleThorCannonMKVIII(turretCases[0]), doubleArcThrowerMKIV(turretCases[1]), 
                            doubleArcThrowerMKIV(turretCases[2]), tripleThorCannonMKVIII(turretCases[3])]

        VoltageClass.ammount += 1

#Dynamo Class Strikecruiser
class DynamoClass(Strikecruiser):
    ammount = 0
    shipStats = {
        "FP": 197, "ACC": 42, "EVA": 39, "SPD": 33,
        "armor": 2.5, "luck": 10
    }

    shields = 7100
    hull = 6200

    def __init__(self, hullnumber, name):
        super().__init__(hullnumber, name)
        #eleven mainGuns in 3 triple turrets and 1 double turret
        turretCases = [''.join([self.vesselID, x]) for x in ['-T1', '-T2', '-T3']]
        self.mainArm = [quadrupleThorCannonMKVIII(turretCases[0]), quadrupleThorCannonMKVIII(turretCases[1]),
                        doubleArcThrowerMKIV(turretCases[2])]

        DynamoClass.ammount += 1

"""--<->----------------------------STRIKECRUISERS------------------------------<->--"""

#Apocalypse Class Heavycrusier
class ApocalypseClass(Heavycruiser):
    ammount = 0
    shipStats = {
        "FP": 205, "ACC": 35, "EVA": 32, "SPD": 25,
        "armor": 2.5, "luck": 10
    }
    
    shields = 6860
    hull = 7700

    def __init__(self, hullnumber, name):
        super().__init__(hullnumber, name)
        #fifteen mainGuns in 5 triple turrets
        turretCases = [''.join([self.vesselID, x]) for x in ['-T1', '-T2', '-T3', '-T4', '-T5']]
        self.mainArm = [tripleThorCannonMKVIII(x) for x in turretCases] 

        ApocalypseClass.ammount += 1

"""--<->--------------------------DESTROYERS---------------------------<->--"""

#Johnston Class destroyer
class JohnstonClass(Destroyer):
    ammount = 0
    shipStats = {
        "FP": 67, "ACC": 48, "EVA": 66, "SPD": 55,
        "armor": 1, "luck": 10
    }
    
    def __init__(self, hullnumber, name):
        super().__init__(hullnumber, name)
        self.mainArm = [quadBPDLaser(''.join([self.vesselID, '-T1']))]

        JohnstonClass.ammount += 1

#Shimakaze class destroyer
class ShimakazeClass(Destroyer):
    ammount = 0
    shipStats = {
        "FP": 47, "ACC": 58, "EVA": 68, "SPD": 61,
        "armor": 1, "luck": 10
    }

    def __init__(self, hullnumber, name):
        super().__init__(hullnumber, name)
        self.mainArm = [quadBPDLaser(''.join([self.vesselID, '-T1']))]

        ShimakazeClass.ammount += 1