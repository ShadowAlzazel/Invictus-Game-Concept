#Point Defense Systems/Emplacements
from shipClasses.shipEquipment.shipWeapons.weaponEntity import shipWeapon


#"""--<->--------------------------Point-Defense----------------------------<->--"""

#quadruple lasers in ball-joint-point-defense-weapon-system
class quad_BPoDS(shipWeapon):
    gunName = 'Quad BPODS'
    gunStats = {
        "ATK": 9 * 4, "RLD": 1, "HIT": 75, "RNG": 1
    }
    def __init__(self, vesselID, batteryNumber):
        super().__init__(vesselID, batteryNumber)
