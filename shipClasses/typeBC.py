from shipClasses.shipEquipment import *
from shipClasses.shipRole import Battlecruiser

#BattleCruisers

#----------------------------Zenith Class Battlecruiser--------------------------------
class ZenithClass(Battlecruiser):
    shipClass = 'ZenithClass' 
    ammount = 0
    shipStats = {       
        "FP": 493, "ACC": 47, "EVA": 37, "SPD": 5,
        "RDR": 5, "LCK": 10
    }

    shields = 27500
    hull = 11700

    def __init__(self, hullnumber, name):
        super().__init__(hullnumber, name)
        ZenithClass.ammount += 1
        vID = self.vesselID
        self.radar = shipHexRadar(vID, self.shipStats['RDR'])
        self.defenses['shieldType'].append(DarkEnergyShieldGen(vID))
        self.defenses['armorType'].append(MythrilAlloyArmor(vID))
        for x in range(1, 6):
            if x <= 3:
                self.armaments['primaryBattery'].append(double_A17_HAT3ArcThrowers(vID, ''.join(['T', str(x)])))
            else:
                self.armaments['primaryBattery'].append(triple_L18_DeuteriumLance(vID, ''.join(['T', str(x)])))
        for x in range(1,6):
            if x <= 2:
                self.armaments['secondaryBattery'].append(quadruple_M12_GaussCannons(vID, ''.join(['S', str(x)])))
            elif x <= 4:
                self.armaments['secondaryBattery'].append(triple_A11_TeslaArcThrowers(vID, ''.join(['S', str(x)])))
            else: 
                 self.armaments['secondaryBattery'].append(triple_L13_HadronLance(vID, ''.join(['S', str(x)])))
        for x in range(1, 17):
            if x <= 8:
                self.armaments['broadsideBattery'].append(double_M6_TitanAutoCannons(vID, ''.join(['B', str(x)])))
            else:
                self.armaments['broadsideBattery'].append(double_L6_ParticleLance(vID, ''.join(['B', str(x)])))


#-----------------------------Eclipse Class Battlecruiser-------------------------
class EclipseClass(Battlecruiser):
    shipClass = 'EclipseClass' 
    ammount = 0
    shipStats = {       
        "FP": 517, "ACC": 45, "EVA": 35, "SPD": 5,
        "RDR": 5, "LCK": 10
    }

    shields = 25600
    hull = 13800

    def __init__(self, hullnumber, name):
        super().__init__(hullnumber, name)
        EclipseClass.ammount += 1
        vID = self.vesselID
        self.radar = shipHexRadar(vID, self.shipStats['RDR'])
        self.defenses['shieldType'].append(DarkEnergyShieldGen(vID))
        self.defenses['armorType'].append(MythrilAlloyArmor(vID))
        for x in range(1, 5):
            if x <= 2:
                self.armaments['primaryBattery'].append(triple_L18_DeuteriumLance(vID, ''.join(['T', str(x)])))
            else:
                self.armaments['primaryBattery'].append(double_M22_GigaRailCannons(vID, ''.join(['T', str(x)])))
        self.armaments['secondaryBattery'] = [quadruple_M12_GaussCannons(vID, ''.join(['S', str(x)])) for x in range(1,5)]
        for x in range(1, 17):
            if x <= 8:
                self.armaments['broadsideBattery'].append(double_L6_ParticleLance(vID, ''.join(['B', str(x)])))
            elif x <= 12:
                self.armaments['broadsideBattery'].append(double_A5_ArcThrowers(vID, ''.join(['B', str(x)])))
            else:
                self.armaments['broadsideBattery'].append(double_M6_TitanAutoCannons(vID, ''.join(['B', str(x)])))
        

#--------------------------------Penumbra Class Battlecruiser------------------------------------
class PenumbraClass(Battlecruiser):
    shipClass = 'PenumbraClass'
    ammount = 0
    shipStats = {       
        "FP": 545, "ACC": 48, "EVA": 35, "SPD": 5,
        "RDR": 5, "LCK": 10
    }

    shields = 23500
    hull = 14500

    def __init__(self, hullnumber, name):
        super().__init__(hullnumber, name)
        PenumbraClass.ammount += 1
        vID = self.vesselID
        self.radar = shipHexRadar(vID, self.shipStats['RDR'])
        self.defenses['shieldType'].append(DarkEnergyShieldGen(vID))
        self.defenses['armorType'].append(MythrilAlloyArmor(vID))
        for x in range(1, 5):
            if x <= 4:
                self.armaments['primaryBattery'].append(double_F20_MatterDisentegrators(vID, ''.join(['T', str(x)])))
            else:
                self.armaments['primaryBattery'].append(double_L18_DeuteriumLance(vID, ''.join(['T', str(x)])))
        self.armaments['secondaryBattery'] = [triple_L13_HadronLance(vID, ''.join(['S', str(x)])) for x in range(1,3)]
        for x in range(1, 17):
            if x <= 8:
                self.armaments['broadsideBattery'].append(double_M6_TitanAutoCannons(vID, ''.join(['B', str(x)])))
            else:
                self.armaments['broadsideBattery'].append(double_L6_ParticleLance(vID, ''.join(['B', str(x)])))


#---------------------------Illustrious Class Battlecruiser--------------------------------------
class IllustriousClass(Battlecruiser):
    shipClass = 'IllustriousClass'
    ammount = 0
    shipStats = {       
        "FP": 523, "ACC": 46, "EVA": 32, "SPD": 5,
        "RDR": 5, "LCK": 10
    }

    shields = 26600
    hull = 16600

    def __init__(self, hullnumber, name):
        IllustriousClass.ammount += 1
        super().__init__(hullnumber, name)
        vID = self.vesselID
        self.radar = shipHexRadar(vID, self.shipStats['RDR'])
        self.defenses['shieldType'].append(DarkEnergyShieldGen(vID))
        self.defenses['armorType'].append(MythrilAlloyArmor(vID))
        self.armaments['primaryBattery'] = [triple_L18_DeuteriumLance(vID, ''.join(['T', str(x)])) for x in range(1,5)]
        self.armaments['secondaryBattery'] = [quadruple_M12_GaussCannons(vID, ''.join(['S', str(x)])) for x in range(1,5)]
        for x in range(1, 17):
            if x <= 8:
                self.armaments['broadsideBattery'].append(double_M6_TitanAutoCannons(vID, ''.join(['B', str(x)])))
            elif x <= 16:
                self.armaments['broadsideBattery'].append(double_L6_ParticleLance(vID, ''.join(['B', str(x)])))
