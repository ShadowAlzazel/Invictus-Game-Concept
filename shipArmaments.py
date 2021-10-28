#Started 10/25/2021
#RNG in km
#RLD in Seconds

"""--<->----------------------------BB-Guns------------------------------<->--"""

#Double Gun Turret Z_MK6
class doubleZeusCannonMKVI:
    gunStats = {
        "ATK": 140 * 2, "RLD": 14, "HIT": 50, "RNG": 30
    }

    def __init__(self, armaID):
        self.armaID = armaID 


#Triple Gun Turret Z_MK6
class tripleZeusCannonMKVI:
    gunStats = {
        "ATK": 140 * 3, "RLD": 18, "HIT": 51, "RNG": 30
    }

    def __init__(self, armaID):
        self.armaID = armaID 


#Quadruple Gun Turret Z_MK6
class quadrupleZeusCannonMKVI:
    gunStats = {
        "ATK": 140 * 4, "RLD": 22, "HIT": 52, "RNG": 30
    }

    def __init__(self, armaID):
        self.armaID = armaID 

        
#Triple Gun Turret Z_MK7
class tripleZeusCannonMKVII:
    gunStats = {
        "ATK": 185 * 3, "RLD": 19, "HIT": 55, "RNG": 35
    }

    def __init__(self, armaID):
        self.armaID = armaID 


#Quad Ball Point-Defense Laser System
class quadBPDLaser:
    gunStats = {
        "ATK": 23 * 4, "RLD": 5, "HIT": 75, "RNG": 5
    }
    
    def __init__(self, armaID):
        self.armaID = armaID 
