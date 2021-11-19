#torpedoes 
from shipClasses.shipEquipment.shipWeapons.weaponEntity import shipWeapon

#"""-------------------------------TORPEDOES------------------------------"""
#fixed laucnh platform
#A - antimatter - annahilation
#N - thermonuclear - devestation
#S - micro-singularity - eradication
#B - biological and chemical - desolation

class FLP5_DevestationTorpedoes(shipWeapon):
    gunStats = {
        "ATK": 472, "RLD": 7, "HIT": 72, "RNG": 5, "QNT": 5
    }
    def __init__(self, vesselID, batteryNumber):
        super().__init__(vesselID, batteryNumber)