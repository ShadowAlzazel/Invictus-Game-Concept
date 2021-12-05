from shipClasses.shipEquipment import *
from shipClasses.shipRole import Battleship

#BATTLESHIPS

#---------------------------Essex Class Battleship---------------------------
class EssexClass(Battleship):
    shipClass = 'EssexClass'
    ammount = 0
    ship_stats = {
        "FP": 666, "ACC": 38, "EVA": 30, "SPD": 4,
        "RDR": 7, "LCK": 10, "STH": 0
    }

    shields = 46600 
    hull = 18800

    def __init__(self, hullnumber, name):
        super().__init__(hullnumber, name)
        EssexClass.ammount += 1
        vID = self.vessel_ID
        self.radar = hex_radar(vID, self.ship_stats['RDR'])
        self.defenses['shield_gen'].append(DarkMatterShieldGen(vID))
        self.defenses['armor_type'].append(AdamantiumAlloyArmor(vID))
        self.armaments['primary_battery'] = [triple_M22_GigaRailCannons(vID, ''.join(['T', str(x)])) for x in range(1,5)]
        self.armaments['secondary_battery'] = [triple_L13_HadronLance(vID, ''.join(['S', str(x)])) for x in range(1,5)]
        for x in range(1, 25):
            if x <= 16:
                self.armaments['broadside_battery'].append(double_M6_TitanAutoCannons(vID, ''.join(['B', str(x)])))
            else:
                self.armaments['broadside_battery'].append(double_L6_ParticleLance(vID, ''.join(['B', str(x)])))
        

#---------------------------Amagi Class Battleship---------------------------
class AmagiClass(Battleship):
    shipClass = 'AmagiClass'
    ammount = 0
    ship_stats = {
        "FP": 682, "ACC": 37, "EVA": 31, "SPD": 4,
        "RDR": 6, "LCK": 10, "STH": 0
    }

    shields = 43200 
    hull = 16800
    
    def __init__(self, hullnumber, name):
        super().__init__(hullnumber, name)
        AmagiClass.ammount += 1
        vID = self.vessel_ID
        self.radar = hex_radar(vID, self.ship_stats['RDR'])
        self.defenses['shield_gen'].append(DarkMatterShieldGen(vID))
        self.defenses['armor_type'].append(AdamantiumAlloyArmor(vID))
        self.armaments['primary_battery'] = [double_M22_GigaRailCannons(vID, ''.join(['T', str(x)])) for x in range(1,7)]
        self.armaments['secondary_battery'] = [triple_L13_HadronLance(vID, ''.join(['S', str(x)])) for x in range(1,5)]
        for x in range(1, 25):
            if x <= 16:
                self.armaments['broadside_battery'].append(double_M6_TitanAutoCannons(vID, ''.join(['B', str(x)])))
            else:
                self.armaments['broadside_battery'].append(double_L6_ParticleLance(vID, ''.join(['B', str(x)])))
    

#---------------------------Vittorio Veneto Class Battleship---------------------------
class VittorioVenetoClass(Battleship):
    shipClass = 'VittorioVenetoClass'
    ammount = 0
    ship_stats = {
        "FP": 660, "ACC": 35, "EVA": 30, "SPD": 4,
        "RDR": 6, "LCK": 10, "STH": 0
    }

    shields = 42100 
    hull = 18400

    def __init__(self, hullnumber, name):
        super().__init__(hullnumber, name)
        VittorioVenetoClass.ammount += 1
        vID = self.vessel_ID
        self.radar = hex_radar(vID, self.ship_stats['RDR'])
        self.defenses['shield_gen'].append(DarkMatterShieldGen(vID))
        self.defenses['armor_type'].append(AdamantiumAlloyArmor(vID))
        self.armaments['primary_battery'] = [triple_M22_GigaRailCannons(vID, ''.join(['T', str(x)])) for x in range(1,5)]
        self.armaments['secondary_battery'] = [triple_L13_HadronLance(vID, ''.join(['S', str(x)])) for x in range(1,5)]
        for x in range(1, 25):
            if x <= 16:
                self.armaments['broadside_battery'].append(double_M6_TitanAutoCannons(vID, ''.join(['B', str(x)])))
            else:
                self.armaments['broadside_battery'].append(double_L6_ParticleLance(vID, ''.join(['B', str(x)])))


#--------------------------Hood Class Battleship---------------------------
class HoodClass(Battleship):
    shipClass = 'HoodClass'
    ammount = 0
    ship_stats = {
        "FP": 685, "ACC": 37, "EVA": 30, "SPD": 4,
        "RDR": 6, "LCK": 10, "STH": 0
    }

    shields = 45300 
    hull = 17600
    
    def __init__(self, hullnumber, name):
        super().__init__(hullnumber, name)
        HoodClass.ammount += 1
        vID = self.vessel_ID
        self.radar = hex_radar(vID, self.ship_stats['RDR'])
        self.defenses['shield_gen'].append(DarkMatterShieldGen(vID))
        self.defenses['armor_type'].append(AdamantiumAlloyArmor(vID))
        self.armaments['primary_battery'] = [double_P22_PulsarPhasers(vID, ''.join(['T', str(x)])) for x in range(1,7)]
        self.armaments['secondary_battery'] = [triple_L13_HadronLance(vID, ''.join(['S', str(x)])) for x in range(1,5)]
        for x in range(1, 25):
            if x <= 16:
                self.armaments['broadside_battery'].append(double_M6_TitanAutoCannons(vID, ''.join(['B', str(x)])))
            else:
                self.armaments['broadside_battery'].append(double_P6_PlasmaPhasers(vID, ''.join(['B', str(x)])))


