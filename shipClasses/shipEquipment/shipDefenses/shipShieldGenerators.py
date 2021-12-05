#shield generators 

#"""---------------------------------SHIELD-OBJECT----------------------------------"""
class shieldGen:
    energyField = 10
    ringField = 100 #initial shield
    shield_regeneration = 1 #percantage

    def __init__(self, vesse_ID): 
        self.damageAbsorbed = 0
        self.equipID = '-'.join([vesse_ID, 'SGEN'])

    def shieldDamage(self, damageNum, wDIS):
        if damageNum < self.energyField or self.damageAbsorbed < self.ringField:
            trueDamage = 0  
        else:
            trueDamage = damageNum * wDIS
        self.damageAbsorbed += damageNum
        return trueDamage


#"""-----------------------------------SHIP-SHIELDS-----------------------------------"""
class AdvancedShieldGen(shieldGen):
    shield_name = 'Hyper Shield-Generator'
    energyField = 110
    ringField = 1800
    shield_regeneration = 0.5

    def __init__(self, vesse_ID):
        super().__init__(vesse_ID)
        

class MegaShieldGen(shieldGen):
    shield_name = 'Mega Shield-Generator'
    energyField = 150
    ringField = 2200
    shield_regeneration = 0.5

    def __init__(self, vesse_ID):
        super().__init__(vesse_ID)


class GigaShieldGen(shieldGen):
    shield_name = 'Giga Shield-Generator'
    energyField = 200
    ringField = 2600
    shield_regeneration = 0.5

    def __init__(self, vesse_ID):
        super().__init__(vesse_ID)


class LumioneShieldGen(shieldGen):
    shield_name = 'Lumione Shield-Generator'
    energyField = 30
    ringField = 550
    shield_regeneration = 1.25
    
    def __init__(self, vesse_ID):
        super().__init__(vesse_ID)


class HyperiumShieldGen(shieldGen):
    shield_name = 'Hyper Shield-Generator'
    energyField = 50
    ringField = 1100
    shield_regeneration = 2

    def __init__(self, vesse_ID):
        super().__init__(vesse_ID)


class HiggsShieldGen(shieldGen):
    shield_name = 'Higgs Shield-Generator'
    energyField = 70
    ringField = 1650
    shield_regeneration = 2.825

    def __init__(self, vesse_ID):
        super().__init__(vesse_ID)


class DarkMatterShieldGen(shieldGen):
    shield_name = 'Dark Energy Shield-Generator'
    energyField = 120
    ringField = 3000
    shield_regeneration = 3.75

    def __init__(self, vesse_ID):
        super().__init__(vesse_ID)