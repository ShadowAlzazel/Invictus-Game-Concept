from shipClasses.shipEquipment import *
from shipClasses.shipRole import Battleship

#BATTLESHIPS

#---------------------------Essex Class Battleship---------------------------
class EssexClass(Battleship):
    shipClass = 'EssexClass'
    ammount = 0
    shipStats = {
        "FP": 666, "ACC": 38, "EVA": 30, "SPD": 4,
        "RDR": 7, "LCK": 10
    }

    shields = 46600 
    hull = 18800

    def __init__(self, hullnumber, name):
        super().__init__(hullnumber, name)
        EssexClass.ammount += 1
        vID = self.vesselID
        self.radar = shipHexRadar(vID, self.shipStats['RDR'])
        self.defenses['shieldType'].append(DarkEnergyShieldGen(vID))
        self.defenses['armorType'].append(DurasteelArmor(vID))
        self.armaments['primaryBattery'] = [triple_M22_GigaRailCannons(vID, ''.join(['T', str(x)])) for x in range(1,5)]
        self.armaments['secondaryBattery'] = [triple_L13_HadronLance(vID, ''.join(['S', str(x)])) for x in range(1,5)]
        for x in range(1, 25):
            if x <= 16:
                self.armaments['broadsideBattery'].append(double_M6_TitanAutoCannons(vID, ''.join(['B', str(x)])))
            elif x <= 24:
                self.armaments['broadsideBattery'].append(double_L6_ParticleLance(vID, ''.join(['B', str(x)])))
        

#---------------------------Amagi Class Battleship---------------------------
class AmagiClass(Battleship):
    shipClass = 'AmagiClass'
    ammount = 0
    shipStats = {
        "FP": 682, "ACC": 37, "EVA": 31, "SPD": 4,
        "RDR": 6, "LCK": 10
    }

    shields = 43200 
    hull = 16800
    
    def __init__(self, hullnumber, name):
        super().__init__(hullnumber, name)
        AmagiClass.ammount += 1
        vID = self.vesselID
        self.radar = shipHexRadar(vID, self.shipStats['RDR'])
        self.defenses['shieldType'].append(DarkEnergyShieldGen(vID))
        self.defenses['armorType'].append(DurasteelArmor(vID))
        self.armaments['primaryBattery'] = [double_M22_GigaRailCannons(vID, ''.join(['T', str(x)])) for x in range(1,7)]
        self.armaments['secondaryBattery'] = [triple_L13_HadronLance(vID, ''.join(['S', str(x)])) for x in range(1,5)]
        for x in range(1, 25):
            if x <= 16:
                self.armaments['broadsideBattery'].append(double_M6_TitanAutoCannons(vID, ''.join(['B', str(x)])))
            elif x <= 24:
                self.armaments['broadsideBattery'].append(double_L6_ParticleLance(vID, ''.join(['B', str(x)])))
    

#---------------------------Vittorio Veneto Class Battleship---------------------------
class VittorioVenetoClass(Battleship):
    shipClass = 'VittorioVenetoClass'
    ammount = 0
    shipStats = {
        "FP": 660, "ACC": 35, "EVA": 30, "SPD": 4,
        "RDR": 6, "LCK": 10
    }

    shields = 42100 
    hull = 18400

    def __init__(self, hullnumber, name):
        super().__init__(hullnumber, name)
        VittorioVenetoClass.ammount += 1
        vID = self.vesselID
        self.radar = shipHexRadar(vID, self.shipStats['RDR'])
        self.defenses['shieldType'].append(DarkEnergyShieldGen(vID))
        self.defenses['armorType'].append(DurasteelArmor(vID))
        self.armaments['primaryBattery'] = [triple_M22_GigaRailCannons(vID, ''.join(['T', str(x)])) for x in range(1,5)]
        self.armaments['secondaryBattery'] = [triple_L13_HadronLance(vID, ''.join(['S', str(x)])) for x in range(1,5)]
        for x in range(1, 25):
            if x <= 16:
                self.armaments['broadsideBattery'].append(double_M6_TitanAutoCannons(vID, ''.join(['B', str(x)])))
            elif x <= 24:
                self.armaments['broadsideBattery'].append(double_L6_ParticleLance(vID, ''.join(['B', str(x)])))


