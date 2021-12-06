#Arc Throwers
from shipClasses.shipEquipment.shipWeapons.weaponEntity import shipWeapon


#"""--<->----------------------------ARC-THROWERS------------------------------<->--"""
#elctromagnetically charged particles are discharged in massive arcs
#HAT3 Arc-Thrower A15-20 '(Hyper Array of Trasnformers with Exremely Energized Electrons)'

class double_A17_HAT3ArcThrowers(shipWeapon):
    gun_name = 'Double (A17) HAT3 Arc-Throwers'
    gun_stats = {
        "ATK": 679, "RLD": 2, "HIT": 79, "RNG": 2, "QNT": 2, "PEN": 0, "DIS": 2
    }
    def __init__(self, vessel_ID, battery_turret_number):
        super().__init__(vessel_ID, battery_turret_number)


class triple_A17_HAT3ArcThrowers(shipWeapon):
    gun_name = 'Triple (A17) HAT3 Arc-Throwers'
    gun_stats = {
        "ATK": 679, "RLD": 2, "HIT": 79, "RNG": 2, "QNT": 3, "PEN": 0, "DIS": 2
    }
    def __init__(self, vessel_ID, battery_turret_number):
        super().__init__(vessel_ID, battery_turret_number)


class triple_A11_TeslaArcThrowers(shipWeapon):
    gun_name = 'Triple (A11) Tesla Arc-Throwers'
    gun_stats = {
        "ATK": 461, "RLD": 2, "HIT": 82, "RNG": 2, "QNT": 3, "PEN": 0, "DIS": 2
    }
    def __init__(self, vessel_ID, battery_turret_number):
        super().__init__(vessel_ID, battery_turret_number)


class double_A8_AmplifiedArcThrowers(shipWeapon):
    gun_stats = {
        "ATK": 329, "RLD": 2, "HIT": 82, "RNG":2, "QNT": 2, "PEN": 0, "DIS": 2
    }
    def __init__(self, vessel_ID, battery_turret_number):
        super().__init__(vessel_ID, battery_turret_number)  


class double_A5_ArcThrowers(shipWeapon):
    gun_name = 'Double (A5) Arc-Throwers'
    gun_stats = {
        "ATK": 187, "RLD": 2, "HIT": 85, "RNG": 1, "QNT": 2, "PEN": 0, "DIS": 2
    }
    def __init__(self, vessel_ID, battery_turret_number):
        super().__init__(vessel_ID, battery_turret_number)
