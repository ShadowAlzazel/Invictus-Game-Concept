#RNG in km
#RLD in Seconds
#M, L, A, denote the guns radius in inches
#All batteries designed for a single case

class shipWeapon:

    def __init__(self, vesselID, batteryNumber):
        self.batteryID = '-'.join([vesselID, batteryNumber])
        self.gunLoadTime = 100 #preloaded

    def reloadGun(self):
        if self.gunLoadTime < self.gunStats['RLD']:
            self.gunLoadTime += 1
        else: 
            self.gunLoadTime = self.gunStats['RLD']
