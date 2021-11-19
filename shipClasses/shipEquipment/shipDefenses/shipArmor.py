#Ship Armor Types]

#"""--------------------------------ARMOR-OBJECT----------------------------------"""
class armor:
    armorValue = 1
    armorRegen = 0

    def __init__(self, vesselID):
        self.armorIntegrity = 100 #%
        self.equipID = '-'.join([vesselID, 'ARMR'])

    def armorDamage(self, damageNum):
        trueDamage = damageNum / ((1 - (self.armorIntegrity / 100)) + (self.armorValue * (self.armorIntegrity / 100)))
        if damageNum / (self.armorIntegrity + 1) > self.armorIntegrity + 1:
            self.armorIntegrity = 0
        elif self.armorIntegrity != 0:
            self.armorIntegrity -= damageNum / (self.armorIntegrity * self.armorValue) #decrerase armor integrity over exposure and hits
        self.armorIntegrity
        return trueDamage

#"""-------------------------------------SHIP-ARMORS------------------------------------"""

class TitaniumArmor(armor):
    armorName = 'Titanium Armor'
    armorValue = 2

    def __init__(self, vesselID):
        super().__init__(vesselID)
        

class CarbonNanoThreadsArmor(armor):
    armorName = 'Carbon-Nanothreads Armor'
    armorValue = 3.25
    
    def __init__(self, vesselID):
        super().__init__(vesselID)
        

class OrichalcumAlloyArmor(armor):
    armorName = 'Orichalcum-alloy Armor'
    armorValue = 3.25
    armorRegen = 1.0
    
    def __init__(self, vesselID):
        super().__init__(vesselID)


class MythrilAlloyArmor(armor):
    armorName = 'Mythril-alloy Armor'
    armorValue = 4.0
    armorRegen = 1.75


    def __init__(self, vesselID):
        super().__init__(vesselID)
    

class LivingDurasteelArmor(armor):
    armorName = 'Living Durasteel Armor'
    armorValue = 4.55
    armorRegen = 2.2


    def __init__(self, vesselID):
        super().__init__(vesselID)


class DurasteelArmor(armor):
    armorName = 'Durasteel Armor'
    armorValue = 5.0

    def __init__(self, vesselID):
        super().__init__(vesselID) 


class NeutroniumArmor(armor):
    armorName = 'Neutronium Armor'
    armorValue = 6.0
    
    def __init__(self, vesselID):
        super().__init__(vesselID)
        

class AdamantiumAlloyArmor(armor):
    armorName = 'Adamantium-alloy Armor'
    armorValue = 6.0
    armorRegen = 2.46

    def __init__(self, vesselID):
        super().__init__(vesselID)


class DarkNeutroniumArmor(armor):
    armorName = 'Dark Neutronium Armor'
    armorValue = 7.77

    def __init__(self, vesselID):
        super().__init__(vesselID)