#RNG in km
#RLD in Seconds
#M, L, A, denote the guns radius in inches
#All batteries designed for a single case

class shipWeapon:
    gunName = 'shipWeapon'
    gunStats = {
        "ATK": 32, "RLD": 1, "HIT": 64, "RNG": 1, "QNT": 1
    }

    def __init__(self, vesselID, batteryNumber):
        self.batteryID = '-'.join([vesselID, batteryNumber])
        self.gunLoadTime = 100 #preloaded

    def reloadGun(self):
        if self.gunLoadTime < self.gunStats['RLD']:
            self.gunLoadTime += 1
        else: 
            self.gunLoadTime = self.gunStats['RLD']
