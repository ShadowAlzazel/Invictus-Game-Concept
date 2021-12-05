#Plasma Phasers
from shipClasses.shipEquipment.shipWeapons.weaponEntity import shipWeapon

#"""--<->----------------------------Plasma-Accelerators------------------------------<->--"""
#supercharged and superheated plasma accelereated in containment warheads

class double_P24_PulsarPhasers(shipWeapon):
    gun_name = 'Double (P24) Pulsar Phasers'
    gun_stats = {
        "ATK": 1258, "RLD": 3, "HIT": 55, "RNG": 5, "QNT": 2, "PEN": 0, "DIS": 1.5
    }
    def __init__(self, vessel_ID, battery_turret_number):
        super().__init__(vessel_ID, battery_turret_number)


class triple_P24_PulsarPhasers(shipWeapon):
    gun_name = 'Triple (P24) Pulsar Phasers'
    gun_stats = {
        "ATK": 1258, "RLD": 3, "HIT": 55, "RNG": 5, "QNT": 3, "PEN": 0, "DIS": 1.5
    }
    def __init__(self, vessel_ID, battery_turret_number):
        super().__init__(vessel_ID, battery_turret_number)


class double_P22_PulsarPhasers(shipWeapon):
    gun_name = 'Double (P22) Pulsar Phasers'
    gun_stats = {
        "ATK": 1118, "RLD": 2, "HIT": 55, "RNG": 5, "QNT": 2, "PEN": 0, "DIS": 1.5
    }
    def __init__(self, vessel_ID, battery_turret_number):
        super().__init__(vessel_ID, battery_turret_number)


class triple_P18_NovaPhasers(shipWeapon):
    gun_name = 'Triple (P19) Nova Phasers'
    gun_stats = {
        "ATK": 856, "RLD": 2, "HIT": 55, "RNG": 4, "QNT": 3, "PEN": 0, "DIS": 1.5
    }
    def __init__(self, vessel_ID, battery_turret_number):
        super().__init__(vessel_ID, battery_turret_number)


class triple_P12_SolarPhasers(shipWeapon):
    gun_name = 'Triple (P12) Solar Phasers'
    gun_stats = {
        "ATK": 552, "RLD": 2, "HIT": 55, "RNG": 3, "QNT": 3, "PEN": 0, "DIS": 1.5
    }
    def __init__(self, vessel_ID, battery_turret_number):
        super().__init__(vessel_ID, battery_turret_number)


class triple_P6_PlasmaPhasers(shipWeapon):
    gun_name = 'Triple (P6) Plasma Phasers'
    gun_stats = {
        "ATK": 175, "RLD": 1, "HIT": 55, "RNG": 2, "QNT": 3, "PEN": 0, "DIS": 1.5
    }
    def __init__(self, vessel_ID, battery_turret_number):
        super().__init__(vessel_ID, battery_turret_number)


class double_P6_PlasmaPhasers(shipWeapon):
    gun_name = 'Triple (P6) Plasma Phasers'
    gun_stats = {
        "ATK": 175, "RLD": 1, "HIT": 55, "RNG": 2, "QNT": 2, "PEN": 0, "DIS": 1.5
    }
    def __init__(self, vessel_ID, battery_turret_number):
        super().__init__(vessel_ID, battery_turret_number)