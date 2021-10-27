#Started 10/25/2021
from shipClasses import *
from random import randint

def combatGame(shipA, shipB):
    game = 0 
    turn = 0
    vessel = turnPrio(shipA, shipB)

    while game == 0:
        totalDmg = 0

        for t in vessel[0 + turn].mainArm:
            if hitCalc(t, vessel[0 + turn].ACC, vessel[1 - turn].EVA) == True:
                totalDmg += damageCalc(t, vessel[0 + turn].FP, vessel[0 + turn].luck, vessel[1 - turn].luck, len(vessel[0 + turn].mainArm))
            else:
                totalDmg += 0
        healthCalc(vessel[1 - turn], totalDmg) 

        print(vessel[0 + turn].name, "Has hit", vessel[1 - turn].name, "for", totalDmg, "Damage!")
        totalDmg = 0
  
        if turn == 1:    
            vessel[0].inspect()
            vessel[1].inspect()     
            if input("Continue the Engagement? Y/N: ") == 'N':  
                game += 1
            else:
                turn -= 1
        else:
            turn += 1


#Who goes first in a turn based system
def turnPrio(A, B):
    shipPlayers = []

    if A.SPD > B.SPD:
        shipPlayers = [A, B]
    else:
        shipPlayers = [B, A]
    return shipPlayers

#hit calculator for armament using two ships stats
def hitCalc(t, s_ACC, d_EVA):
    hitRate = (s_ACC - d_EVA) + t.HIT
    r = randint(1, 100)

    if hitRate >= r:
        return True
    else:
        return False

#damage calculater for armament  using two ships stats
def damageCalc(t, s_FP, s_luck, d_luck, truFP):
    critRate = s_luck - d_luck + 5
    mult = 1
    damage = 0
    r = randint(1, 100)

    if critRate >= r:
        mult = 1.2 + (s_luck / 100)
    
    damage = ((t.ATK + (s_FP // truFP)) * mult) // 1
    return damage

#health calculator using an int damage
def healthCalc(vessel, damage):    
    if vessel.shields > damage:
        vessel.shields -= damage
    elif vessel.hull > damage:
        truDmg = damage - vessel.shields
        vessel.shields = 0
        vessel.hull -= truDmg // vessel.armor
    else: 
        print("Ship destroyed!")