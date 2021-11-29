#shield generators 

#"""---------------------------------SHIELD-OBJECT----------------------------------"""
class shieldGen:
    energyField = 10
    ringField = 100 #initial shield
    rechargeRate = 100

    def __init__(self, vesselID): 
        self.damageAbsorbed = 0
        self.equipID = '-'.join([vesselID, 'SGEN'])

    def shieldDamage(self, damageNum, wDIS):
        if damageNum < self.energyField or self.damageAbsorbed < self.ringField:
            trueDamage = 0  
        else:
            trueDamage = damageNum * wDIS
        self.damageAbsorbed += damageNum
        return trueDamage


#"""-----------------------------------SHIP-SHIELDS-----------------------------------"""

class LumioneShieldGen(shieldGen):
    shieldName = 'Lumione Shield-Generator'
    energyField = 30
    ringField = 250
    rechargeRate = 100
    
    def __init__(self, vesselID):
        super().__init__(vesselID)


class HyperShieldGen(shieldGen):
    shieldName = 'Hyper Shield-Generator'
    energyField = 50
    ringField = 1600
    rechargeRate = 200

    def __init__(self, vesselID):
        super().__init__(vesselID)


class DarkEnergyShieldGen(shieldGen):
    shieldName = 'Dark Energy Shield-Generator'
    energyField = 70
    ringField = 3000
    rechargeRate = 300

    def __init__(self, vesselID):
        super().__init__(vesselID)