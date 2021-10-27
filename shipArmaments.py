#Started 10/25/2021
#RNG in km
#RLD in Seconds


#Triple Gun Turret
class tripleZeusCannonMKVI:
    ATK = 70 * 3
    RLD = 21
    HIT = 50
    RNG = 30

    def __init__(self, gunID):
        self.gunID = gunID 

#Double Gun Turret
class doubleZeusCannonMKVI:
    ATK = 70 * 2
    RLD = 25
    HIT = 50

    def __init__(self, gunID):
        self.gunID = gunID 

#Quadruple Gun Turret
class quadrupleZeusCannonMKVI:
    ATK = 70 * 4
    RLD = 29
    HIT = 50

    def __init__(self, gunID):
        self.gunID = gunID 
        
#Quad Ball Point-Defense Laser System
class quadBPDLaser:
    ATK = 14 * 4
    RLD = 5
    HIT = 75
    RNG = 5 

    def __init__(self, gunID):
        self.gunID = gunID 
