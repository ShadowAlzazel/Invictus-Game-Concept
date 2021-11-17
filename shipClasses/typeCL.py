from shipClasses.shipEquipment import *
from shipClasses.shipRole import Lightcruiser

#light cruisers

#-----------------------------------Midnight Class Light Cruiser--------------------------------- 
class MidnightClass(Lightcruiser):
    shipClass = 'MidnightClass'
    ammount = 0 
    shiptype = 'CL'
    shipStats = {
        "FP": 200, "ACC": 35, "EVA": 45, "SPD": 7,
        "RDR": 5, "LCK": 10
    }
    
    shields = 7500
    hull = 7500

    def __init__(self, hullnumber, name):
        MidnightClass.ammount += 1
        super().__init__(hullnumber, name)
        vID = self.vesselID
        self.radar = shipHexRadar(vID, self.shipStats['RDR'])
        self.defenses['shieldType'].append(HyperShieldGen(vID))
        self.defenses['armorType'].append(TitaniumArmor(vID))
        self.armaments['primaryBattery'] = [triple_L6_ParticleLance(vID, ''.join(['T', str(x)])) for x in range(1, 5)]
        self.armaments['secondaryBattery'] = [double_M4_ShredderAutoCannons(vID, ''.join(['S', str(x)])) for x in range(1, 3)] 
        self.armaments['broadsideBattery'] = [quad_BPoDS(vID, ''.join(['S', str(x)])) for x in range(1, 5)]