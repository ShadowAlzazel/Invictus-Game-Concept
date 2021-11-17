#Ion Lasers
from shipClasses.shipEquipment.shipWeapons.weaponEntity import shipWeapon

#"""--<->----------------------------Ion-Lasers------------------------------<->--"""
#Chained-Ions Beams


class double_L18_DeuteriumLance(shipWeapon):
    gunName = 'Double (L18) Deuterium Lance'
    gunStats = {
        "ATK": 206 * 2, "RLD": 2, "HIT": 85, "RNG": 4
    }
    def __init__(self, vesselID, batteryNumber):
        super().__init__(vesselID, batteryNumber)


class triple_L18_DeuteriumLance(shipWeapon):
    gunName = 'Triple (L18) Deuterium Lance'
    gunStats = {
        "ATK": 206 * 3, "RLD": 2, "HIT": 85, "RNG": 4
    }
    def __init__(self, vesselID, batteryNumber):
        super().__init__(vesselID, batteryNumber)


class double_L13_HadronLance(shipWeapon):
    gunName = 'Double (L13) Hadron Lance'
    gunStats = {
        "ATK": 141 * 2, "RLD": 1, "HIT": 85, "RNG": 3
    }
    def __init__(self, vesselID, batteryNumber):
        super().__init__(vesselID, batteryNumber) 


class triple_L13_HadronLance(shipWeapon):
    gunName = 'Triple (L13) Hadron Lance'
    gunStats = {
        "ATK": 141 * 3, "RLD": 1, "HIT": 85, "RNG": 3
    }
    def __init__(self, vesselID, batteryNumber):
        super().__init__(vesselID, batteryNumber)


class triple_L6_ParticleLance(shipWeapon):
    gunName = 'Triple (L6) Laser Lance'
    gunStats = {
        "ATK": 58 * 3, "RLD": 1, "HIT": 85, "RNG": 2
    }
    def __init__(self, vesselID, batteryNumber):
        super().__init__(vesselID, batteryNumber)


class double_L6_ParticleLance(shipWeapon):
    gunName = 'Double (L5) Laser Lance'
    gunStats = {
        "ATK": 40 * 2, "RLD": 1, "HIT": 85, "RNG": 2
    }
    def __init__(self, vesselID, batteryNumber):
        super().__init__(vesselID, batteryNumber)