#Rail Cannons
from shipClasses.shipEquipment.shipWeapons.weaponEntity import shipWeapon

#"""--<->----------------------------Rail-Cannons------------------------------<->--"""
#Mass-Rail-Cannons:
#Zeus Cannons M24-30
#Thor Giga-Guns M16-23
#Neutron Launchers M11-15
#Titan Auto-Cannons M6-10
#Shredder Auto-Guns M1-5

class triple_M26_ZeusCannons(shipWeapon):
    gunName = 'Triple (M26) Zeus Cannons'
    gunStats = {
        "ATK": 515 * 3, "RLD": 3, "HIT": 55, "RNG": 7
    }
    def __init__(self, vesselID, turretDesignation):
        super().__init__(vesselID, turretDesignation)


class double_M22_ThorGigaGuns(shipWeapon):
    gunName = 'Double (M22) Thor Giga-Guns'
    gunStats = {
        "ATK": 348 * 2, "RLD": 3, "HIT": 53, "RNG": 6
    }
    def __init__(self, vesselID, turretDesignation):
        super().__init__(vesselID, turretDesignation)


class triple_M22_ThorGigaGuns(shipWeapon):
    gunName = 'Triple (M22) Thor Giga-Guns'
    gunStats = {
        "ATK": 348 * 3, "RLD": 3, "HIT": 53, "RNG": 6
    }
    def __init__(self, vesselID, turretDesignation):
        super().__init__(vesselID, turretDesignation)


class quadruple_M22_ThorGigaGuns(shipWeapon):
    gunName = 'Quadruple (M22) Thor Giga-Guns'
    gunStats = {
        "ATK": 348 * 4, "RLD": 3, "HIT": 53, "RNG": 6
    }
    def __init__(self, vesselID, turretDesignation):
        super().__init__(vesselID, turretDesignation)


class triple_M12_NeutronLauchers(shipWeapon):
    gunName = 'Triple (M12) Neutron Launchers'
    gunStats = {
        "ATK": 156 * 3, "RLD": 2, "HIT": 53, "RNG": 4
    }
    def __init__(self, vesselID, turretDesignation):
        super().__init__(vesselID, turretDesignation)


class quadruple_M12_NeutronLauchers(shipWeapon):
    gunName = 'Quadruple (M12) Neutron Launchers'
    gunStats = {
        "ATK": 156 * 4, "RLD": 2, "HIT": 53, "RNG": 4
    }
    def __init__(self, vesselID, turretDesignation):
        super().__init__(vesselID, turretDesignation) 


class triple_M7_TitanAutoCannons(shipWeapon):
    gunName = 'Triple (M7) Titan Auto-Cannons'
    gunStats = {
        "ATK": 51 * 3, "RLD": 1, "HIT": 55, "RNG": 2
    }
    def __init__(self, vesselID, turretDesignation):
        super().__init__(vesselID, turretDesignation)    


class double_M6_TitanAutoCannons(shipWeapon):
    gunName = 'Double (M6) Titan Auto-Cannons'
    gunStats = {
        "ATK": 45 * 2, "RLD": 1, "HIT": 55, "RNG": 2
    }
    def __init__(self, vesselID, turretDesignation):
        super().__init__(vesselID, turretDesignation) 


class double_M4_ShredderAutoGuns(shipWeapon):
    gunName = 'Double (M4) Shredder Auto-Guns'
    gunStats = {
        "ATK": 13 * 2, "RLD": 1, "HIT": 58, "RNG": 1
    }
    def __init__(self, vesselID, turretDesignation):
        super().__init__(vesselID, turretDesignation) 

