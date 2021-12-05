#Realm Distorters
from shipClasses.shipEquipment.shipWeapons.weaponEntity import shipWeapon


#"""--<->----------------------------REALM-DISTORTERS------------------------------<->--"""
#uses warp technology to create sinusodial space-time waves that distort matter

class double_A8_RealmDistorter(shipWeapon):
    gun_name = 'Double (A8) Realm Distorter'
    gun_stats = {
        "ATK": 279, "RLD": 3, "HIT": 79, "RNG": 2, "QNT": 2, "PEN": 0, "DIS": -1
    }
    def __init__(self, vessel_ID, battery_turret_number):
        super().__init__(vessel_ID, battery_turret_number)