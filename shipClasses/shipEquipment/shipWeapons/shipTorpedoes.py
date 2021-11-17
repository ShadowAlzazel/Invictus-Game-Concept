#torpedoes 
from shipClasses.shipEquipment.shipWeapons.weaponEntity import shipWeapon

#"""-------------------------------TORPEDOES------------------------------"""
#fixed laucnh platform

class FLP5_devestatorTorpedoes(shipWeapon):
    gunStats = {
        "ATK": 472, "RLD": 7, "HIT": 75, "RNG": 5, "QNT": 5
    }
    def __init__(self, vesselID, batteryNumber):
        super().__init__(vesselID, batteryNumber)