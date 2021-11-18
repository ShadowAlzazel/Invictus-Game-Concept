#Arc Throwers
from shipClasses.shipEquipment.shipWeapons.weaponEntity import shipWeapon

#"""--<->----------------------------ARC-THROWERS------------------------------<->--"""
#elctromagnetically charged particles are discharged in massive ammounts

#HAT3 Arc-Thrower A15-20 '(Hyper Array of Trasnformers with Exremely Energized Electrons)'

class double_A17_HAT3ArcThrowers(shipWeapon):
    gunName = 'Double (A17) HAT3 Arc-Throwers'
    gunStats = {
        "ATK": 529, "RLD": 3, "HIT": 75, "RNG": 2, "QNT": 2
    }
    def __init__(self, vesselID, batteryNumber):
        super().__init__(vesselID, batteryNumber)


class triple_A17_HAT3ArcThrowers(shipWeapon):
    gunName = 'Triple (A17) HAT3 Arc-Throwers'
    gunStats = {
        "ATK": 529, "RLD": 3, "HIT": 75, "RNG": 2, "QNT": 3
    }
    def __init__(self, vesselID, batteryNumber):
        super().__init__(vesselID, batteryNumber)


class triple_A11_TeslaArcThrowers(shipWeapon):
    gunName = 'Triple (A11) Tesla Arc-Throwers'
    gunStats = {
        "ATK": 297, "RLD": 3, "HIT": 75, "RNG": 2, "QNT": 3
    }
    def __init__(self, vesselID, batteryNumber):
        super().__init__(vesselID, batteryNumber)


class double_A8_AmplifiedArcThrowers(shipWeapon):
    gunStats = {
        "ATK": 237, "RLD": 2, "HIT": 75, "RNG":2, "QNT": 2
    }
    def __init__(self, vesselID, batteryNumber):
        super().__init__(vesselID, batteryNumber)  


class double_A5_ArcThrowers(shipWeapon):
    gunName = 'Double (A5) Arc-Throwers'
    gunStats = {
        "ATK": 177, "RLD": 2, "HIT": 75, "RNG": 2, "QNT": 2
    }
    def __init__(self, vesselID, batteryNumber):
        super().__init__(vesselID, batteryNumber)
