#Started 10/24/2021
from shipTypes import *
from shipClasses import *
from random import randint

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
    r = randint(0, 100)

    if r >= hitrate:
        #vessel_1.shields -= vessel_0.FP // vessel_1.Armor
        vessel_1.shields -= vessel_0.FP  
        print(vessel_0.name, "Has Hit", vessel_1.name, "For", vessel_0.FP)
    else:
        print(vessel_0.name, "Has Missed", vessel_1.name)



#function call tester
BB66 = AmagiClass(66, 'Amagi')
BB69 = EssexClass(69, 'Essex')
BB76 = EssexClass(76, 'Enterprise')
BB79 = EssexClass(79, 'Intrepid')

combatGame(BB66, BB76)

#BB70 = Battleship(70, 'Valorant')
#BB79.shield_capacity = 76
#BB79.inspect()
