#shield generators 

#"""---------------------------------SHIELD-OBJECT----------------------------------"""
class shieldGen:
    mitigation_field = 10
    phase_field = 100 #initial shield
    shield_regeneration = 1 #percantage

    def __init__(self, vessel_ID): 
        self.damage_deflected = 0
        self.equipment_ID = '-'.join([vessel_ID, 'SGEN'])

    def take_shield_damage(self, damage_amount, wep_DIS):
        if damage_amount < self.mitigation_field or self.damage_deflected < self.phase_field:
            true_damage = 0  
        else:
            true_damage = damage_amount * wep_DIS
        self.damage_deflected += damage_amount
        return true_damage


#"""-----------------------------------SHIP-SHIELDS-----------------------------------"""
class AdvancedShieldGen(shieldGen):
    shield_name = 'Hyper Shield-Generator'
    mitigation_field = 110
    phase_field = 1800
    shield_regeneration = 0.5

    def __init__(self, vessel_ID):
        super().__init__(vessel_ID)
        

class MegaShieldGen(shieldGen):
    shield_name = 'Mega Shield-Generator'
    mitigation_field = 150
    phase_field = 2200
    shield_regeneration = 0.5

    def __init__(self, vessel_ID):
        super().__init__(vessel_ID)


class GigaShieldGen(shieldGen):
    shield_name = 'Giga Shield-Generator'
    mitigation_field = 200
    phase_field = 2600
    shield_regeneration = 0.5

    def __init__(self, vessel_ID):
        super().__init__(vessel_ID)


class LumioneShieldGen(shieldGen):
    shield_name = 'Lumione Shield-Generator'
    mitigation_field = 30
    phase_field = 550
    shield_regeneration = 1.25
    
    def __init__(self, vessel_ID):
        super().__init__(vessel_ID)


class HyperiumShieldGen(shieldGen):
    shield_name = 'Hyper Shield-Generator'
    mitigation_field = 50
    phase_field = 1100
    shield_regeneration = 2

    def __init__(self, vessel_ID):
        super().__init__(vessel_ID)


class HiggsShieldGen(shieldGen):
    shield_name = 'Higgs Shield-Generator'
    mitigation_field = 70
    phase_field = 1650
    shield_regeneration = 2.825

    def __init__(self, vessel_ID):
        super().__init__(vessel_ID)


class DarkMatterShieldGen(shieldGen):
    shield_name = 'Dark Energy Shield-Generator'
    mitigation_field = 120
    phase_field = 3000
    shield_regeneration = 3.75

    def __init__(self, vessel_ID):
        super().__init__(vessel_ID)