#Plasma Accelerators
from shipClasses.shipEquipment.shipWeapons.weaponEntity import shipWeapon

#"""--<->----------------------------Plasma-Accelerators------------------------------<->--"""
#supercharged and superheated plasma accelereated in containment warheads

class triple_P19_NovaAccelerators(shipWeapon):
    gunName = 'Triple (P19) Nova Accelerators'
    gunStats = {
        "ATK": 382, "RLD": 3, "HIT": 50, "RNG": 4, "QNT": 3
    }
    def __init__(self, vesselID, batteryNumber):
        super().__init__(vesselID, batteryNumber)


class triple_P12_SolarAccelerators(shipWeapon):
    gunName = 'Triple (P12) Solar Accelerators'
    gunStats = {
        "ATK": 212, "RLD": 3, "HIT": 50, "RNG": 3, "QNT": 3
    }
    def __init__(self, vesselID, batteryNumber):
        super().__init__(vesselID, batteryNumber)


class triple_P6_PlasmaAccelerators(shipWeapon):
    gunName = 'Triple (P6) Plasma Accelerators'
    gunStats = {
        "ATK": 65, "RLD": 3, "HIT": 50, "RNG": 2, "QNT": 3
    }
    def __init__(self, vesselID, batteryNumber):
        super().__init__(vesselID, batteryNumber)