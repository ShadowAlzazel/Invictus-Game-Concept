#Arc Throwers
from shipClasses.shipEquipment.shipWeapons.weaponEntity import shipWeapon

#"""--<->----------------------------Arc-Throwers------------------------------<->--"""
#Arc-Throwers:
#HAT3 Arc-Thrower A15-20 '(Hyper Array and Trasnformers of Exremely Energized Excited Electrons)'
#Tesla Arc-Thrower A9-14 'Uses superconductive coils supercharged in parallel to discharge massive ammounts of elctrons'
#Wave Arc-Thrower A4-8 'Uses electromagnetic waves to create a super crest in which elctrons ar discharged' 

class double_A17_HAT3ArcThrowers(shipWeapon):
    gunName = 'Double (A17) HAT3 Arc-Throwers'
    gunStats = {
        "ATK": 409 * 2, "RLD": 21, "HIT": 51, "RNG": 15
    }
    def __init__(self, vesselID, turretDesignation):
        super().__init__(vesselID, turretDesignation)


class triple_A17_HAT3ArcThrowers(shipWeapon):
    gunName = 'Triple (A17) HAT3 Arc-Throwers'
    gunStats = {
        "ATK": 409 * 3, "RLD": 22, "HIT": 51, "RNG": 15
    }
    def __init__(self, vesselID, turretDesignation):
        super().__init__(vesselID, turretDesignation)


class triple_A11_TeslaArcThrowers(shipWeapon):
    gunName = 'Triple (A11) Tesla Arc-Throwers'
    gunStats = {
        "ATK": 347 * 3, "RLD": 18, "HIT": 51, "RNG": 15
    }
    def __init__(self, vesselID, turretDesignation):
        super().__init__(vesselID, turretDesignation)


class double_A5_WaveArcThrowers(shipWeapon):
    gunName = 'Double (A5) Wave Arc-Throwers'
    gunStats = {
        "ATK": 157 * 2, "RLD": 16, "HIT": 51, "RNG": 12
    }
    def __init__(self, vesselID, turretDesignation):
        super().__init__(vesselID, turretDesignation)
