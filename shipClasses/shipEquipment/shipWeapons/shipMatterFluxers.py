#matter fluxers
from shipClasses.shipEquipment.shipWeapons.weaponEntity import shipWeapon

#"""--<->----------------------------MATTER-FLUXERS------------------------------<->--"""
#disentegrates matter by exciting quantum fields in focused dimensional beams  
#The higgs field is excited and starts to discharge, causing mass to leave the dimension.

class double_F20_MatterDisentegrators(shipWeapon):
    gunName = 'Double (F20) Matter Disentegrators'
    gunStats = {
        "ATK": 835, "RLD": 4, "HIT": 75, "RNG": 2, "QNT": 2
    }
    def __init__(self, vesselID, batteryNumber):
        super().__init__(vesselID, batteryNumber) 


class double_F14_MatterErasers(shipWeapon):
    gunName = 'Double (F14) Matter Erasers'
    gunStats = {
        "ATK": 565, "RLD": 4, "HIT": 75, "RNG": 2, "QNT": 2
    }
    def __init__(self, vesselID, batteryNumber):
        super().__init__(vesselID, batteryNumber) 


class double_F8_MatterFluxers(shipWeapon):
    gunName = 'Double (F8) Matter Fluxers'
    gunStats = {
        "ATK": 216, "RLD": 4, "HIT": 75, "RNG": 2, "QNT": 2
    }
    def __init__(self, vesselID, batteryNumber):
        super().__init__(vesselID, batteryNumber) 
