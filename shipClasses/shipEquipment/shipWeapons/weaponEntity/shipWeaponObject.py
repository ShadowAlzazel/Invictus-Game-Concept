#RNG in km
#RLD in Seconds
#M, L, A, denote the guns radius in inches
#All batteries designed for a single case

class shipWeapon:

    def __init__(self, vesselID, turretDesignation):
        self.batteryID = '-'.join([vesselID, turretDesignation])
