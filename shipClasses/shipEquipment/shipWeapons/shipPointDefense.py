#Point Defense Systems/Emplacements
from shipClasses.shipEquipment.shipWeapons.weaponEntity import shipWeapon


#"""--<->--------------------------Point-Defense----------------------------<->--"""

#quadruple lasers in ball-joint-point-defense-weapon-system
class quad_BPoDS(shipWeapon):
    gunName = 'Quad BPODS'
    gun_stats = {
        "ATK": 12, "RLD": 1, "HIT": 75, "RNG": 1, "QNT": 4, "PEN": 0, "DIS": 1
    }
    def __init__(self, vesse_ID, batteryNumber):
        super().__init__(vesse_ID, batteryNumber)
