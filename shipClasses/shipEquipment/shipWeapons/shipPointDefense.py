#Point Defense Systems/Emplacements
from shipClasses.shipEquipment.shipWeapons.weaponEntity import shipWeapon


#"""--<->--------------------------Point-Defense----------------------------<->--"""

#quadruple lasers in ball-joint-point-defense-weapon-system
class quad_BPoDS(shipWeapon):
    gun_name = 'Quad BPODS'
    gun_stats = {
        "ATK": 12, "RLD": 1, "HIT": 75, "RNG": 1, "QNT": 4, "PEN": 0, "DIS": 1
    }
    def __init__(self, vessel_ID, battery_turret_number):
        super().__init__(vessel_ID, battery_turret_number)
