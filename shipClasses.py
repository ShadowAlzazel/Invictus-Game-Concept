#Started 10/24/2021
from shipTypes import *
from shipArmaments import *

#--<->----------------------------BATTLESHIPS------------------------------<->--

"""Essex Class Battleship"""
class EssexClass(Battleship):
    ammount = 0

    FP = 325
    ACC = 32
    shields = 12500
    hull = 10000
    #Nine mainGuns in 3 triple turrets

    def __init__(self, hullnumber, name):
        super().__init__(hullnumber, name)
        turretCases = [''.join([self.vesselID, x]) for x in ['T1', 'T2', 'T3']]
        self.mainArm = [tripleZeusCannonMKVI(x) for x in turretCases]

        EssexClass.ammount += 1


    """
    def EssexBarrage(self):
        e = self.FP * 200
        print("Essex Barrage! Dmg:", e)
    """

"""Amagi Class Battleship"""
class AmagiClass(Battleship):
    ammount = 0

    FP = 305
    ACC = 34
    EVA = 33
    shields = 11000
    hull = 9500
    #Eight mainGuns in 4 double turrets
    
    def __init__(self, hullnumber, name):
        super().__init__(hullnumber, name)
        turretCases = [''.join([self.vesselID, x]) for x in ['T1', 'T2', 'T3', 'T4']]
        self.mainArm = [doubleZeusCannonMKVI(x) for x in turretCases]
        
        AmagiClass.ammount += 1

"""Vittorio Veneto Class Battleship"""
class VittorioVenetoClass(Battleship):
    ammount = 0

    FP = 310
    ACC = 33
    EVA = 31 
    shields = 10500
    hull = 11000
    #Nine mainGuns in 3 triple turrets

    def __init__(self, hullnumber, name):
        super().__init__(hullnumber, name)
        turretCases = [''.join([self.vesselID, x]) for x in ['T1', 'T2', 'T3']]
        self.mainArm = [tripleZeusCannonMKVI(x) for x in turretCases]

        VittorioVenetoClass.ammount += 1

"""Hood Class Battleship"""
class HoodClass(Battleship):
    ammount = 0

    FP = 325
    ACC = 35
    EVA = 34
    shields = 10500
    hull = 8500
    #Eight mainGuns in 4 double turrets
    
    def __init__(self, hullnumber, name):
        super().__init__(hullnumber, name)
        turretCases = [''.join([self.vesselID, x]) for x in ['T1', 'T2', 'T3', 'T4']]
        self.mainArm = [doubleZeusCannonMKVI(x) for x in turretCases]
        
        HoodClass.ammount += 1

"""Prince of Wales Class Battleship"""
class PrinceOfWalesClass(Battleship):
    ammount = 0

    FP = 320
    shields = 11000
    hull = 10500
    #Eight mainGuns in 2 quadruple turrets

    def __init__(self, hullnumber, name):
        super().__init__(hullnumber, name)
        turretCases = [''.join([self.vesselID, x]) for x in ['T1', 'T2']]
        self.mainArm = [quadrupleZeusCannonMKVI(x) for x in turretCases]
        
        PrinceOfWalesClass.ammount += 1  



#--<->--------------DESTROYERS---------------<->--

class JohnstonClass(Destroyer):
    ammount = 0
    
    def __init__(self, hullnumber, name):
        super().__init__(hullnumber, name)
        self.mainArm = [quadBPDLaser(''.join([self.vesselID, '-T1']))]

        JohnstonClass.ammount += 1

