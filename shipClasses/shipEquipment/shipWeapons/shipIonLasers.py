#Ion Lasers
from shipClasses.shipEquipment.shipWeapons.weaponEntity import shipWeapon

#"""--<->----------------------------Ion-Lasers------------------------------<->--"""
#Chained-Ionic-Particles-Lasers:
#Deuterium Lance L16-23 'Uses special fusion chambers to create chians of super heated deuterium and electrons'
#Hadron Lance L8-15 'Uses special particle accelerators to create a plasma chian from hydrogen'
#Laser Lance L2-7 'Uses superenergized electro-magnetic particles'

class double_L18_DeuteriumLance(shipWeapon):
    gunName = 'Double (L18) Deuterium Lance'
    gunStats = {
        "ATK": 185 * 2, "RLD": 18, "HIT": 85, "RNG": 20
    }
    def __init__(self, vesselID, turretDesignation):
        super().__init__(vesselID, turretDesignation)


class triple_L18_DeuteriumLance(shipWeapon):
    gunName = 'Triple (L18) Deuterium Lance'
    gunStats = {
        "ATK": 185 * 3, "RLD": 19, "HIT": 85, "RNG": 20
    }
    def __init__(self, vesselID, turretDesignation):
        super().__init__(vesselID, turretDesignation)


class double_L13_HadronLance(shipWeapon):
    gunName = 'Double (L13) Hadron Lance'
    gunStats = {
        "ATK": 121 * 2, "RLD": 16, "HIT": 85, "RNG": 20
    }
    def __init__(self, vesselID, turretDesignation):
        super().__init__(vesselID, turretDesignation) 


class triple_L13_HadronLance(shipWeapon):
    gunName = 'Triple (L13) Hadron Lance'
    gunStats = {
        "ATK": 121 * 3, "RLD": 17, "HIT": 85, "RNG": 20
    }
    def __init__(self, vesselID, turretDesignation):
        super().__init__(vesselID, turretDesignation)


class triple_A6_LaserLance(shipWeapon):
    gunName = 'Triple (L6) Laser Lance'
    gunStats = {
        "ATK": 58 * 3, "RLD": 12, "HIT": 85, "RNG": 7
    }
    def __init__(self, vesselID, turretDesignation):
        super().__init__(vesselID, turretDesignation)


class double_A5_LaserLance(shipWeapon):
    gunName = 'Double (L5) Laser Lance'
    gunStats = {
        "ATK": 49 * 2, "RLD": 11, "HIT": 85, "RNG": 7
    }
    def __init__(self, vesselID, turretDesignation):
        super().__init__(vesselID, turretDesignation)