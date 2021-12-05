#Ship Armor Types]

#"""--------------------------------ARMOR-OBJECT----------------------------------"""
class armor:
    armor_name = 'armor'
    armor_value = 1
    armor_repair = 0

    def __init__(self, vessel_ID):
        self.armor_integrity = 100 #%
        self.equipment_ID = '-'.join([vessel_ID, 'ARMR'])

    def armorDamage(self, damage_amount, wep_PEN=0):
        true_PEN = wep_PEN
        if wep_PEN > self.armor_value:
            true_PEN = self.armor_value 

        true_damage = damage_amount / (1 + ((self.armor_value - true_PEN) * (self.armor_integrity / 100)))
        if damage_amount / (self.armor_integrity + 1) > self.armor_integrity + 1:
            self.armor_integrity = 0
        elif self.armor_integrity != 0:
            self.armor_integrity -= true_damage / (self.armor_integrity * self.armor_value) #decrerase armor integrity over exposure and hits
        return true_damage

#"""-------------------------------------SHIP-ARMORS------------------------------------"""

class TitaniumArmor(armor):
    armor_name = 'Titanium Armor'
    armor_value = 2

    def __init__(self, vessel_ID):
        super().__init__(vessel_ID)
        

class CarbonNanoThreadsArmor(armor):
    armor_name = 'Carbon-Nanothreads Armor'
    armor_value = 3.25
    
    def __init__(self, vessel_ID):
        super().__init__(vessel_ID)
        

class OrichalcumAlloyArmor(armor):
    armor_name = 'Orichalcum-alloy Armor'
    armor_value = 3.25
    armor_repair = 1.0
    
    def __init__(self, vessel_ID):
        super().__init__(vessel_ID)


class MythrilAlloyArmor(armor):
    armor_name = 'Mythril-alloy Armor'
    armor_value = 4.0
    armor_repair = 1.75


    def __init__(self, vessel_ID):
        super().__init__(vessel_ID)
    

class LivingDurasteelArmor(armor):
    armor_name = 'Living Durasteel Armor'
    armor_value = 4.55
    armor_repair = 2.2


    def __init__(self, vessel_ID):
        super().__init__(vessel_ID)


class DurasteelArmor(armor):
    armor_name = 'Durasteel Armor'
    armor_value = 5.0

    def __init__(self, vessel_ID):
        super().__init__(vessel_ID) 


class NeutroniumArmor(armor):
    armor_name = 'Neutronium Armor'
    armor_value = 6.2
    
    def __init__(self, vessel_ID):
        super().__init__(vessel_ID)
        

class AdamantiumAlloyArmor(armor):
    armor_name = 'Adamantium-alloy Armor'
    armor_value = 6.0
    armor_repair = 2.46

    def __init__(self, vessel_ID):
        super().__init__(vessel_ID)


class DarkNeutroniumArmor(armor):
    armor_name = 'Dark Neutronium Armor'
    armor_value = 7.77

    def __init__(self, vessel_ID):
        super().__init__(vessel_ID)