#Plasma Phasers
from shipClasses.shipEquipment.shipWeapons.weaponEntity import shipWeapon

#"""--<->----------------------------Plasma-Accelerators------------------------------<->--"""
#supercharged and superheated plasma accelereated in containment warheads
class triple_P24_PulsarPhasers(shipWeapon):
    gunName = 'Triple (P19) Pulsar Phasers'
    gunStats = {
        "ATK": 562, "RLD": 3, "HIT": 55, "RNG": 5, "QNT": 3
    }
    def __init__(self, vesselID, batteryNumber):
        super().__init__(vesselID, batteryNumber)


class triple_P18_NovaPhasers(shipWeapon):
    gunName = 'Triple (P19) Nova Phasers'
    gunStats = {
        "ATK": 442, "RLD": 3, "HIT": 55, "RNG": 4, "QNT": 3
    }
    def __init__(self, vesselID, batteryNumber):
        super().__init__(vesselID, batteryNumber)


class triple_P12_SolarPhasers(shipWeapon):
    gunName = 'Triple (P12) Solar Phasers'
    gunStats = {
        "ATK": 212, "RLD": 2, "HIT": 55, "RNG": 3, "QNT": 3
    }
    def __init__(self, vesselID, batteryNumber):
        super().__init__(vesselID, batteryNumber)


class triple_P6_PlasmaPhasers(shipWeapon):
    gunName = 'Triple (P6) Plasma Phasers'
    gunStats = {
        "ATK": 65, "RLD": 1, "HIT": 55, "RNG": 2, "QNT": 3
    }
    def __init__(self, vesselID, batteryNumber):
        super().__init__(vesselID, batteryNumber)