#--------------------------Prince of Wales Class Battleship---------------------------
class PrinceOfWalesClass(Battleship):
    shipClass = 'PrinceOfWalesClass'
    ammount = 0
    ship_stats = {
        "FP": 704, "ACC": 35, "EVA": 29, "SPD": 4,
        "RDR": 6, "LCK": 10, "STH": 0
    }

    shields = 42800 
    hull = 18500

    def __init__(self, hullnumber, name):
        super().__init__(hullnumber, name)
        PrinceOfWalesClass.ammount += 1
        vID = self.vessel_ID
        self.radar = hex_radar(vID, self.ship_stats['RDR'])
        self.defenses['shield_gen'].append(DarkMatterShieldGen(vID))
        self.defenses['armor_type'].append(AdamantiumAlloyArmor(vID))
        for x in range(1, 5):
            if x <= 2:
                self.armaments['primary_battery'].append(double_M22_GigaRailCannons(vID, ''.join(['T', str(x)])))
            else:
                self.armaments['primary_battery'].append(quadruple_M22_GigaRailCannons(vID, ''.join(['T', str(x)])))
        self.armaments['secondary_battery'] = [triple_L13_HadronLance(vID, ''.join(['S', str(x)])) for x in range(1,5)]
        for x in range(1, 25):
            if x <= 16:
                self.armaments['broadside_battery'].append(double_M6_TitanAutoCannons(vID, ''.join(['B', str(x)])))
            else:
                self.armaments['broadside_battery'].append(double_P6_PlasmaPhasers(vID, ''.join(['B', str(x)])))
          

#--------------------------New Jersey Class Battleship-----------------------------
class NewJerseyClass(Battleship):
    shipClass = 'NewJerseyClass'
    ammount = 0 
    ship_stats = {
        "FP": 888, "ACC": 38, "EVA": 28, "SPD": 4,
        "RDR": 7, "LCK": 10, "STH": 0
    }

    shields = 66200
    hull = 25250

    def __init__(self, hullnumber, name):
        super().__init__(hullnumber, name)
        NewJerseyClass.ammount += 1 
        vID = self.vessel_ID
        self.radar = hex_radar(vID, self.ship_stats['RDR'])
        self.defenses['shield_gen'].append(DarkMatterShieldGen(vID))
        self.defenses['armor_type'].append(DarkNeutroniumArmor(vID))
        for x in range(1, 5):
            if x <= 2:
                self.armaments['primary_battery'].append(quadruple_M22_GigaRailCannons(vID, ''.join(['T', str(x)])))
            else:
                self.armaments['primary_battery'].append(triple_M26_ZeusCannons(vID, ''.join(['T', str(x)])))
        for x in range(1,7):
            if x <= 2:
                self.armaments['secondary_battery'].append(quadruple_M12_GaussCannons(vID, ''.join(['S', str(x)])))
            else:
                self.armaments['secondary_battery'].append(triple_L13_HadronLance(vID, ''.join(['S', str(x)])))
        for x in range(1, 33):
            if x <= 20:
                self.armaments['broadside_battery'].append(double_M6_TitanAutoCannons(vID, ''.join(['B', str(x)])))
            else:
                self.armaments['broadside_battery'].append(double_L6_ParticleLance(vID, ''.join(['B', str(x)])))   

    
#--------------------------Devestator Class Battleship-----------------------------
class DevestatorClass(Battleship):
    shipClass = 'DevestatorClass'
    ammount = 0 
    ship_stats = {
        "FP": 1013, "ACC": 38, "EVA": 30, "SPD": 4,
        "RDR": 7, "LCK": 10, "STH": 0
    }

    shields = 89400
    hull = 30250

    def __init__(self, hullnumber, name):
        super().__init__(hullnumber, name)
        DevestatorClass.ammount += 1 
        vID = self.vessel_ID
        self.radar = hex_radar(vID, self.ship_stats['RDR'])
        self.defenses['shield_gen'].append(DarkMatterShieldGen(vID))
        self.defenses['armor_type'].append(DarkNeutroniumArmor(vID))
        for x in range(1, 7):
            if x <= 2:
                self.armaments['primary_battery'].append(triple_P24_PulsarPhasers(vID, ''.join(['T', str(x)])))
            else:
                self.armaments['primary_battery'].append(triple_M26_ZeusCannons(vID, ''.join(['T', str(x)])))
        self.armaments['secondary_battery'] = [double_F14_MatterErasers(vID, ''.join(['S', str(x)])) for x in range(1,5)]
        for x in range(1, 49):
            if x <= 20:
                self.armaments['broadside_battery'].append(double_M6_TitanAutoCannons(vID, ''.join(['B', str(x)])))
            elif x < 32:
                self.armaments['broadside_battery'].append(triple_P6_PlasmaPhasers(vID, ''.join(['B', str(x)])))   
            elif x < 40:
                self.armaments['broadside_battery'].append(triple_L6_ParticleLance(vID, ''.join(['B', str(x)])))   
            else: 
                self.armaments['broadside_battery'].append(double_M4_ShredderAutoGuns(vID, ''.join(['B', str(x)])))   
