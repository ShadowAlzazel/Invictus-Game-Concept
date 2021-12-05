#matter fluxers
from shipClasses.shipEquipment.shipWeapons.weaponEntity import shipWeapon

#"""--<->----------------------------MATTER-FLUXERS------------------------------<->--"""
#disentegrates matter by exciting quantum fields in focused dimensional beams  
#The higgs field is excited and starts to discharge, causing mass to leave the dimension.

class double_F20_MatterDisentegrators(shipWeapon):
    gunName = 'Double (F20) Matter Disentegrators'
    gun_stats = {
        "ATK": 1285, "RLD": 4, "HIT": 75, "RNG": 2, "QNT": 2, "PEN": 3, "DIS": 0.5
    }
    def __init__(self, vessel_ID, batteryNumber):
        super().__init__(vessel_ID, batteryNumber) 


class double_F14_MatterErasers(shipWeapon):
    gunName = 'Double (F14) Matter Erasers'
    gun_stats = {
        "ATK": 775, "RLD": 4, "HIT": 75, "RNG": 2, "QNT": 2, "PEN": 3, "DIS": 0.5
    }
    def __init__(self, vessel_ID, batteryNumber):
        super().__init__(vessel_ID, batteryNumber) 


class double_F8_MatterFluxers(shipWeapon):
    gunName = 'Double (F8) Matter Fluxers'
    gun_stats = {
        "ATK": 396, "RLD": 4, "HIT": 75, "RNG": 2, "QNT": 2, "PEN": 3, "DIS": 0.5
    }
    def __init__(self, vessel_ID, batteryNumber):
        super().__init__(vessel_ID, batteryNumber) 
