#Started 10/25/2021
#RNG in km
#RLD in Seconds

"""--<->----------------------------Rail-Cannons------------------------------<->--"""

#Two heavy mass-rail-cannons(Gen6) desgined for a single turret case
class doubleZeusCannonMKVI:
    gunStats = {
        "ATK": 183 * 2, "RLD": 14, "HIT": 50, "RNG": 30
    }

    def __init__(self, armaID):
        self.armaID = armaID 


#Three grade mass-rail-cannons(Gen6) desgined for a single turret case
class tripleZeusCannonMKVI:
    gunStats = {
        "ATK": 183 * 3, "RLD": 16, "HIT": 51, "RNG": 30
    }

    def __init__(self, armaID):
        self.armaID = armaID 


#Four heavy mass-rail-cannons(Gen6) desgined for a single turret case
class quadrupleZeusCannonMKVI:
    gunStats = {
        "ATK": 183 * 4, "RLD": 18, "HIT": 52, "RNG": 30
    }

    def __init__(self, armaID):
        self.armaID = armaID 

        
#Three heavy mass-rail-cannons(Gen7) desgined for a single turret case
class tripleZeusCannonMKVII:
    gunStats = {
        "ATK": 225 * 3, "RLD": 21, "HIT": 55, "RNG": 35
    }

    def __init__(self, armaID):
        self.armaID = armaID 


#Three medium mass-rail-cannons(Gen8) designed for a single turret case
class tripleThorCannonMKVIII:
    gunStats = {
        "ATK": 91 * 3, "RLD": 11, "HIT": 53, "RNG": 20
    }

    def __init__(self, armaID):
        self.armaID = armaID 


#Four medium mass-rail-cannons(Gen8) designed for a single turret case
class quadrupleThorCannonMKVIII:
    gunStats = {
        "ATK": 91 * 4, "RLD": 12, "HIT": 54, "RNG": 20
    }

    def __init__(self, armaID):
        self.armaID = armaID 



"""--<->----------------------------Ion-Throwers------------------------------<->--"""

#Three particle-ion-chain launchers(Gen4) designed for a single turret case
class doubleArcThrowerMKV:
    gunStats = {
        "ATK": 149 * 2, "RLD": 14, "HIT": 75, "RNG": 25
    }

    def __init__(self, armaID):
        self.armaID = armaID 


#Three particle-ion-chain launchers(Gen4) designed for a single turret case
class tripleArcThrowerMKV:
    gunStats = {
        "ATK": 149 * 3, "RLD": 15, "HIT": 75, "RNG": 25
    }

    def __init__(self, armaID):
        self.armaID = armaID 


#Two particle-ion-chain launchers(Gen4) designed for a single turret case
class doubleArcThrowerMKIV:
    gunStats = {
        "ATK": 119 * 2, "RLD": 14, "HIT": 75, "RNG": 20
    }

    def __init__(self, armaID):
        self.armaID = armaID 

"""--<->--------------------------Point-Defense----------------------------<->--"""


#Quad Ball Point-Defense Laser System
class quadBPDLaser:
    gunStats = {
        "ATK": 23 * 4, "RLD": 5, "HIT": 75, "RNG": 5
    }
    
    def __init__(self, armaID):
        self.armaID = armaID 
