#Missile launchers 
from shipClasses.shipEquipment.shipWeapons.weaponEntity import shipWeapon

#"""--------------------------------SHIP-MISSILES------------------------------"""
#variable launch systems

class VLS21_antimatterMissiles(shipWeapon):
    gunStats = {
        "ATK": 372, "RLD": 6, "HIT": 65, "RNG": 4, "QNT": 21
    }
    def __init__(self, vesselID, batteryNumber):
        super().__init__(vesselID, batteryNumber)


class VLS35_nuclearMissiles(shipWeapon):
    gunStats = {
        "ATK": 172, "RLD": 6, "HIT": 65, "RNG": 3, "QNT": 35
    }
    def __init__(self, vesselID, batteryNumber):
        super().__init__(vesselID, batteryNumber)