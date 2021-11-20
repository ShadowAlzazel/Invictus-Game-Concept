#Energy Lasers
from shipClasses.shipEquipment.shipWeapons.weaponEntity import shipWeapon

#"""--<->----------------------------ENERGY-LASERS------------------------------<->--"""
#Energy Laser:
#charged and energized electromagnetic waves

class triple_L17_GammaRayLasers(shipWeapon):
    gunName = 'Triple (L17) Gamma Ray Lasers'
    gunStats = {
        "ATK": 468, "RLD": 1, "HIT": 93, "RNG": 1, "QNT": 3
    }
    def __init__(self, vesselID, batteryNumber):
        super().__init__(vesselID, batteryNumber)


class double_L13_XRayLasers(shipWeapon):
    gunName = 'Double (L13) X-Ray Lasers'
    gunStats = {
        "ATK": 303, "RLD": 1, "HIT": 94, "RNG": 1, "QNT": 2
    }
    def __init__(self, vesselID, batteryNumber):
        super().__init__(vesselID, batteryNumber)


class triple_L13_XRayLasers(shipWeapon):
    gunName = 'Triple (L13) X-Ray Lasers'
    gunStats = {
        "ATK": 303, "RLD": 1, "HIT": 94, "RNG": 1, "QNT": 3
    }
    def __init__(self, vesselID, batteryNumber):
        super().__init__(vesselID, batteryNumber)


class triple_L9_UltravioletLasers(shipWeapon):
    gunName = 'Triple (L9) Ultraviolet Lasers'
    gunStats = {
        "ATK": 191, "RLD": 1, "HIT": 96, "RNG": 1, "QNT": 3
    }
    def __init__(self, vesselID, batteryNumber):
        super().__init__(vesselID, batteryNumber)


class triple_L5_WaveLasers(shipWeapon):
    gunName = 'Triple (L5) Wave Lasers'
    gunStats = {
        "ATK": 64, "RLD": 1, "HIT": 97, "RNG": 1, "QNT": 3
    }
    def __init__(self, vesselID, batteryNumber):
        super().__init__(vesselID, batteryNumber)


class double_L5_WaveLasers(shipWeapon):
    gunName = 'Double (L5) Wave Lasers'
    gunStats = {
        "ATK": 64, "RLD": 1, "HIT": 97, "RNG": 1, "QNT": 2
    }
    def __init__(self, vesselID, batteryNumber):
        super().__init__(vesselID, batteryNumber)



