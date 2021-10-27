#Started 10/24/2021
from shipTypes import *
from shipClasses import *
from random import randint

#------------------OUTDATED-------------------


def combatGame(shipA, shipB):   
    game = 0
    vessel = priority(shipA, shipB)

    while game == 0:
        hit(vessel[0], vessel[1])
        hit(vessel[1], vessel[0])
        vessel[1].inspect()
        vessel[0].inspect()

        if input("Continue the Engagement? Y/N: ") == 'N':
            game += 1


def priority(vesselA, vesselB):
    combantants = []

    if vesselA.SPD > vesselB.SPD: 
        combantants = [vesselA, vesselB]
    else: 
        combantants = [vesselB, vesselA]
    
    return combantants


def hit(vessel_0, vessel_1):
    hitrate = (vessel_0.ACC) - (vessel_1.EVA) + 50  
    extraAcc = (hitrate % 100) * (hitrate // 100)
    critrate = (vessel_0.luck) - (vessel_1.luck) + 1 + extraAcc
    critmult = 1
    r = randint(0, 100)

    if hitrate >= r:
        if critrate >= r:
            critmult += 0.20 + (vessel_0.luck / 100)
        
        dmg = vessel_0.FP * critmult
        healthDamage(vessel_1, dmg) 
        print(vessel_0.name, "Has Hit", vessel_1.name, "For", dmg)
    else:
        print(vessel_0.name, "Has Missed", vessel_1.name)


def healthDamage(vessel, damage):
    if vessel.shields > damage:
        vessel.shields -= damage
    elif vessel.hull > damage:
        trudmg = damage - vessel.shields 
        vessel.shields = 0
        vessel.hull -= trudmg // vessel.armor
    else: 
        print(vessel.name, "Destroyed!")


#function call tester
BB66 = AmagiClass(66, 'Amagi')
BB69 = EssexClass(69, 'Essex')
BB76 = EssexClass(76, 'Enterprise')
BB79 = EssexClass(79, 'Intrepid')
DD557 = JohnstonClass(557, 'Johnston')

#combatGame(BB66, DD557)

#BB70 = Battleship(70, 'Valorant')
#BB79.shield_capacity = 76
#BB79.inspect()