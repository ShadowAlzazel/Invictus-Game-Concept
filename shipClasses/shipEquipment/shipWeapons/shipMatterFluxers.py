#matter fluxers
from shipClasses.shipEquipment.shipWeapons.weaponEntity import shipWeapon

#"""--<->----------------------------MATTER-FLUXERS------------------------------<->--"""
#disentegrates matter by exciting quantum fields in focused dimensional beams  
#The higgs field is excited and starts to discharge, causing mass to leave the dimension.

class double_F20_MatterDisentegrators(shipWeapon):
    gun_name = 'Double (F20) Matter Disentegrators'
    gun_stats = {
        "ATK": 1285, "RLD": 4, "HIT": 75, "RNG": 2, "QNT": 2, "PEN": 3, "DIS": 0.5
    }
    def __init__(self, vessel_ID, battery_turret_number):
        super().__init__(vessel_ID, battery_turret_number) 


class double_F14_MatterErasers(shipWeapon):
    gun_name = 'Double (F14) Matter Erasers'
    gun_stats = {
        "ATK": 775, "RLD": 4, "HIT": 75, "RNG": 2, "QNT": 2, "PEN": 3, "DIS": 0.5
    }
    def __init__(self, vessel_ID, battery_turret_number):
        super().__init__(vessel_ID, battery_turret_number) 


class double_F8_MatterFluxers(shipWeapon):
    gun_name = 'Double (F8) Matter Fluxers'
    gun_stats = {
        "ATK": 396, "RLD": 4, "HIT": 75, "RNG": 2, "QNT": 2, "PEN": 3, "DIS": 0.5
    }
    def __init__(self, vessel_ID, battery_turret_number):
        super().__init__(vessel_ID, battery_turret_number) 
