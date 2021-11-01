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
            for mainBattery in self.combatLib[x].mainArm:
                if (tSec % mainBattery.gunStats['RLD']) == 0:
                    if self.hitCalc(mainBattery, self.combatLib[x].shipStats['ACC'], self.combatLib[y].shipStats['EVA']) == True:
                        salvoDamage += self.damageCalc(mainBattery ,self.combatLib[x].shipStats['FP'], self.combatLib[x].shipStats['luck'],
                                                    self.combatLib[y].shipStats['luck'], len(self.combatLib[x].mainArm))
                    else:
                        salvoDamage += 0
                    self.combatLib[y].takeDamage(salvoDamage)
                    print(mainBattery.armaID, "Has hit", self.combatLib[y].name, "For", salvoDamage, "Damage!")
                    salvoDamage = 0
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
                print(n)
                n = 0

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
