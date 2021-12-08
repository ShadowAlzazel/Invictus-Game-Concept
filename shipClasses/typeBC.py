from shipClasses.shipEquipment import *
from shipClasses.shipRole import Battlecruiser

#BattleCruisers

#----------------------------Zenith Class Battlecruiser--------------------------------
class ZenithClass(Battlecruiser):
    ship_class = 'ZenithClass' 
    ammount = 0
    ship_stats = {       
        "FP": 493, "ACC": 47, "EVA": 37, "SPD": 5,
        "RDR": 5, "LCK": 10, "STH": 0
    }

    shields = 27500
    hull = 11700

    def __init__(self, hullnumber, name, command, fleet_name):
        super().__init__(hullnumber, name, command, fleet_name)
        ZenithClass.ammount += 1
        vID = self.vessel_ID
        self.radar = hex_radar(vID, self.ship_stats['RDR'])
        self.defenses['shield_gen'].append(HiggsShieldGen(vID))
        self.defenses['armor_type'].append(NeutroniumArmor(vID))
        for x in range(1, 5):
            if x <= 2:
                self.armaments['primary_battery'].append(triple_P18_NovaPhasers(vID, ''.join(['T', str(x)])))
            else:
                self.armaments['primary_battery'].append(triple_L18_DeuteriumLance(vID, ''.join(['T', str(x)])))
        self.armaments['secondary_battery'] = [triple_P12_SolarPhasers(vID, ''.join(['S', str(x)])) for x in range(1,3)]
        for x in range(1, 17):
            if x <= 8:
                self.armaments['broadside_battery'].append(double_M6_TitanAutoCannons(vID, ''.join(['B', str(x)])))
            else:
                self.armaments['broadside_battery'].append(double_L6_ParticleLance(vID, ''.join(['B', str(x)])))


#-----------------------------Eclipse Class Battlecruiser-------------------------
class EclipseClass(Battlecruiser):
    ship_class = 'EclipseClass' 
    ammount = 0
    ship_stats = {       
        "FP": 517, "ACC": 45, "EVA": 35, "SPD": 5,
        "RDR": 5, "LCK": 10, "STH": 0
    }

    shields = 25600
    hull = 13800

    def __init__(self, hullnumber, name, command, fleet_name):
        super().__init__(hullnumber, name, command, fleet_name)
        EclipseClass.ammount += 1
        vID = self.vessel_ID
        self.radar = hex_radar(vID, self.ship_stats['RDR'])
        self.defenses['shield_gen'].append(HiggsShieldGen(vID))
        self.defenses['armor_type'].append(NeutroniumArmor(vID))
        for x in range(1, 5):
            if x <= 2:
                self.armaments['primary_battery'].append(triple_L18_DeuteriumLance(vID, ''.join(['T', str(x)])))
            else:
                self.armaments['primary_battery'].append(double_M22_GigaRailCannons(vID, ''.join(['T', str(x)])))
        self.armaments['secondary_battery'] = [quadruple_M12_GaussCannons(vID, ''.join(['S', str(x)])) for x in range(1,3)]
        for x in range(1, 17):
            if x <= 8:
                self.armaments['broadside_battery'].append(double_M6_TitanAutoCannons(vID, ''.join(['B', str(x)])))
            else:
                self.armaments['broadside_battery'].append(double_P6_PlasmaPhasers(vID, ''.join(['B', str(x)])))


#--------------------------------Penumbra Class Battlecruiser------------------------------------
class PenumbraClass(Battlecruiser):
    ship_class = 'PenumbraClass'
    ammount = 0
    ship_stats = {       
        "FP": 535, "ACC": 48, "EVA": 35, "SPD": 5,
        "RDR": 5, "LCK": 10, "STH": 0
    }

    shields = 23500
    hull = 14500

    def __init__(self, hullnumber, name, command, fleet_name):
        super().__init__(hullnumber, name, command, fleet_name)
        PenumbraClass.ammount += 1
        vID = self.vessel_ID
        self.radar = hex_radar(vID, self.ship_stats['RDR'])
        self.defenses['shield_gen'].append(HiggsShieldGen(vID))
        self.defenses['armor_type'].append(NeutroniumArmor(vID))
        for x in range(1, 5):
            if x <= 4:
                self.armaments['primary_battery'].append(double_F20_MatterDisentegrators(vID, ''.join(['T', str(x)])))
            else:
                self.armaments['primary_battery'].append(double_L18_DeuteriumLance(vID, ''.join(['T', str(x)])))
        self.armaments['secondary_battery'] = [triple_L13_HadronLance(vID, ''.join(['S', str(x)])) for x in range(1,3)]
        for x in range(1, 17):
            if x <= 8:
                self.armaments['broadside_battery'].append(double_M6_TitanAutoCannons(vID, ''.join(['B', str(x)])))
            else:
                self.armaments['broadside_battery'].append(double_L6_ParticleLance(vID, ''.join(['B', str(x)])))


#-----------------------------------Illustrious Class Battlecruiser--------------------------------------
class IllustriousClass(Battlecruiser):
    ship_class = 'IllustriousClass'
    ammount = 0
    ship_stats = {       
        "FP": 513, "ACC": 46, "EVA": 32, "SPD": 5,
        "RDR": 5, "LCK": 10, "STH": 0
    }

    shields = 26600
    hull = 16600

    def __init__(self, hullnumber, name, command, fleet_name):
        IllustriousClass.ammount += 1
        super().__init__(hullnumber, name, command, fleet_name)
        vID = self.vessel_ID
        self.radar = hex_radar(vID, self.ship_stats['RDR'])
        self.defenses['shield_gen'].append(HiggsShieldGen(vID))
        self.defenses['armor_type'].append(NeutroniumArmor(vID))
        self.armaments['primary_battery'] = [triple_L18_DeuteriumLance(vID, ''.join(['T', str(x)])) for x in range(1,5)]
        self.armaments['secondary_battery'] = [triple_A11_TeslaArcThrowers(vID, ''.join(['S', str(x)])) for x in range(1,3)]
        for x in range(1, 17):
            if x <= 8:
                self.armaments['broadside_battery'].append(double_M6_TitanAutoCannons(vID, ''.join(['B', str(x)])))
            elif x <= 16:
                self.armaments['broadside_battery'].append(double_L6_ParticleLance(vID, ''.join(['B', str(x)])))
