#Started 10/24/2021
from shipTypes import *
from shipClasses import *

def combat_1v1(shipA, shipB):   
    combat = 0

    if shipA.EVA > shipB.EVA:
        prio = shipA
        nonp = shipB
    else:
        prio = shipB
        nonp = shipA

    while combat == 0:
        nonp.shields -= prio.FP
        print(prio.name, "Has Hit", nonp.name, "For", prio.FP)
        prio.shields -= nonp.FP
        print(nonp.name, "Has Hit", prio.name, "For", nonp.FP)
        nonp.inspect()
        prio.inspect()

        prompt = input("Continue the Engagement? Y/N: ")
        if prompt == 'N':
            combat += 1

#BASIC FUNCTION CALL TESTER
BB66 = AmagiClass(66, 'Amagi')
BB69 = EssexClass(69, 'Essex')
BB76 = EssexClass(76, 'Enterprise')
BB79 = EssexClass(79, 'Intrepid')

combat_1v1(BB66, BB76)

#BB70 = Battleship(70, 'Valorant')
#BB79.shield_capacity = 76
#BB79.inspect()
