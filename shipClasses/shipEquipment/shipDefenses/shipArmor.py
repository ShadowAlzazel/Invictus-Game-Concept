#Ship Armor Types]

#"""--------------------------------ARMOR-OBJECT----------------------------------"""
class armor:
    armor_name = 'armor'
    armorValue = 1
    armor_repair = 0

    def __init__(self, vessel_ID):
        self.armor_integrity = 100 #%
        self.equipment_ID = '-'.join([vessel_ID, 'ARMR'])

    def armorDamage(self, damageNum, wPEN=0):
        p = wPEN
        if wPEN > self.armorValue:
            p = self.armorValue 

        trueDamage = damageNum / (1 + ((self.armorValue - p) * (self.armor_integrity / 100)))
        if damageNum / (self.armor_integrity + 1) > self.armor_integrity + 1:
            self.armor_integrity = 0
        elif self.armor_integrity != 0:
            self.armor_integrity -= trueDamage / (self.armor_integrity * self.armorValue) #decrerase armor integrity over exposure and hits
        return trueDamage

#"""-------------------------------------SHIP-ARMORS------------------------------------"""

class TitaniumArmor(armor):
    armor_name = 'Titanium Armor'
    armorValue = 2

    def __init__(self, vessel_ID):
        super().__init__(vessel_ID)
        

class CarbonNanoThreadsArmor(armor):
    armor_name = 'Carbon-Nanothreads Armor'
    armorValue = 3.25
    
    def __init__(self, vessel_ID):
        super().__init__(vessel_ID)
        

class OrichalcumAlloyArmor(armor):
    armor_name = 'Orichalcum-alloy Armor'
    armorValue = 3.25
    armor_repair = 1.0
    
    def __init__(self, vessel_ID):
        super().__init__(vessel_ID)


class MythrilAlloyArmor(armor):
    armor_name = 'Mythril-alloy Armor'
    armorValue = 4.0
    armor_repair = 1.75


    def __init__(self, vessel_ID):
        super().__init__(vessel_ID)
    

class LivingDurasteelArmor(armor):
    armor_name = 'Living Durasteel Armor'
    armorValue = 4.55
    armor_repair = 2.2


    def __init__(self, vessel_ID):
        super().__init__(vessel_ID)


class DurasteelArmor(armor):
    armor_name = 'Durasteel Armor'
    armorValue = 5.0

    def __init__(self, vessel_ID):
        super().__init__(vessel_ID) 


class NeutroniumArmor(armor):
    armor_name = 'Neutronium Armor'
    armorValue = 6.2
    
    def __init__(self, vessel_ID):
        super().__init__(vessel_ID)
        

class AdamantiumAlloyArmor(armor):
    armor_name = 'Adamantium-alloy Armor'
    armorValue = 6.0
    armor_repair = 2.46

    def __init__(self, vessel_ID):
        super().__init__(vessel_ID)


class DarkNeutroniumArmor(armor):
    armor_name = 'Dark Neutronium Armor'
    armorValue = 7.77

    def __init__(self, vessel_ID):
        super().__init__(vessel_ID)