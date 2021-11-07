import time 
from random import randint

#Timer 
def timerFunc(timeSecs):
    nowTime = time.time()
    stepTime = time.time()
    futureTime = nowTime + timeSecs
    u = 0
    while time.time() < futureTime:
        varTime = time.time()
        if (stepTime // 1) < (varTime // 1):
            stepTime = varTime
            u += 1


"""-----------------------------------------------------------------------"""
#Game Logics
class ACombatGame:


    def __init__(self, comTime, shipA, shipB):
        self.comTime = comTime
        self.combatLib = []
        if shipA.shipStats['SPD'] > shipB.shipStats['SPD']:
            self.combatLib.append(shipA)
            self.combatLib.append(shipB)
        else:
            self.combatLib.append(shipB)
            self.combatLib.append(shipA)


    def runGame(self, tSec, maxCycles):
        assert maxCycles % 2 == 0
        salvoDamage = 0
        turn = 0
        maxTurns = maxCycles #maxCycles = 2, for 1 second turns 
        x, y = 0, 1
        while turn < maxTurns:
            turn += 1
            print("Time Stamp: ", tSec, " Seconds, Turn: ", turn, sep='')
            #run primary guns
            for gunBattery in self.combatLib[x].primaryBattery:
                if (tSec % gunBattery.gunStats['RLD']) == 0:
                    if self.hitCalc(gunBattery, self.combatLib[x].shipStats['ACC'], self.combatLib[y].shipStats['EVA']) == True:
                        salvoDamage += self.damageCalc(gunBattery ,self.combatLib[x].shipStats['FP'], self.combatLib[x].shipStats['luck'],
                                                    self.combatLib[y].shipStats['luck'], len(self.combatLib[x].primaryBattery))
                    else:
                        salvoDamage += 0
                    self.combatLib[y].takeDamage(salvoDamage)
                    print(gunBattery.batteryID, "Has hit", self.combatLib[y].name, "For", salvoDamage, "Damage!")
                    salvoDamage = 0

            #run secondary guns
            for gunBattery in self.combatLib[x].secondaryBattery:
                if (tSec % gunBattery.gunStats['RLD']) == 0:
                    if self.hitCalc(gunBattery, self.combatLib[x].shipStats['ACC'], self.combatLib[y].shipStats['EVA']) == True:
                        salvoDamage += self.damageCalc(gunBattery ,self.combatLib[x].shipStats['FP'], self.combatLib[x].shipStats['luck'],
                                                    self.combatLib[y].shipStats['luck'], len(self.combatLib[x].secondaryBattery))
                    else:
                        salvoDamage += 0
                    self.combatLib[y].takeDamage(salvoDamage)
                    print(gunBattery.batteryID, "Has hit", self.combatLib[y].name, "For", salvoDamage, "Damage!")
                    salvoDamage = 0
                    
            #run broadside guns
            broadsideTotalDamage = 0
            bN = 0
            for gunBattery in self.combatLib[x].broadsideBattery:
                if bN % 2 == 0 and (tSec % gunBattery.gunStats['RLD']) == 0:
                    if self.hitCalc(gunBattery, self.combatLib[x].shipStats['ACC'], self.combatLib[y].shipStats['EVA']) == True:
                        salvoDamage += self.damageCalc(gunBattery ,self.combatLib[x].shipStats['FP'], self.combatLib[x].shipStats['luck'],
                                                    self.combatLib[y].shipStats['luck'], len(self.combatLib[x].broadsideBattery))
                    else:
                        salvoDamage += 0
                    self.combatLib[y].takeDamage(salvoDamage)
                    broadsideTotalDamage += salvoDamage
                    salvoDamage = 0
                bN += 1
                if bN == len(self.combatLib[x].broadsideBattery) and broadsideTotalDamage > 0:
                    print(self.combatLib[x].name, "Broadside Barrage Has hit", self.combatLib[y].name, "For", broadsideTotalDamage, "Damage!")

            x, y = 1, 0


    #Passes a combatSequence every second
    def timedCombatGame(self, m = 2):
        nowTime = time.time()
        stepTime = time.time()
        futureTime = nowTime + self.comTime
        timeSec = 0
        n = 0
        while time.time() < futureTime:
            n += 1
            varTime = time.time()
            #run a cycle every 1sec
            if (stepTime // 1) < (varTime // 1):
                stepTime = varTime
                timeSec += 1
                self.runGame(timeSec, m)
                print("Calculations:", n)
                n = 0

    #Passes a query based combat system
    def testCombatGame(self, m = 2):
        noQuery = ['No', 'no', 'N', 'n']
        insQuery = ['I', 'Inspect', 'i', 'inspect', 'ins']
        testC = 0
        tSec = 0
        while testC == 0:
            tSec += 1
            self.runGame(tSec, m)
            p = input("Continue?:")
            if p in noQuery:
                testC = 1
            elif p in insQuery:
                self.combatLib[0].fullInspect()
                self.combatLib[1].fullInspect()

    
    def hitCalc(self, gunBattery, hACC, jEVA):
        hitrate = (hACC - jEVA) + gunBattery.gunStats['HIT']
        ranVal = randint(1, 100)

        if hitrate >= ranVal:
            return True
        else:
            return False

    
    def damageCalc(self, gunBattery, hFP, hLuck, jLuck, ammountOfBat):
        critRate = hLuck - jLuck + 5
        damageMult = 1
        damage = 0
        ranVal = randint(1,100)

        if critRate >= ranVal:
            damageMult = 1.25 + (hLuck / 100)

        damage = ((gunBattery.gunStats['ATK'] + (hFP // ammountOfBat)) * damageMult) 
        return damage


"""-----------------------------------------------------------------------"""

print("combatGameT")