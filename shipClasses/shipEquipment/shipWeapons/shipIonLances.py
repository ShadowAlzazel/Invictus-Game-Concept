#Ion Lances
from shipClasses.shipEquipment.shipWeapons.weaponEntity import shipWeapon

#"""--<->----------------------------ION-LANCES------------------------------<->--"""
#Chained-Ions Beams
#chains energized ions and light particles in high energy states to weaponize it


class double_L18_DeuteriumLance(shipWeapon):
    gunName = 'Double (L18) Deuterium Lance'
    gunStats = {
        "ATK": 586, "RLD": 2, "HIT": 85, "RNG": 3, "QNT": 2
    }
    def __init__(self, vesselID, batteryNumber):
        super().__init__(vesselID, batteryNumber)


class triple_L18_DeuteriumLance(shipWeapon):
    gunName = 'Triple (L18) Deuterium Lance'
    gunStats = {
        "ATK": 586, "RLD": 2, "HIT": 85, "RNG": 4, "QNT": 3
    }
    def __init__(self, vesselID, batteryNumber):
        super().__init__(vesselID, batteryNumber)


class double_L13_HadronLance(shipWeapon):
    gunName = 'Double (L13) Hadron Lance'
    gunStats = {
        "ATK": 341, "RLD": 1, "HIT": 85, "RNG": 3, "QNT": 2
    }
    def __init__(self, vesselID, batteryNumber):
        super().__init__(vesselID, batteryNumber) 


class triple_L13_HadronLance(shipWeapon):
    gunName = 'Triple (L13) Hadron Lance'
    gunStats = {
        "ATK": 341, "RLD": 1, "HIT": 85, "RNG": 3, "QNT": 3
    }
    def __init__(self, vesselID, batteryNumber):
        super().__init__(vesselID, batteryNumber)


class triple_L6_ParticleLance(shipWeapon):
    gunName = 'Triple (L6) Particle Lance'
    gunStats = {
        "ATK": 72, "RLD": 1, "HIT": 85, "RNG": 2, "QNT": 3
    }
    def __init__(self, vesselID, batteryNumber):
        super().__init__(vesselID, batteryNumber)


class double_L6_ParticleLance(shipWeapon):
    gunName = 'Double (L5) Particle Lance'
    gunStats = {
        "ATK": 72, "RLD": 1, "HIT": 85, "RNG": 2, "QNT": 2
    }
    def __init__(self, vesselID, batteryNumber):
        super().__init__(vesselID, batteryNumber)