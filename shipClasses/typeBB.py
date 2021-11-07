#Started 11/5/2021
#from . shipEquipment import *
#from . shipRole import Battleship
from shipClasses.shipEquipment import *
from shipClasses.shipRole import Battleship

#"""--<->----------------------------BATTLESHIPS------------------------------<->--"""

#Essex Class Battleship
class EssexClass(Battleship):
    ammount = 0
    shipStats = {
        "FP": 666, "ACC": 38, "EVA": 30, "SPD": 25,
        "armor": 3, "luck": 10
    }

    shields = 46600 
    hull = 18800

    def __init__(self, hullnumber, name):
        super().__init__(hullnumber, name)
        vID = self.vesselID
        self.defenses['ShieldType'].append(DarkEnergyShieldGen(vID))
        self.defenses['ArmorType'].append(DurasteelArmor(vID))
        self.primaryBattery = [triple_M22_ThorGigaGuns(vID, ''.join(['T', str(x)])) for x in range(1,5)]
        self.secondaryBattery = [triple_L13_HadronLance(vID, ''.join(['S', str(x)])) for x in range(1,5)]
        self.broadsideBattery = []
        for x in range(1, 25):
            if x <= 16:
                self.broadsideBattery.append(double_M6_TitanAutoCannons(vID, ''.join(['B', str(x)])))
            elif x <= 24:
                self.broadsideBattery.append(double_A5_LaserLance(vID, ''.join(['B', str(x)])))
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
        "FP": 682, "ACC": 37, "EVA": 31, "SPD": 26,
        "armor": 3, "luck": 10
    }

    shields = 43200 
    hull = 16800
    
    def __init__(self, hullnumber, name):
        super().__init__(hullnumber, name)
        vID = self.vesselID
        self.defenses['ShieldType'].append(DarkEnergyShieldGen(vID))
        self.defenses['ArmorType'].append(DurasteelArmor(vID))
        self.primaryBattery = [double_M22_ThorGigaGuns(vID, ''.join(['T', str(x)])) for x in range(1,7)]
        self.secondaryBattery = [triple_L13_HadronLance(vID, ''.join(['S', str(x)])) for x in range(1,5)]
        self.broadsideBattery = []
        for x in range(1, 25):
            if x <= 16:
                self.broadsideBattery.append(double_M6_TitanAutoCannons(vID, ''.join(['B', str(x)])))
            elif x <= 24:
                self.broadsideBattery.append(double_A5_LaserLance(vID, ''.join(['B', str(x)])))
        AmagiClass.ammount += 1

#Vittorio Veneto Class Battleship
class VittorioVenetoClass(Battleship):
    ammount = 0
    shipStats = {
        "FP": 660, "ACC": 35, "EVA": 30, "SPD": 25,
        "armor": 3, "luck": 10
    }

    shields = 42100 
    hull = 18400

    def __init__(self, hullnumber, name):
        super().__init__(hullnumber, name)
        vID = self.vesselID
        self.defenses['ShieldType'].append(DarkEnergyShieldGen(vID))
        self.defenses['ArmorType'].append(DurasteelArmor(vID))
        self.primaryBattery = [triple_M22_ThorGigaGuns(vID, ''.join(['T', str(x)])) for x in range(1,5)]
        self.secondaryBattery = [triple_L13_HadronLance(vID, ''.join(['S', str(x)])) for x in range(1,5)]
        self.broadsideBattery = []
        for x in range(1, 25):
            if x <= 16:
                self.broadsideBattery.append(double_M6_TitanAutoCannons(vID, ''.join(['B', str(x)])))
            elif x <= 24:
                self.broadsideBattery.append(double_A5_LaserLance(vID, ''.join(['B', str(x)])))
        VittorioVenetoClass.ammount += 1

