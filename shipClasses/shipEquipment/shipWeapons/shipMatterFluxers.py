#matter fluxers
from shipClasses.shipEquipment.shipWeapons.weaponEntity import shipWeapon

#"""--<->----------------------------MATTER-FLUXERS------------------------------<->--"""
#disentegrates matter by exciting quantum fields in focused dimensional beams  
#The higgs field is excited and starts to discharge, causing mass to leave the dimension.

class double_F20_MatterDisentegrator(shipWeapon):
    gunName = 'double (F20) Matter Disentegrators'
    gunStats = {
        "ATK": 1035, "RLD": 4, "HIT": 85, "RNG": 2, "QNT": 2
    }
    def __init__(self, vesselID, batteryNumber):
        super().__init__(vesselID, batteryNumber) 


class double_F14_MatterEraser(shipWeapon):
    gunName = 'double (F14) Matter Eraser'
    gunStats = {
        "ATK": 765, "RLD": 4, "HIT": 85, "RNG": 2, "QNT": 2
    }
    def __init__(self, vesselID, batteryNumber):
        super().__init__(vesselID, batteryNumber) 


class double_F8_MatterFluxer(shipWeapon):
    gunName = 'double (F8) Matter Fluxers'
    gunStats = {
        "ATK": 456, "RLD": 4, "HIT": 75, "RNG": 2, "QNT": 2
    }
    def __init__(self, vesselID, batteryNumber):
        super().__init__(vesselID, batteryNumber) 
