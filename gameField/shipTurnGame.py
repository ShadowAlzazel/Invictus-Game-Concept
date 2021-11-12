#a turn based combat game
from gameField.gameBoard import *
from random import randint

class turnCombatGame:
    Query = {'No': ['No', 'no', 'N', 'n'], 'Yes': ['Yes', 'yes', 'Y', 'y'], 
            'Inspect': ['I', 'Inspect', 'i', 'inspect', 'ins'], 'Skip': ['Skip', 'skip', 'S', 's'],
            'Move': ['Move', 'move', 'm', 'M'], 'End': ['End', 'end', 'finish', 'Finish', 'E', 'e'],
            'Attack': ['Attack', 'attack', 'atk', 'Atk', 'a', 'A', 'ATK'], 'AutoAttack': ['AutAttack', 'autoattack', 'auto', 'aa', 'AA']
            }

    def __init__(self, operationSpace):
        self.opsSpace = operationSpace
        self.activeShips = operationSpace.spaceEntities['shipObject']
        self.activeFleets = operationSpace.fleetEntities
        self.gameTurn = 0
        self.selectedHex = None 
        self.currentFleetTurn = 'XLFF'   #None
        for s in self.activeShips:
            s.shipMovement = 0
            s.shipAttacks = 0
            s.shipTurn = True 

    #select ship
    def selectHex(self, aHex):
        print('ClickHEx')
        print(aHex.empty)
        if self.selectedHex:
            result = self._moveShipAction(aHex)
            if not result:
                self.selectedHex = None 
                self.selectHex(aHex)

        aShip = aHex.entity
        if not aHex.empty and self.currentFleetTurn == aShip.command:
            self.selectedHex = aHex
            return True

        return False 

    #hit calculator for a gun
    def gunHitCalc(self, gunBattery, aShipACC, bShipEVA):
        hitRate = (aShipACC - bShipEVA) + gunBattery.gunStats['HIT']
        randHit = randint(1, 100)
        if hitRate > randHit:
            return True
        else:
            return False

    #damage calculator for a gun
    def gunDamageCalc(self, gunBattery, aShipFP, aShipLuck, bShipLuck, batDistro):
        critRate = aShipLuck - bShipLuck + 5
        damageMult = 1
        damage = 0
        randCrit = randint(1, 100)
        if critRate > randCrit:
            damageMult = 1.25 + (aShipLuck / 100)

        damage = (gunBattery.gunStats['ATK'] + (aShipFP // batDistro) * damageMult)
        return damage


    #all availabe ship action query 
    def shipActions(self, aShip):
        #self.opsSpace.showMap() 
        shipturnActive = True

        while shipturnActive:   
            mes = aShip.vesselID + ' ' + aShip.name +  ' ' + "Awaiting Orders...: "
            playerInput = input(mes)

            if playerInput in self.Query['End']:
                print("Ship Turn Ended! ")
                aShip.shipTurn = False
                shipturnActive = False
                return 


            if playerInput in self.Query['Skip']:
                print("Ship Skipped! ")
                shipturnActive = False
                return

            elif playerInput in self.Query['Move']:
                if aShip.shipMovement != 0:
                    if self._moveShipAction(aShip):
                        aShip.shipMovement -= 1 
                else: 
                    print("No More Moves Available")

            elif playerInput in self.Query['Attack']:
                if aShip.shipAttacks != 0:
                    if self.attackShipAction(aShip):
                        aShip.shipAttacks -= 1
                else: 
                    print('No Attacks Available')

            elif playerInput in self.Query['Inspect']:
                aShip.fullInspect()

            elif playerInput in self.Query['AutoAttack']:
                print("AutoAttack")

    #attack action; check for minimum  range, and guns in ranges
    def attackShipAction(self, aShip):
        nID = 0
        if not aShip.gunsReady():
            print("No guns loaded")
            return True

        nearbyShips = aShip.findTargets()
        if not nearbyShips:
            print("No ships in minimmum range")
            return False 
        else: 
            for k in nearbyShips:
                print("Targets within minimmum range:", k.entity.vesselID, k.entity.name, "At Hex", k.coord['hexNum'], 'TiD:', nID)
                nID += 1


        #authorize attack order
        authAtk = False
        numStrings = [str(c) for c in range(0,100)] 
        while not authAtk:
            newOrder = input("Choose a target to fire: ")
            if newOrder in self.Query['No'] or newOrder in self.Query['Skip'] or newOrder in self.Query['End']:
                print("Fire Sequence Failed")
                return False
            elif newOrder in numStrings:
                authAtk = True  
            else: 
                print("Unknown authorization")

        #attack input target and end attacks
        newOrder = int(newOrder)
        if newOrder < nID:
            self.shipSalvoAction(aShip, nearbyShips[newOrder].entity)
        else:
            print("Unknown target")
            #return True 

    #move ship on board
    def _moveShipAction(self, aHex):
        result = False
        if aHex.empty and (aHex in self.selectedHex.neighbors):
            selectedShip = self.selectedHex.entity
            result = self.opsSpace.moveClickEntity(selectedShip, aHex) 
        return result


    #fire all guns in range 
    def shipSalvoAction(self, aShip, bShip):
        shipExists = [bShip]
        #check if guns are loaded
        gunToFire = []
        for p in aShip.primaryBattery:
            if p.gunLoadTime == p.gunStats['RLD']:
                gunToFire.append(p)
        for s in aShip.secondaryBattery:
            if s.gunLoadTime == s.gunStats['RLD']:
                gunToFire.append(s)
        bEven = 0      
        for b in aShip.broadsideBattery:
            if b.gunLoadTime == b.gunStats['RLD'] and bEven % 2 == 0:
                gunToFire.append(b)
            elif bEven % 2 == 1:
                b.gunLoadTime = 0 #make half the boradside not reload 
            bEven += 1

        totalDamage = 0
        for g in gunToFire:
            if not shipExists:
                print("ship Destroyed!")
            salvoDamage = 0
            trueDamage = 0
            if aShip.gunInRange(g, bShip):
                batPow = 0  
                if g in aShip.primaryBattery:
                    batPow = aShip.shipStats['FP'] // len(aShip.primaryBattery)
                elif g in aShip.secondaryBattery:
                    batPow = aShip.shipStats['FP'] // len(aShip.secondaryBattery)
                elif g in aShip.broadsideBattery:
                    batPow = aShip.shipStats['FP'] // len(aShip.broadsideBattery)

                if self.gunHitCalc(g, aShip.shipStats['ACC'], bShip.shipStats['EVA']) == True:
                    salvoDamage += self.gunDamageCalc(g, aShip.shipStats['FP'], aShip.shipStats['LCK'], bShip.shipStats['LCK'], batPow)

                trueDamage = bShip.takeDamage(salvoDamage)
                if trueDamage > 0:
                    print(g.batteryID, "Has Hit", bShip.name, "For", trueDamage, "Damage!")
                g.gunLoadTime = 0

            totalDamage += trueDamage
            salvoDamage = 0

        print(aShip.vesselID, aShip.name, "Has done", totalDamage, "Total Damage to", bShip.vesselID, bShip.name)

    #fleet Actions
    def fleetActions(self, aFleet):
        #create/add new actions to fleet ships
        for t in aFleet.fleetShips:
            t.shipMovement = t.shipStats['SPD']
            t.shipAttacks = 1
            t.reloadGuns()
            t.shipTurn = True

        fleetTurn = True
        while fleetTurn:
            n = 0
            for s in aFleet.fleetShips:
                if s.shipTurn:
                    self.shipActions(s)
                else:
                    n += 1

            if n == len(aFleet.fleetShips):
                print("No turns available for all ships in", aFleet.name)      
                fleetTurn = False   

    #start a new turn
    def runATurn(self):
        for x in self.activeFleets:
            self.fleetActions(x)

    #run game function
    def runGame(self):
        gameRunning = True
        while gameRunning:
            self.runATurn()
            play = input("Continue Game?: ")
            if play in self.Query['No'] or play in self.Query['End']:
                gameRunning = False
            else:
                self.gameTurn += 1