#Hood Class Battleship
class HoodClass(Battleship):
    ammount = 0
    shipStats = {
        "FP": 685, "ACC": 37, "EVA": 30, "SPD": 26,
        "armor": 3, "luck": 10
    }

    shields = 45300 
    hull = 17600
    
    def __init__(self, hullnumber, name):
        super().__init__(hullnumber, name)
        vID = self.vesselID
        self.defenses['ShieldType'].append(DarkEnergyShieldGen(vID))
        self.defenses['ArmorType'].append(DurasteelArmor(vID))
        self.primaryBattery = [double_M22_ThorGigaGuns(vID, ''.join(['T', str(x)])) for x in range(1,7)]
        self.secondaryBattery = [triple_L13_HadronLance(vID, ''.join(['S', str(x)])) for x in range(1,5)]
        self.broadsideBattery = []
        for x in range(1, 25):
            if x <= 16:
                self.broadsideBattery.append(double_M6_TitanAutoCannons(vID, ''.join(['B', str(x)])))
            elif x <= 24:
                self.broadsideBattery.append(double_A5_LaserLance(vID, ''.join(['B', str(x)])))
        HoodClass.ammount += 1

#Prince of Wales Class Battleship
class PrinceOfWalesClass(Battleship):
    ammount = 0
    shipStats = {
        "FP": 654, "ACC": 36, "EVA": 29, "SPD": 25,
        "armor": 3, "luck": 10
    }

    shields = 42800 
    hull = 18500

    def __init__(self, hullnumber, name):
        super().__init__(hullnumber, name)
        vID = self.vesselID
        self.defenses['ShieldType'].append(DarkEnergyShieldGen(vID))
        self.defenses['ArmorType'].append(DurasteelArmor(vID))
        self.primaryBattery = []
        for x in range(1, 5):
            if x <= 2:
                self.primaryBattery.append(double_M22_ThorGigaGuns(vID, ''.join(['T', str(x)])))
            elif x <= 4:
                self.primaryBattery.append(quadruple_M22_ThorGigaGuns(vID, ''.join(['T', str(x)])))
        self.secondaryBattery = [triple_L13_HadronLance(vID, ''.join(['S', str(x)])) for x in range(1,5)]
        self.broadsideBattery = []
        for x in range(1, 25):
            if x <= 16:
                self.broadsideBattery.append(double_M6_TitanAutoCannons(vID, ''.join(['B', str(x)])))
            elif x <= 24:
                self.broadsideBattery.append(double_A5_LaserLance(vID, ''.join(['B', str(x)])))
        
        PrinceOfWalesClass.ammount += 1  

#New Jersey Class Battleship
class NewJerseyClass(Battleship):
    ammount = 0 
    shipStats = {
        "FP": 888, "ACC": 48, "EVA": 34, "SPD": 28,
        "armor": 3.3, "luck": 10
    }

    shields = 66200
    hull = 25250

    def __init__(self, hullnumber, name):
        super().__init__(hullnumber, name)
        vID = self.vesselID
        self.defenses['ShieldType'].append(DarkEnergyShieldGen(vID))
        self.defenses['ArmorType'].append(DarkNeutronianArmor(vID))
        self.primaryBattery = []
        for x in range(1, 5):
            if x <= 2:
                self.primaryBattery.append(quadruple_M22_ThorGigaGuns(vID, ''.join(['T', str(x)])))
            elif x <= 4:
                self.primaryBattery.append(triple_M26_ZeusCannons(vID, ''.join(['T', str(x)])))
        self.secondaryBattery = []
        for x in range(1,7):
            if x <= 2:
                self.secondaryBattery.append(quadruple_M12_NeutronLauchers(vID, ''.join(['S', str(x)])))
            elif x <= 6:
                self.secondaryBattery.append(triple_L13_HadronLance(vID, ''.join(['S', str(x)])))
        self.broadsideBattery = []
        for x in range(1, 33):
            if x <= 20:
                self.broadsideBattery.append(double_M6_TitanAutoCannons(vID, ''.join(['B', str(x)])))
            elif x <= 32:
                self.broadsideBattery.append(double_A5_LaserLance(vID, ''.join(['B', str(x)])))   

        NewJerseyClass.ammount += 1    
