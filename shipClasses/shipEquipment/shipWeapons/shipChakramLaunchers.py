#Chakram Launchers
from shipClasses.shipEquipment.shipWeapons.weaponEntity import shipWeapon


#"""--<->----------------------------CHAKRAM-LAUNCHERS------------------------------<->--"""
#chakram disks outlined with superheated plasma made for penetration and small form-factor

class broadside_A6_ChakramLaunchers(shipWeapon):
    gun_name = 'Broadside (A6) Chakram Launchers'
    gun_stats = {
        "ATK": 99, "RLD": 2, "HIT": 79, "RNG": 2, "QNT": 24, "PEN": 2, "DIS": 0.75
    }
    def __init__(self, vessel_ID, battery_turret_number):
        super().__init__(vessel_ID, battery_turret_number)


class quadruple_A6_ChakramLaunchers(shipWeapon):
    gun_name = 'Quadruple (A6) Chakram Launchers'
    gun_stats = {
        "ATK": 99, "RLD": 2, "HIT": 79, "RNG": 2, "QNT": 4, "PEN": 2, "DIS": 0.75
    }
    def __init__(self, vessel_ID, battery_turret_number):
        super().__init__(vessel_ID, battery_turret_number)

