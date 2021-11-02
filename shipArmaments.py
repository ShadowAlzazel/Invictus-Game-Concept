#Started 10/25/2021
#RNG in km
#RLD in Seconds
#M, L, A, denote the guns radius in inches
#All batteries designed for a single case

class shipBattery:

    def __init__(self, vesselID, turretDesignation):
        batteryID = '-'.join([vesselID, turretDesignation])
        self.batteryID = batteryID


"""--<->----------------------------Rail-Cannons------------------------------<->--"""
#Mass-Rail-Cannons:
#Zeus Cannons M24-30
#Thor Giga-Guns M16-23
#Neutron Launchers M11-15
#Titan Auto-Cannons M6-10
#Shredder Auto-Guns M1-5

class triple_M26_ZeusCannons(shipBattery):
    gunStats = {
        "ATK": 296 * 3, "RLD": 19, "HIT": 55, "RNG": 35
    }

    def __init__(self, vesselID, turretDesignation):
        super().__init__(vesselID, turretDesignation)


class double_M22_ThorGigaGuns(shipBattery):
    gunStats = {
        "ATK": 248 * 2, "RLD": 14, "HIT": 53, "RNG": 35
    }

    def __init__(self, vesselID, turretDesignation):
        super().__init__(vesselID, turretDesignation)


class triple_M22_ThorGigaGuns(shipBattery):
    gunStats = {
        "ATK": 248 * 3, "RLD": 16, "HIT": 53, "RNG": 35
    }

    def __init__(self, vesselID, turretDesignation):
        super().__init__(vesselID, turretDesignation)


class quadruple_M22_ThorGigaGuns(shipBattery):
    gunStats = {
        "ATK": 248 * 4, "RLD": 18, "HIT": 53, "RNG": 35
    }

    def __init__(self, vesselID, turretDesignation):
        super().__init__(vesselID, turretDesignation)


class triple_M12_NeutronLauchers(shipBattery):
    gunStats = {
        "ATK": 126 * 3, "RLD": 11, "HIT": 53, "RNG": 35
    }

    def __init__(self, vesselID, turretDesignation):
        super().__init__(vesselID, turretDesignation)


class quadruple_M12_NeutronLauchers(shipBattery):
    gunStats = {
        "ATK": 126 * 4, "RLD": 12, "HIT": 53, "RNG": 35
    }

    def __init__(self, vesselID, turretDesignation):
        super().__init__(vesselID, turretDesignation) 


class triple_M7_TitanAutoCannons(shipBattery):
    gunStats = {
        "ATK": 38 * 3, "RLD": 5, "HIT": 55, "RNG": 10
    }

    def __init__(self, vesselID, turretDesignation):
        super().__init__(vesselID, turretDesignation)    


class double_M6_TitanAutoCannons(shipBattery):
    gunStats = {
        "ATK": 31 * 2, "RLD": 4, "HIT": 55, "RNG": 10
    }

    def __init__(self, vesselID, turretDesignation):
        super().__init__(vesselID, turretDesignation) 


class double_M4_ShredderAutoGuns(shipBattery):
    gunStats = {
        "ATK": 13 * 2, "RLD": 1, "HIT": 58, "RNG": 5
    }

    def __init__(self, vesselID, turretDesignation):
        super().__init__(vesselID, turretDesignation) 


"""--<->----------------------------Ion-Lasers------------------------------<->--"""
#Chained-Ionic-Particles-Lasers:
#Deuterium Lance L16-23 'Uses special fusion chambers to create chians of super heated deuterium and electrons'
#Hadron Lance L8-15 'Uses special particle accelerators to create a plasma chian from hydrogen'
#Laser Lance L2-7 'Uses superenergized electro-magnetic particles'

class double_L18_DeuteriumLance(shipBattery):
    gunStats = {
        "ATK": 165 * 2, "RLD": 18, "HIT": 85, "RNG": 20
    }

    def __init__(self, vesselID, turretDesignation):
        super().__init__(vesselID, turretDesignation)


class triple_L18_DeuteriumLance(shipBattery):
    gunStats = {
        "ATK": 165 * 3, "RLD": 19, "HIT": 85, "RNG": 20
    }

    def __init__(self, vesselID, turretDesignation):
        super().__init__(vesselID, turretDesignation)


class double_L13_HadronLance(shipBattery):
    gunStats = {
        "ATK": 109 * 2, "RLD": 16, "HIT": 85, "RNG": 20
    }

    def __init__(self, vesselID, turretDesignation):
        super().__init__(vesselID, turretDesignation) 


class triple_L13_HadronLance(shipBattery):
    gunStats = {
        "ATK": 109 * 3, "RLD": 17, "HIT": 85, "RNG": 20
    }

    def __init__(self, vesselID, turretDesignation):
        super().__init__(vesselID, turretDesignation)


class triple_A6_LaserLance(shipBattery):
    gunStats = {
        "ATK": 56 * 3, "RLD": 12, "HIT": 85, "RNG": 7
    }

    def __init__(self, vesselID, turretDesignation):
        super().__init__(vesselID, turretDesignation)


class double_A5_LaserLance(shipBattery):
    gunStats = {
        "ATK": 49 * 2, "RLD": 11, "HIT": 85, "RNG": 7
    }

    def __init__(self, vesselID, turretDesignation):
        super().__init__(vesselID, turretDesignation)

"""--<->----------------------------Arc-Throwers------------------------------<->--"""
#Arc-Throwers:
#HAT3 Arc-Thrower A15-20 '(Hyper Array and Trasnformers of Exremely Energized Excited Electrons)'
#Tesla Arc-Thrower A9-14 'Uses superconductive coils supercharged in parallel to discharge massive ammounts of elctrons'
#Wave Arc-Thrower A4-8 'Uses electromagnetic waves to create a super crest in which elctrons ar discharged' 

class double_A17_HAT3ArcThrowers(shipBattery):
    gunStats = {
        "ATK": 239 * 2, "RLD": 19, "HIT": 60, "RNG": 15
    }

    def __init__(self, vesselID, turretDesignation):
        super().__init__(vesselID, turretDesignation)


class triple_A17_HAT3ArcThrowers(shipBattery):
    gunStats = {
        "ATK": 239 * 3, "RLD": 20, "HIT": 51, "RNG": 15
    }

    def __init__(self, vesselID, turretDesignation):
        super().__init__(vesselID, turretDesignation)


class triple_A11_TeslaArcThrowers(shipBattery):
    gunStats = {
        "ATK": 157 * 3, "RLD": 18, "HIT": 51, "RNG": 15
    }

    def __init__(self, vesselID, turretDesignation):
        super().__init__(vesselID, turretDesignation)


class double_A5_WaveArcThrowers(shipBattery):
    gunStats = {
        "ATK": 97 * 2, "RLD": 16, "HIT": 51, "RNG": 12
    }

    def __init__(self, vesselID, turretDesignation):
        super().__init__(vesselID, turretDesignation)

"""--<->--------------------------Point-Defense----------------------------<->--"""


#quadruple lasers in ball-joint-point-defense-weapon-system
class quad_BPoDS(shipBattery):
    gunStats = {
        "ATK": 9 * 4, "RLD": 5, "HIT": 75, "RNG": 5
    }
    
    def __init__(self, vesselID, turretDesignation):
        super().__init__(vesselID, turretDesignation)
