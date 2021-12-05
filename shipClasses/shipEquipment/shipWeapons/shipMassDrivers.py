#mass cannons
from shipClasses.shipEquipment.shipWeapons.weaponEntity import shipWeapon

#"""--<->----------------------------MASS-DRIVERS------------------------------<->--"""
#mass drivers accelerate kinetic ammunition 

class double_M26_ZeusCannons(shipWeapon):
    gun_name = 'Double (M26) Zeus Cannons'
    gun_stats = {
        "ATK": 1248, "RLD": 3, "HIT": 55, "RNG": 7, "QNT": 2, "PEN": 0.5, "DIS": 1
    }
    def __init__(self, vessel_ID, battery_turret_number):
        super().__init__(vessel_ID, battery_turret_number)


class triple_M26_ZeusCannons(shipWeapon):
    gun_name = 'Triple (M26) Zeus Cannons'
    gun_stats = {
        "ATK": 1248, "RLD": 3, "HIT": 55, "RNG": 7, "QNT": 3, "PEN": 0.5, "DIS": 1
    }
    def __init__(self, vessel_ID, battery_turret_number):
        super().__init__(vessel_ID, battery_turret_number)


class double_M22_GigaRailCannons(shipWeapon):
    gun_name = 'Double (M22) Giga Rail Cannons'
    gun_stats = {
        "ATK": 1035, "RLD": 2, "HIT": 55, "RNG": 6, "QNT": 2, "PEN": 0.5, "DIS": 1
    }
    def __init__(self, vessel_ID, battery_turret_number):
        super().__init__(vessel_ID, battery_turret_number)


class triple_M22_GigaRailCannons(shipWeapon):
    gun_name = 'Triple (M22) Giga Rail Cannons'
    gun_stats = {
        "ATK": 1035, "RLD": 2, "HIT": 55, "RNG": 6, "QNT": 3, "PEN": 0.5, "DIS": 1
    }
    def __init__(self, vessel_ID, battery_turret_number):
        super().__init__(vessel_ID, battery_turret_number)


class quadruple_M22_GigaRailCannons(shipWeapon):
    gun_name = 'Quadruple (M22) Giga Rail Cannons'
    gun_stats = {
        "ATK": 1035, "RLD": 2, "HIT": 55, "RNG": 6, "QNT": 4, "PEN": 0.5, "DIS": 1
    }
    def __init__(self, vessel_ID, battery_turret_number):
        super().__init__(vessel_ID, battery_turret_number)


class triple_M16_RailCannons(shipWeapon):
    gun_name = 'Triple (M16) Rail Cannons'
    gun_stats = {
        "ATK": 612, "RLD": 2, "HIT": 55, "RNG": 5, "QNT": 3, "PEN": 0.5, "DIS": 1
    }
    def __init__(self, vessel_ID, battery_turret_number):
        super().__init__(vessel_ID, battery_turret_number)


class triple_M12_GaussCannons(shipWeapon):
    gun_name = 'Triple (M12) Gauss Cannons'
    gun_stats = {
        "ATK": 404, "RLD": 2, "HIT": 58, "RNG": 4, "QNT": 3, "PEN": 0.5, "DIS": 1
    }
    def __init__(self, vessel_ID, battery_turret_number):
        super().__init__(vessel_ID, battery_turret_number)


class quadruple_M12_GaussCannons(shipWeapon):
    gun_name = 'Quadruple (M12) Gauss Cannons'
    gun_stats = {
        "ATK": 404, "RLD": 2, "HIT": 58, "RNG": 4, "QNT": 4, "PEN": 0.5, "DIS": 1
    }
    def __init__(self, vessel_ID, battery_turret_number):
        super().__init__(vessel_ID, battery_turret_number) 


class triple_M7_TitanAutoCannons(shipWeapon):
    gun_name = 'Triple (M7) Titan Auto-Cannons'
    gun_stats = {
        "ATK": 184, "RLD": 1, "HIT": 61, "RNG": 2, "QNT": 3, "PEN": 0.5, "DIS": 1
    }
    def __init__(self, vessel_ID, battery_turret_number):
        super().__init__(vessel_ID, battery_turret_number)    


class double_M6_TitanAutoCannons(shipWeapon):
    gun_name = 'Double (M6) Titan Auto-Cannons'
    gun_stats = {
        "ATK": 151, "RLD": 1, "HIT": 61, "RNG": 2, "QNT": 2, "PEN": 0.5, "DIS": 1
    }
    def __init__(self, vessel_ID, battery_turret_number):
        super().__init__(vessel_ID, battery_turret_number) 


class triple_M5_WraithAutoGuns(shipWeapon):
    gun_name = 'Double (M4) Shredder Auto-Guns'
    gun_stats = {
        "ATK": 63, "RLD": 1, "HIT": 84, "RNG": 1, "QNT": 3, "PEN": 0.5, "DIS": 1
    }
    def __init__(self, vessel_ID, battery_turret_number):
        super().__init__(vessel_ID, battery_turret_number) 


class double_M4_ShredderAutoGuns(shipWeapon):
    gun_name = 'Double (M4) Shredder Auto-Guns'
    gun_stats = {
        "ATK": 43, "RLD": 1, "HIT": 88, "RNG": 1, "QNT": 2, "PEN": 0.5, "DIS": 1
    }
    def __init__(self, vessel_ID, battery_turret_number):
        super().__init__(vessel_ID, battery_turret_number) 
