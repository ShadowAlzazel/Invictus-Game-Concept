#Started 10/25/2021
#RNG in km
#RLD in Seconds

"""--<->----------------------------BB-Guns------------------------------<->--"""

#Double Gun Turret Z_MK6
class doubleZeusCannonMKVI:
    ATK = 70 * 2
    RLD = 25
    HIT = 50
    RNG = 30

    def __init__(self, armaID):
        self.armaID = armaID 


#Triple Gun Turret Z_MK6
class tripleZeusCannonMKVI:
    ATK = 70 * 3
    RLD = 21
    HIT = 50
    RNG = 30

    def __init__(self, armaID):
        self.armaID = armaID 


#Quadruple Gun Turret Z_MK6
class quadrupleZeusCannonMKVI:
    ATK = 70 * 4
    RLD = 29
    HIT = 50
    RNG = 30

    def __init__(self, armaID):
        self.armaID = armaID 

        
#Triple Gun Turret Z_MK7
class tripleZeusCannonMKVII:
    ATK = 97 * 3
    RLD = 24
    HIT = 55
    RNG = 35

    def __init__(self, armaID):
        self.armaID = armaID 


#Quad Ball Point-Defense Laser System
class quadBPDLaser:
    ATK = 14 * 4
    RLD = 5
    HIT = 75
    RNG = 5 

    def __init__(self, armaID):
        self.armaID = armaID 
