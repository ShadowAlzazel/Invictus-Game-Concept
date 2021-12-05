#Ion Lances
from shipClasses.shipEquipment.shipWeapons.weaponEntity import shipWeapon

#"""--<->----------------------------ION-LANCES------------------------------<->--"""
#Chained-Ions Beams
#chains energized ions and light particles in high energy states to weaponize it

class double_L23_PositroniumLance(shipWeapon):
    gun_name = 'Double (L18) Positronium Lance'
    gun_stats = {
        "ATK": 886, "RLD": 2, "HIT": 85, "RNG": 3, "QNT": 2, "PEN": 0, "DIS": 1
    }
    def __init__(self, vessel_ID, battery_turret_number):
        super().__init__(vessel_ID, battery_turret_number)


class double_L18_DeuteriumLance(shipWeapon):
    gun_name = 'Double (L18) Deuterium Lance'
    gun_stats = {
        "ATK": 586, "RLD": 2, "HIT": 85, "RNG": 3, "QNT": 2, "PEN": 0, "DIS": 1
    }
    def __init__(self, vessel_ID, battery_turret_number):
        super().__init__(vessel_ID, battery_turret_number)


class triple_L18_DeuteriumLance(shipWeapon):
    gun_name = 'Triple (L18) Deuterium Lance'
    gun_stats = {
        "ATK": 586, "RLD": 2, "HIT": 85, "RNG": 4, "QNT": 3, "PEN": 0, "DIS": 1
    }
    def __init__(self, vessel_ID, battery_turret_number):
        super().__init__(vessel_ID, battery_turret_number)


class double_L13_HadronLance(shipWeapon):
    gun_name = 'Double (L13) Hadron Lance'
    gun_stats = {
        "ATK": 341, "RLD": 1, "HIT": 85, "RNG": 3, "QNT": 2, "PEN": 0, "DIS": 1
    }
    def __init__(self, vessel_ID, battery_turret_number):
        super().__init__(vessel_ID, battery_turret_number) 


class triple_L13_HadronLance(shipWeapon):
    gun_name = 'Triple (L13) Hadron Lance'
    gun_stats = {
        "ATK": 341, "RLD": 1, "HIT": 85, "RNG": 3, "QNT": 3, "PEN": 0, "DIS": 1
    }
    def __init__(self, vessel_ID, battery_turret_number):
        super().__init__(vessel_ID, battery_turret_number)


class triple_L6_ParticleLance(shipWeapon):
    gun_name = 'Triple (L6) Particle Lance'
    gun_stats = {
        "ATK": 72, "RLD": 1, "HIT": 85, "RNG": 2, "QNT": 3, "PEN": 0, "DIS": 1
    }
    def __init__(self, vessel_ID, battery_turret_number):
        super().__init__(vessel_ID, battery_turret_number)


class double_L6_ParticleLance(shipWeapon):
    gun_name = 'Double (L5) Particle Lance'
    gun_stats = {
        "ATK": 72, "RLD": 1, "HIT": 85, "RNG": 2, "QNT": 2, "PEN": 0, "DIS": 1
    }
    def __init__(self, vessel_ID, battery_turret_number):
        super().__init__(vessel_ID, battery_turret_number)