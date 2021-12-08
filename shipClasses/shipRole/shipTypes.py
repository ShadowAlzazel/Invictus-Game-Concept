from shipClasses.shipRole.shipEntity import Ship

#"""---------------------------------------SHIP-TYPES------------------------------------------"""

#Battleship
class Battleship(Ship):
    ammount = 0
    ship_type = 'BB'
    ship_stats = {
        "FP": 650, "ACC": 35, "EVA": 30, "SPD": 4,
        "RDR": 7, "LCK": 10, "STH": 0
    }

    shields = 45000 
    hull = 17500

    def __init__(self, hullnumber, name, command, fleet_name):
        super().__init__(hullnumber, name, command, fleet_name)
        Battleship.ammount += 1
        print(self.ship_type, '-', hullnumber, sep='')


#Battlecruiser
class Battlecruiser(Ship):
    ammount = 0
    ship_type = 'BC'
    ship_stats = {       
        "FP": 500, "ACC": 45, "EVA": 35, "SPD": 5,
        "RDR": 6, "LCK": 10, "STH": 0
    }

    shields = 27500
    hull = 12500

    def __init__(self, hullnumber, name, command, fleet_name):
        super().__init__(hullnumber, name, command, fleet_name)
        Battlecruiser.ammount += 1
        print(self.ship_type, '-', hullnumber, sep='')


#Strikecruiser
class Strikecruiser(Ship):
    ammount = 0
    ship_type = 'CS'
    ship_stats = {
        "FP": 280, "ACC": 38, "EVA": 40, "SPD": 6,
        "RDR": 5, "LCK": 10, "STH": 1
    }
    
    shields = 12500
    hull = 8500

    def __init__(self, hullnumber, name, command, fleet_name):
        super().__init__(hullnumber, name, command, fleet_name)
        Strikecruiser.ammount += 1
        print(self.ship_type, '-', hullnumber, sep='')


#Heavycrusier
class Heavycruiser(Ship):
    ammount = 0 
    ship_type = 'CA'
    ship_stats = {
        "FP": 350, "ACC": 33, "EVA": 30, "SPD": 5,
        "RDR": 5, "LCK": 10, "STH": 0
    }
    
    shields = 10000
    hull = 10000

    def __init__(self, hullnumber, name, command, fleet_name):
        super().__init__(hullnumber, name, command, fleet_name)
        Heavycruiser.ammount += 1
        print(self.ship_type, '-', hullnumber, sep='')


#Lightcruiser
class Lightcruiser(Ship):
    ammount = 0 
    ship_type = 'CL'
    ship_stats = {
        "FP": 200, "ACC": 35, "EVA": 45, "SPD": 7,
        "RDR": 5, "LCK": 10, "STH": 2
    }
    
    shields = 7500
    hull = 7500

    def __init__(self, hullnumber, name, command, fleet_name):
        super().__init__(hullnumber, name, command, fleet_name)
        Lightcruiser.ammount += 1
        print(self.ship_type, '-', hullnumber, sep='') 


#Destroyers
class Destroyer(Ship):
    ammount = 0
    ship_type = 'DD'
    ship_stats = {
        "FP": 100, "ACC": 45, "EVA": 65, "SPD": 8,
        "RDR": 5, "LCK": 10, "STH": 2
    }
    
    shields = 3300
    hull = 2500

    def __init__(self, hullnumber, name, command, fleet_name):
        super().__init__(hullnumber, name, command, fleet_name)
        Destroyer.ammount += 1
        print(self.ship_type, '-', hullnumber, sep='')