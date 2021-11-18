#shield generators 

#"""---------------------------------SHIELD-OBJECT----------------------------------"""
class shieldGen:
    def __init__(self, vesselID): 
        self.energyField = 10
        self.damageAbsorbed = 0
        self.ringField = 100 #initial shield
        self.equipID = '-'.join([vesselID, 'SGEN'])
        self.rechargeRate = 100

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
        self.rechargeRate = 100


class HyperShieldGen(shieldGen):
    shieldName = 'Hyper Shield-Generator'
    def __init__(self, vesselID):
        super().__init__(vesselID)
        self.energyField = 50
        self.ringField = 1600
        self.rechargeRate = 200


class DarkEnergyShieldGen(shieldGen):
    shieldName = 'Dark Energy Shield-Generator'
    def __init__(self, vesselID):
        super().__init__(vesselID)
        self.energyField = 70
        self.ringField = 3000
        self.rechargeRate = 300