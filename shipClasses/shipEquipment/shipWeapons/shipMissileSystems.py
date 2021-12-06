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
    gun_stats = {
        "ATK": 292, "RLD": 6, "HIT": 40, "RNG": 4, "QNT": 21, "PEN": 0.5, "DIS": 1
    }
    def __init__(self, vessel_ID, battery_turret_number):
        super().__init__(vessel_ID, battery_turret_number)


class VLS_35C_DevestationMissiles(shipWeapon):
    gun_stats = {
        "ATK": 122, "RLD": 6, "HIT": 40, "RNG": 4, "QNT": 35, "PEN": 0.5, "DIS": 1
    }
    def __init__(self, vessel_ID, battery_turret_number):
        super().__init__(vessel_ID, battery_turret_number)