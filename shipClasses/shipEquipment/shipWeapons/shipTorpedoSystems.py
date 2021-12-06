#torpedoes 
from shipClasses.shipEquipment.shipWeapons.weaponEntity import shipWeapon

#"""-------------------------------TORPEDOES------------------------------"""
#fixed laucnh platform
#A - antimatter - annahilation
#N - thermonuclear - devestation
#S - micro-singularity - eradication
#B - biological and chemical - desolation

class FLP5_DevestationTorpedoes(shipWeapon):
    gun_stats = {
        "ATK": 472, "RLD": 7, "HIT": 55, "RNG": 5, "QNT": 5, "PEN": 0, "DIS": 1
    }
    def __init__(self, vessel_ID, battery_turret_number):
        super().__init__(vessel_ID, battery_turret_number)