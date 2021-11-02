#Started 10/24/2021
from shipTypes import *
from shipArmaments import *

"""--<->----------------------------BATTLESHIPS------------------------------<->--"""

#Essex Class Battleship
class EssexClass(Battleship):
    ammount = 0
    shipStats = {
        "FP": 445, "ACC": 43, "EVA": 30, "SPD": 25,
        "armor": 3.2, "luck": 10
    }

    shields = 15500
    hull = 12000

    def __init__(self, hullnumber, name):
        super().__init__(hullnumber, name)
        vID = self.vesselID

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
        "FP": 425, "ACC": 44, "EVA": 31, "SPD": 27,
        "armor": 3.2, "luck": 10
    }

    shields = 14000
    hull = 13500
    
    def __init__(self, hullnumber, name):
        super().__init__(hullnumber, name)
        vID = self.vesselID

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
        "FP": 433, "ACC": 43, "EVA": 29, "SPD": 24,
        "armor": 3.2, "luck": 10
    }

    shields = 12500
    hull = 13000

    def __init__(self, hullnumber, name):
        super().__init__(hullnumber, name)
        vID = self.vesselID

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
        "FP": 424, "ACC": 46, "EVA": 31, "SPD": 27,
        "armor": 3.2, "luck": 10
    }

    shields = 12800
    hull = 11700
    
    def __init__(self, hullnumber, name):
        super().__init__(hullnumber, name)
        vID = self.vesselID

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
        "FP": 444, "ACC": 44, "EVA": 30, "SPD": 26,
        "armor": 3.2, "luck": 10
    }

    shields = 13200
    hull = 12500

    def __init__(self, hullnumber, name):
        super().__init__(hullnumber, name)
        vID = self.vesselID

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
        "FP": 488, "ACC": 48, "EVA": 34, "SPD": 28,
        "armor": 3.3, "luck": 10
    }

    shields = 16200
    hull = 15250

    def __init__(self, hullnumber, name):
        super().__init__(hullnumber, name)
        vID = self.vesselID

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

"""--<->----------------------------BATTLECRUISERS------------------------------<->--"""

#Zenith Class Battlecruiser
class ZenithClass(Battlecruiser):
    ammount = 0
    shipStats = {
        "FP": 297, "ACC": 50, "EVA": 35, "SPD": 30,
        "armor": 3, "luck": 10
    }

    shields = 8700
    hull = 8550

    def __init__(self, hullnumber, name):
        super().__init__(hullnumber, name)
        vID = self.vesselID

        self.primaryBattery = []
        for x in range(1, 6):
            if x <= 3:
                self.primaryBattery.append(double_A17_HAT3ArcThrowers(vID, ''.join(['T', str(x)])))
            elif x <= 5:
                self.primaryBattery.append(triple_L18_DeuteriumLance(vID, ''.join(['T', str(x)])))
        self.secondaryBattery = []
        for x in range(1,6):
            if x <= 2:
                self.secondaryBattery.append(quadruple_M12_NeutronLauchers(vID, ''.join(['S', str(x)])))
            elif x <= 4:
                self.secondaryBattery.append(triple_A11_TeslaArcThrowers(vID, ''.join(['S', str(x)])))
            elif x <= 5: 
                 self.secondaryBattery.append(triple_L13_HadronLance(vID, ''.join(['S', str(x)])))
        self.broadsideBattery = []
        for x in range(1, 17):
            if x <= 8:
                self.broadsideBattery.append(double_M6_TitanAutoCannons(vID, ''.join(['B', str(x)])))
            elif x <= 16:
                self.broadsideBattery.append(double_A5_LaserLance(vID, ''.join(['B', str(x)])))

        ZenithClass.ammount += 1

#Eclipse Class Battlecruiser
class EclipseClass(Battlecruiser):
    ammount = 0
    shipStats = {
        "FP": 287, "ACC": 49, "EVA": 38, "SPD": 31,
        "armor": 3, "luck": 10
    }

    shields = 9400
    hull = 8250

    def __init__(self, hullnumber, name):
        super().__init__(hullnumber, name)
        vID = self.vesselID

        self.primaryBattery = []
        for x in range(1, 5):
            if x <= 2:
                self.primaryBattery.append(triple_L18_DeuteriumLance(vID, ''.join(['T', str(x)])))
            elif x <= 4:
                self.primaryBattery.append(double_M22_ThorGigaGuns(vID, ''.join(['T', str(x)])))
        self.secondaryBattery = [quadruple_M12_NeutronLauchers(vID, ''.join(['S', str(x)])) for x in range(1,5)]
        self.broadsideBattery = []
        for x in range(1, 17):
            if x <= 8:
                self.broadsideBattery.append(double_A5_LaserLance(vID, ''.join(['B', str(x)])))
            elif x <= 12:
                self.broadsideBattery.append(double_A5_WaveArcThrowers(vID, ''.join(['B', str(x)])))
            elif x <= 16:
                self.broadsideBattery.append(double_M6_TitanAutoCannons(vID, ''.join(['B', str(x)])))
        
        EclipseClass.ammount += 1

