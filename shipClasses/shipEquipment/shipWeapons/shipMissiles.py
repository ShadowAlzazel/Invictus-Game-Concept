#Missile launchers 
from shipClasses.shipEquipment.shipWeapons.weaponEntity import shipWeapon

#"""--------------------------------SHIP-MISSILES------------------------------"""

class VLS21_antimatter_missiles(shipWeapon):
    gunStats = {
        "ATK": 372 * 21, "RLD": 6, "HIT": 75, "RNG": 4
    }
    def __init__(self, vesselID, batteryNumber):
        super().__init__(vesselID, batteryNumber)
