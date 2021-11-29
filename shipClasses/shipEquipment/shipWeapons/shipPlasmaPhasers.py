#Plasma Phasers
from shipClasses.shipEquipment.shipWeapons.weaponEntity import shipWeapon

#"""--<->----------------------------Plasma-Accelerators------------------------------<->--"""
#supercharged and superheated plasma accelereated in containment warheads

class double_P24_PulsarPhasers(shipWeapon):
    gunName = 'Double (P24) Pulsar Phasers'
    gunStats = {
        "ATK": 1258, "RLD": 3, "HIT": 55, "RNG": 5, "QNT": 2, "PEN": 0, "DIS": 1.5
    }
    def __init__(self, vesselID, batteryNumber):
        super().__init__(vesselID, batteryNumber)


class triple_P24_PulsarPhasers(shipWeapon):
    gunName = 'Triple (P24) Pulsar Phasers'
    gunStats = {
        "ATK": 1258, "RLD": 3, "HIT": 55, "RNG": 5, "QNT": 3, "PEN": 0, "DIS": 1.5
    }
    def __init__(self, vesselID, batteryNumber):
        super().__init__(vesselID, batteryNumber)


class double_P22_PulsarPhasers(shipWeapon):
    gunName = 'Double (P22) Pulsar Phasers'
    gunStats = {
        "ATK": 1118, "RLD": 2, "HIT": 55, "RNG": 5, "QNT": 2, "PEN": 0, "DIS": 1.5
    }
    def __init__(self, vesselID, batteryNumber):
        super().__init__(vesselID, batteryNumber)


class triple_P18_NovaPhasers(shipWeapon):
    gunName = 'Triple (P19) Nova Phasers'
    gunStats = {
        "ATK": 856, "RLD": 2, "HIT": 55, "RNG": 4, "QNT": 3, "PEN": 0, "DIS": 1.5
    }
    def __init__(self, vesselID, batteryNumber):
        super().__init__(vesselID, batteryNumber)


class triple_P12_SolarPhasers(shipWeapon):
    gunName = 'Triple (P12) Solar Phasers'
    gunStats = {
        "ATK": 552, "RLD": 2, "HIT": 55, "RNG": 3, "QNT": 3, "PEN": 0, "DIS": 1.5
    }
    def __init__(self, vesselID, batteryNumber):
        super().__init__(vesselID, batteryNumber)


class triple_P6_PlasmaPhasers(shipWeapon):
    gunName = 'Triple (P6) Plasma Phasers'
    gunStats = {
        "ATK": 175, "RLD": 1, "HIT": 55, "RNG": 2, "QNT": 3, "PEN": 0, "DIS": 1.5
    }
    def __init__(self, vesselID, batteryNumber):
        super().__init__(vesselID, batteryNumber)


class double_P6_PlasmaPhasers(shipWeapon):
    gunName = 'Triple (P6) Plasma Phasers'
    gunStats = {
        "ATK": 175, "RLD": 1, "HIT": 55, "RNG": 2, "QNT": 2, "PEN": 0, "DIS": 1.5
    }
    def __init__(self, vesselID, batteryNumber):
        super().__init__(vesselID, batteryNumber)