#Ship Armor Types]

#"""--------------------------------ARMOR-OBJECT----------------------------------"""
class armor:
    def __init__(self, vesselID):
        self.armorIntegrity = 100 #%
        self.armorValue = 1
        self.armorRegen = 0
        self.equipID = '-'.join([vesselID, 'ARMR'])

    def armorDamage(self, damageNum):
        trueDamage = damageNum // ((1 - (self.armorIntegrity / 100)) + (self.armorValue * (self.armorIntegrity / 100)))
        if damageNum / (self.armorIntegrity + 1) > self.armorIntegrity + 1:
            self.armorIntegrity = 0
        else:
            self.armorIntegrity -= damageNum / self.armorIntegrity #decrerase armor integrity over contact
        self.armorIntegrity += self.armorRegen
        return trueDamage

#"""-------------------------------------SHIP-ARMORS------------------------------------"""

class TitaniumArmor(armor):
    armorName = 'Titanium Armor'

    def __init__(self, vesselID):
        super().__init__(vesselID)
        self.armorValue = 2


class CarbonNanoThreadsArmor(armor):
    armorName = 'Carbon-Nanothreads Armor'

    def __init__(self, vesselID):
        super().__init__(vesselID)
        self.armorValue = 3.25


class OrichalcumAlloyArmor(armor):
    armorName = 'Orichalcum-alloy Armor'

    def __init__(self, vesselID):
        super().__init__(vesselID)
        self.armorValue = 3.25
        self.armorRegen = 1.0


class MythrilAlloyArmor(armor):
    armorName = 'Mythril-alloy Armor'

    def __init__(self, vesselID):
        super().__init__(vesselID)
        self.armorValue = 4.0
        self.armorRegen = 1.75


class LivingDurasteelArmor(armor):
    armorName = 'Living Durasteel Armor'

    def __init__(self, vesselID):
        super().__init__(vesselID)
        self.armorValue = 4.75
        self.armorRegen = 2.5


class DurasteelArmor(armor):
    armorName = 'Durasteel Armor'

    def __init__(self, vesselID):
        super().__init__(vesselID)
        self.armorValue = 5.0 


class DarkNeutronianArmor(armor):
    armorName = 'Dark Neutronian Armor'

    def __init__(self, vesselID):
        super().__init__(vesselID)
        self.armorValue = 6.66