#Penumbra Class Battlecruiser
class PenumbraClass(Battlecruiser):
    ammount = 0
    shipStats = {
        "FP": 321, "ACC": 49, "EVA": 36, "SPD": 30,
        "armor": 3, "luck": 10
    }

    shields = 8800
    hull = 8470

    def __init__(self, hullnumber, name):
        super().__init__(hullnumber, name)
        vID = self.vesselID

        self.primaryBattery = [double_L18_DeuteriumLance(vID, ''.join(['T', str(x)])) for x in range(1,7)]
        self.secondaryBattery = [quadruple_M12_NeutronLauchers(vID, ''.join(['S', str(x)])) for x in range(1,3)]
        self.broadsideBattery = []
        for x in range(1, 17):
            if x <= 8:
                self.broadsideBattery.append(double_M6_TitanAutoCannons(vID, ''.join(['B', str(x)])))
            elif x <= 16:
                self.broadsideBattery.append(double_A5_LaserLance(vID, ''.join(['B', str(x)])))

        PenumbraClass.ammount += 1

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
        vID = self.vesselID

        self.primaryBattery = []
        for x in range(1, 5):
            if x <= 2:
                self.primaryBattery.append(triple_L13_HadronLance(vID, ''.join(['T', str(x)])))
            elif x <= 4:
                self.primaryBattery.append(triple_A11_TeslaArcThrowers(vID, ''.join(['T', str(x)])))
        self.secondaryBattery = [triple_M7_TitanAutoCannons(vID, ''.join(['S', str(x)])) for x in range(1,3)]
        self.broadsideBattery = []
        for x in range(1, 9):
            if x <= 4:
                self.broadsideBattery.append(double_M4_ShredderAutoGuns(vID, ''.join(['B', str(x)])))
            elif x <= 8:
                self.broadsideBattery.append(double_A5_LaserLance(vID, ''.join(['B', str(x)])))

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
        vID = self.vesselID
        
        self.primaryBattery = []
        for x in range(1, 5):
            if x <= 2:
                self.primaryBattery.append(triple_M12_NeutronLauchers(vID, ''.join(['T', str(x)])))
            elif x <= 4:
                self.primaryBattery.append(triple_A11_TeslaArcThrowers(vID, ''.join(['T', str(x)])))
        self.secondaryBattery = [triple_A6_LaserLance(vID, ''.join(['S', str(x)])) for x in range(1,3)]
        self.broadsideBattery = []
        for x in range(1, 9):
            if x <= 4:
                self.broadsideBattery.append(double_M4_ShredderAutoGuns(vID, ''.join(['B', str(x)])))
            elif x <= 8:
                self.broadsideBattery.append(double_A5_WaveArcThrowers(vID, ''.join(['B', str(x)])))

        DynamoClass.ammount += 1

"""--<->----------------------------HEAVYCRUISERS------------------------------<->--"""

#Apocalypse Class Heavycrusier
class ApocalypseClass(Heavycruiser):
    ammount = 0
    shipStats = {
        "FP": 215, "ACC": 36, "EVA": 32, "SPD": 26,
        "armor": 2.5, "luck": 10
    }
    
    shields = 7660
    hull = 7700

    def __init__(self, hullnumber, name):
        super().__init__(hullnumber, name)
        vID = self.vesselID

        self.primaryBattery = [triple_M12_NeutronLauchers(vID, ''.join(['T', str(x)])) for x in range(1,6)]
        self.secondaryBattery = [triple_M7_TitanAutoCannons(vID, ''.join(['S', str(x)])) for x in range(1,4)] 
        self.broadsideBattery = []
        for x in range(1, 11):
            if x <= 8:
                self.broadsideBattery.append(double_M6_TitanAutoCannons(vID, ''.join(['B', str(x)])))
            elif x <= 10:
                self.broadsideBattery.append(double_A5_LaserLance(vID, ''.join(['B', str(x)])))

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
        vID = self.vesselID
        self.primaryBattery = [double_M6_TitanAutoCannons(vID, 'T1'), double_M4_ShredderAutoGuns(vID, 'T2')]
        self.secondaryBattery = []
        self.broadsideBattery = []

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
        vID = self.vesselID
        self.primaryBattery = [double_M6_TitanAutoCannons(vID, 'T1'), double_M4_ShredderAutoGuns(vID, 'T2')]
        self.secondaryBattery = []
        self.broadsideBattery = []

        ShimakazeClass.ammount += 1