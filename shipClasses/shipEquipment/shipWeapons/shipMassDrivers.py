#mass cannons
from shipClasses.shipEquipment.shipWeapons.weaponEntity import shipWeapon

#"""--<->----------------------------MASS-DRIVERS------------------------------<->--"""
#mass drivers accelerate kinetic ammunition 

class triple_M26_ZeusCannons(shipWeapon):
    gunName = 'Triple (M26) Zeus Cannons'
    gunStats = {
        "ATK": 515, "RLD": 3, "HIT": 55, "RNG": 7, "QNT": 3
    }
    def __init__(self, vesselID, batteryNumber):
        super().__init__(vesselID, batteryNumber)


class double_M22_GigaRailCannons(shipWeapon):
    gunName = 'Double (M22) Giga Rail Cannons'
    gunStats = {
        "ATK": 367, "RLD": 3, "HIT": 53, "RNG": 6, "QNT": 2
    }
    def __init__(self, vesselID, batteryNumber):
        super().__init__(vesselID, batteryNumber)


class triple_M22_GigaRailCannons(shipWeapon):
    gunName = 'Triple (M22) Giga Rail Cannons'
    gunStats = {
        "ATK": 367, "RLD": 3, "HIT": 53, "RNG": 6, "QNT": 3
    }
    def __init__(self, vesselID, batteryNumber):
        super().__init__(vesselID, batteryNumber)


class quadruple_M22_GigaRailCannons(shipWeapon):
    gunName = 'Quadruple (M22) Giga Rail Cannons'
    gunStats = {
        "ATK": 367, "RLD": 3, "HIT": 53, "RNG": 6, "QNT": 4
    }
    def __init__(self, vesselID, batteryNumber):
        super().__init__(vesselID, batteryNumber)


class triple_M16_RailCannons(shipWeapon):
    gunName = 'Triple (M16) Rail Cannons'
    gunStats = {
        "ATK": 216, "RLD": 2, "HIT": 53, "RNG": 5, "QNT": 3
    }
    def __init__(self, vesselID, batteryNumber):
        super().__init__(vesselID, batteryNumber)


class triple_M12_GaussCannons(shipWeapon):
    gunName = 'Triple (M12) Gauss Cannons'
    gunStats = {
        "ATK": 156, "RLD": 2, "HIT": 53, "RNG": 4, "QNT": 3
    }
    def __init__(self, vesselID, batteryNumber):
        super().__init__(vesselID, batteryNumber)


class quadruple_M12_GaussCannons(shipWeapon):
    gunName = 'Quadruple (M12) Gauss Cannons'
    gunStats = {
        "ATK": 156, "RLD": 2, "HIT": 53, "RNG": 4, "QNT": 4
    }
    def __init__(self, vesselID, batteryNumber):
        super().__init__(vesselID, batteryNumber) 


class triple_M7_TitanAutoCannons(shipWeapon):
    gunName = 'Triple (M7) Titan Auto-Cannons'
    gunStats = {
        "ATK": 51, "RLD": 1, "HIT": 55, "RNG": 2, "QNT": 3
    }
    def __init__(self, vesselID, batteryNumber):
        super().__init__(vesselID, batteryNumber)    


class double_M6_TitanAutoCannons(shipWeapon):
    gunName = 'Double (M6) Titan Auto-Cannons'
    gunStats = {
        "ATK": 45, "RLD": 1, "HIT": 55, "RNG": 2, "QNT": 2
    }
    def __init__(self, vesselID, batteryNumber):
        super().__init__(vesselID, batteryNumber) 


class double_M4_ShredderAutoCannons(shipWeapon):
    gunName = 'Double (M4) Shredder Auto-Guns'
    gunStats = {
        "ATK": 13, "RLD": 1, "HIT": 58, "RNG": 1, "QNT": 2
    }
    def __init__(self, vesselID, batteryNumber):
        super().__init__(vesselID, batteryNumber) 
