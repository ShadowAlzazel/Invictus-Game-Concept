#ship proton colliders
from shipClasses.shipEquipment.shipWeapons.weaponEntity import shipWeapon


#"""--<->----------------------------PROTON-COLLIDERS------------------------------<->--"""
#smashes protons and neutrinos at a target using particle accelarators for destructive capabilities

class double_A12_ProtonColliders(shipWeapon):
    gunName = 'Double (A12) Realm Distorter'
    gunStats = {
        "ATK": 656, "RLD": 2, "HIT": 69, "RNG": 2, "QNT": 2, "PEN": 1, "DIS": 2
    }
    def __init__(self, vesselID, batteryNumber):
        super().__init__(vesselID, batteryNumber)