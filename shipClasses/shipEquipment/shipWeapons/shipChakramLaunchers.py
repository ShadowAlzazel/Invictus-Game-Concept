#Chakram Launchers
from shipClasses.shipEquipment.shipWeapons.weaponEntity import shipWeapon


#"""--<->----------------------------CHAKRAM-LAUNCHERS------------------------------<->--"""
#chakram disks outlined with superheated plasma made for penetration and small form-factor

class broadside_A6_ChakramLaunchers(shipWeapon):
    gunName = 'Broadside (A6) Chakram Launchers'
    gunStats = {
        "ATK": 99, "RLD": 2, "HIT": 79, "RNG": 2, "QNT": 24, "PEN": 2, "DIS": 0.75
    }
    def __init__(self, vesselID, batteryNumber):
        super().__init__(vesselID, batteryNumber)