#--------------------------Hood Class Battleship---------------------------
class HoodClass(Battleship):
    shipClass = 'HoodClass'
    ammount = 0
    shipStats = {
        "FP": 685, "ACC": 37, "EVA": 30, "SPD": 4,
        "RDR": 6, "LCK": 10
    }

    shields = 45300 
    hull = 17600
    
    def __init__(self, hullnumber, name):
        super().__init__(hullnumber, name)
        HoodClass.ammount += 1
        vID = self.vesselID
        self.radar = shipHexRadar(vID, self.shipStats['RDR'])
        self.defenses['shieldType'].append(DarkEnergyShieldGen(vID))
        self.defenses['armorType'].append(DurasteelArmor(vID))
        self.armaments['primaryBattery'] = [double_M22_GigaRailCannons(vID, ''.join(['T', str(x)])) for x in range(1,7)]
        self.armaments['secondaryBattery'] = [triple_L13_HadronLance(vID, ''.join(['S', str(x)])) for x in range(1,5)]
        for x in range(1, 25):
            if x <= 16:
                self.armaments['broadsideBattery'].append(double_M6_TitanAutoCannons(vID, ''.join(['B', str(x)])))
            elif x <= 24:
                self.armaments['broadsideBattery'].append(double_L6_ParticleLance(vID, ''.join(['B', str(x)])))


#--------------------------Prince of Wales Class Battleship---------------------------
class PrinceOfWalesClass(Battleship):
    shipClass = 'PrinceOfWalesClass'
    ammount = 0
    shipStats = {
        "FP": 654, "ACC": 36, "EVA": 29, "SPD": 4,
        "RDR": 6, "LCK": 10
    }

    shields = 42800 
    hull = 18500

    def __init__(self, hullnumber, name):
        super().__init__(hullnumber, name)
        PrinceOfWalesClass.ammount += 1
        vID = self.vesselID
        self.radar = shipHexRadar(vID, self.shipStats['RDR'])
        self.defenses['shieldType'].append(DarkEnergyShieldGen(vID))
        self.defenses['armorType'].append(DurasteelArmor(vID))
        for x in range(1, 5):
            if x <= 2:
                self.armaments['primaryBattery'].append(double_M22_GigaRailCannons(vID, ''.join(['T', str(x)])))
            elif x <= 4:
                self.armaments['primaryBattery'].append(quadruple_M22_GigaRailCannons(vID, ''.join(['T', str(x)])))
        self.armaments['secondaryBattery'] = [triple_L13_HadronLance(vID, ''.join(['S', str(x)])) for x in range(1,5)]
        for x in range(1, 25):
            if x <= 16:
                self.armaments['broadsideBattery'].append(double_M6_TitanAutoCannons(vID, ''.join(['B', str(x)])))
            elif x <= 24:
                self.armaments['broadsideBattery'].append(double_L6_ParticleLance(vID, ''.join(['B', str(x)])))
          

#--------------------------New Jersey Class Battleship-----------------------------
class NewJerseyClass(Battleship):
    shipClass = 'NewJerseyClass'
    ammount = 0 
    shipStats = {
        "FP": 888, "ACC": 48, "EVA": 34, "SPD": 4,
        "RDR": 8, "LCK": 10
    }

    shields = 66200
    hull = 25250

    def __init__(self, hullnumber, name):
        super().__init__(hullnumber, name)
        NewJerseyClass.ammount += 1 
        vID = self.vesselID
        self.radar = shipHexRadar(vID, self.shipStats['RDR'])
        self.defenses['shieldType'].append(DarkEnergyShieldGen(vID))
        self.defenses['armorType'].append(DarkNeutronianArmor(vID))
        for x in range(1, 5):
            if x <= 2:
                self.armaments['primaryBattery'].append(quadruple_M22_GigaRailCannons(vID, ''.join(['T', str(x)])))
            elif x <= 4:
                self.armaments['primaryBattery'].append(triple_M26_ZeusCannons(vID, ''.join(['T', str(x)])))

        for x in range(1,7):
            if x <= 2:
                self.armaments['secondaryBattery'].append(quadruple_M12_GaussCannons(vID, ''.join(['S', str(x)])))
            elif x <= 6:
                self.armaments['secondaryBattery'].append(triple_L13_HadronLance(vID, ''.join(['S', str(x)])))
        for x in range(1, 33):
            if x <= 20:
                self.armaments['broadsideBattery'].append(double_M6_TitanAutoCannons(vID, ''.join(['B', str(x)])))
            elif x <= 32:
                self.armaments['broadsideBattery'].append(double_L6_ParticleLance(vID, ''.join(['B', str(x)])))   