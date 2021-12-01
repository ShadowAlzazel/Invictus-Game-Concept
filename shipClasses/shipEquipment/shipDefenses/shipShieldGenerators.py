#shield generators 

#"""---------------------------------SHIELD-OBJECT----------------------------------"""
class shieldGen:
    energyField = 10
    ringField = 100 #initial shield
    rechargeRate = 1 #percantage

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
class AdvancedShieldGen(shieldGen):
    shieldName = 'Hyper Shield-Generator'
    energyField = 110
    ringField = 1800
    rechargeRate = 0.5

    def __init__(self, vesselID):
        super().__init__(vesselID)
        

class MegaShieldGen(shieldGen):
    shieldName = 'Mega Shield-Generator'
    energyField = 150
    ringField = 2200
    rechargeRate = 0.5

    def __init__(self, vesselID):
        super().__init__(vesselID)


class GigaShieldGen(shieldGen):
    shieldName = 'Giga Shield-Generator'
    energyField = 200
    ringField = 2600
    rechargeRate = 0.5

    def __init__(self, vesselID):
        super().__init__(vesselID)


class LumioneShieldGen(shieldGen):
    shieldName = 'Lumione Shield-Generator'
    energyField = 30
    ringField = 550
    rechargeRate = 1.25
    
    def __init__(self, vesselID):
        super().__init__(vesselID)


class HyperiumShieldGen(shieldGen):
    shieldName = 'Hyper Shield-Generator'
    energyField = 50
    ringField = 1100
    rechargeRate = 2

    def __init__(self, vesselID):
        super().__init__(vesselID)


class HiggsShieldGen(shieldGen):
    shieldName = 'Higgs Shield-Generator'
    energyField = 70
    ringField = 1650
    rechargeRate = 2.825

    def __init__(self, vesselID):
        super().__init__(vesselID)


class DarkMatterShieldGen(shieldGen):
    shieldName = 'Dark Energy Shield-Generator'
    energyField = 120
    ringField = 3000
    rechargeRate = 3.75

    def __init__(self, vesselID):
        super().__init__(vesselID)