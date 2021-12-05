#mass cannons
from shipClasses.shipEquipment.shipWeapons.weaponEntity import shipWeapon

#"""--<->----------------------------MASS-DRIVERS------------------------------<->--"""
#mass drivers accelerate kinetic ammunition 

class double_M26_ZeusCannons(shipWeapon):
    gunName = 'Double (M26) Zeus Cannons'
    gun_stats = {
        "ATK": 1248, "RLD": 3, "HIT": 55, "RNG": 7, "QNT": 2, "PEN": 0.5, "DIS": 1
    }
    def __init__(self, vessel_ID, batteryNumber):
        super().__init__(vessel_ID, batteryNumber)


class triple_M26_ZeusCannons(shipWeapon):
    gunName = 'Triple (M26) Zeus Cannons'
    gun_stats = {
        "ATK": 1248, "RLD": 3, "HIT": 55, "RNG": 7, "QNT": 3, "PEN": 0.5, "DIS": 1
    }
    def __init__(self, vessel_ID, batteryNumber):
        super().__init__(vessel_ID, batteryNumber)


class double_M22_GigaRailCannons(shipWeapon):
    gunName = 'Double (M22) Giga Rail Cannons'
    gun_stats = {
        "ATK": 1035, "RLD": 2, "HIT": 55, "RNG": 6, "QNT": 2, "PEN": 0.5, "DIS": 1
    }
    def __init__(self, vessel_ID, batteryNumber):
        super().__init__(vessel_ID, batteryNumber)


class triple_M22_GigaRailCannons(shipWeapon):
    gunName = 'Triple (M22) Giga Rail Cannons'
    gun_stats = {
        "ATK": 1035, "RLD": 2, "HIT": 55, "RNG": 6, "QNT": 3, "PEN": 0.5, "DIS": 1
    }
    def __init__(self, vessel_ID, batteryNumber):
        super().__init__(vessel_ID, batteryNumber)


class quadruple_M22_GigaRailCannons(shipWeapon):
    gunName = 'Quadruple (M22) Giga Rail Cannons'
    gun_stats = {
        "ATK": 1035, "RLD": 2, "HIT": 55, "RNG": 6, "QNT": 4, "PEN": 0.5, "DIS": 1
    }
    def __init__(self, vessel_ID, batteryNumber):
        super().__init__(vessel_ID, batteryNumber)


class triple_M16_RailCannons(shipWeapon):
    gunName = 'Triple (M16) Rail Cannons'
    gun_stats = {
        "ATK": 612, "RLD": 2, "HIT": 55, "RNG": 5, "QNT": 3, "PEN": 0.5, "DIS": 1
    }
    def __init__(self, vessel_ID, batteryNumber):
        super().__init__(vessel_ID, batteryNumber)


class triple_M12_GaussCannons(shipWeapon):
    gunName = 'Triple (M12) Gauss Cannons'
    gun_stats = {
        "ATK": 404, "RLD": 2, "HIT": 58, "RNG": 4, "QNT": 3, "PEN": 0.5, "DIS": 1
    }
    def __init__(self, vessel_ID, batteryNumber):
        super().__init__(vessel_ID, batteryNumber)


class quadruple_M12_GaussCannons(shipWeapon):
    gunName = 'Quadruple (M12) Gauss Cannons'
    gun_stats = {
        "ATK": 404, "RLD": 2, "HIT": 58, "RNG": 4, "QNT": 4, "PEN": 0.5, "DIS": 1
    }
    def __init__(self, vessel_ID, batteryNumber):
        super().__init__(vessel_ID, batteryNumber) 


class triple_M7_TitanAutoCannons(shipWeapon):
    gunName = 'Triple (M7) Titan Auto-Cannons'
    gun_stats = {
        "ATK": 184, "RLD": 1, "HIT": 61, "RNG": 2, "QNT": 3, "PEN": 0.5, "DIS": 1
    }
    def __init__(self, vessel_ID, batteryNumber):
        super().__init__(vessel_ID, batteryNumber)    


class double_M6_TitanAutoCannons(shipWeapon):
    gunName = 'Double (M6) Titan Auto-Cannons'
    gun_stats = {
        "ATK": 151, "RLD": 1, "HIT": 61, "RNG": 2, "QNT": 2, "PEN": 0.5, "DIS": 1
    }
    def __init__(self, vessel_ID, batteryNumber):
        super().__init__(vessel_ID, batteryNumber) 


class triple_M5_WraithAutoGuns(shipWeapon):
    gunName = 'Double (M4) Shredder Auto-Guns'
    gun_stats = {
        "ATK": 63, "RLD": 1, "HIT": 84, "RNG": 1, "QNT": 3, "PEN": 0.5, "DIS": 1
    }
    def __init__(self, vessel_ID, batteryNumber):
        super().__init__(vessel_ID, batteryNumber) 


class double_M4_ShredderAutoGuns(shipWeapon):
    gunName = 'Double (M4) Shredder Auto-Guns'
    gun_stats = {
        "ATK": 43, "RLD": 1, "HIT": 88, "RNG": 1, "QNT": 2, "PEN": 0.5, "DIS": 1
    }
    def __init__(self, vessel_ID, batteryNumber):
        super().__init__(vessel_ID, batteryNumber) 
