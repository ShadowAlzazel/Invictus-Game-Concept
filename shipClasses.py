#Started 10/24/2021
from shipTypes import *
from Armaments import *

#--<->--------------BATTLESHIPS---------------<->--

class EssexClass(Battleship):
    ammount = 0

    FP = 325
    shields = 12500
    hull = 10000

    def __init__(self, hullnumber, name):
        super().__init__(hullnumber, name)
        turretCases = [''.join([self.shipID, x]) for x in ['T1', 'T1', 'T3']]
        self.mainArm = [tripleZeusCannonMKVI(x) for x in turretCases]

        EssexClass.ammount += 1


    """
    def EssexBarrage(self):
        e = self.FP * 200
        print("Essex Barrage! Dmg:", e)
    """

class AmagiClass(Battleship):
    ammount = 0

    FP = 305
    ACC = 34
    EVA = 33
    shields = 11000
    hull = 9500
    #mainGuns = [zeusCannonMK8(x, hullnumber) for x in range(1,3)]
    
    def __init__(self, hullnumber, name):
        super().__init__(hullnumber, name)
        turretCases = [''.join([self.shipID, x]) for x in ['T1', 'T1', 'T3', 'T4']]
        self.mainArm = [doubleZeusCannonMKVI(x) for x in turretCases]
        
        AmagiClass.ammount += 1

#--<->--------------DESTROYERS---------------<->--

class JohnstonClass(Destroyer):
    ammount = 0
    
    def __init__(self, hullnumber, name):
        super().__init__(hullnumber, name)
        self.mainArm = [quadBPDLaser(''.join([self.shipID, '-T1']))]

        JohnstonClass.ammount += 1


BB66 = AmagiClass(66, 'Amagi')
