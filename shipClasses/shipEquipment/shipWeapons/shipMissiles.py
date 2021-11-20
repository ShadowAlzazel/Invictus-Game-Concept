#Missile launchers 
from shipClasses.shipEquipment.shipWeapons.weaponEntity import shipWeapon

#"""--------------------------------SHIP-MISSILES------------------------------"""
#variable launch systems
#nth Cells
#antimatter - annihilation
#thermonuclear - devestation
#micro-singularity - eradication
#biological and chemical - desolation
#

class VLS_21C_AnnihilationMissiles(shipWeapon):
    gunStats = {
        "ATK": 292, "RLD": 6, "HIT": 40, "RNG": 4, "QNT": 21
    }
    def __init__(self, vesselID, batteryNumber):
        super().__init__(vesselID, batteryNumber)


class VLS_35C_DevestationMissiles(shipWeapon):
    gunStats = {
        "ATK": 122, "RLD": 6, "HIT": 40, "RNG": 3, "QNT": 35
    }
    def __init__(self, vesselID, batteryNumber):
        super().__init__(vesselID, batteryNumber)