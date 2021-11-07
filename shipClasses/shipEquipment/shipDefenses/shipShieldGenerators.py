#shield generators 

#"""---------------------------------SHIELD-OBJECT----------------------------------"""
class shieldGen:
    def __init__(self, vesselID): 
        self.energyField = 10
        self.damageAbsorbed = 0
        self.ringField = 500 #initial shield
        self.equipID = '-'.join([vesselID, 'SGEN'])

    def shieldDamage(self, damageNum):
        if damageNum < self.energyField or self.damageAbsorbed < self.ringField:
            trueDamage = 0  
        else:
            trueDamage = damageNum
        self.damageAbsorbed += damageNum
        return trueDamage


#"""-----------------------------------SHIP-SHIELDS-----------------------------------"""

class LumioneShieldGen(shieldGen):
    shieldName = 'Lumione Shield-Generator'

    def __init__(self, vesselID):
        super().__init__(vesselID)
        self.energyField = 30
        self.ringField = 250


class HyperShieldGen(shieldGen):
    shieldName = 'Hyper Shield-Generator'

    def __init__(self, vesselID):
        super().__init__(vesselID)
        self.energyField = 90
        self.ringField = 1600


class DarkEnergyShieldGen(shieldGen):
    shieldName = 'Dark Energy Shield-Generator'

    def __init__(self, vesselID):
        super().__init__(vesselID)
        self.energyField = 120
        self.ringField = 3000