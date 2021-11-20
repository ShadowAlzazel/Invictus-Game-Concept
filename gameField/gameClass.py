#a turn based combat game
from random import randint

class spaceField:
    #Query = {'No': ['No', 'no', 'N', 'n'], 'Yes': ['Yes', 'yes', 'Y', 'y'], 
    #        'Inspect': ['I', 'Inspect', 'i', 'inspect', 'ins'], 'Skip': ['Skip', 'skip', 'S', 's'],
    #        'Move': ['Move', 'move', 'm', 'M'], 'End': ['End', 'end', 'finish', 'Finish', 'E', 'e'],
    #        'Attack': ['Attack', 'attack', 'atk', 'Atk', 'a', 'A', 'ATK'], 'AutoAttack': ['AutAttack', 'autoattack', 'auto', 'aa', 'AA']
    #        }

    def __init__(self, operationSpace):
        self.opsSpace = operationSpace
        self.gameShips = operationSpace.spaceEntities['shipObject']
        self.gameFleets = operationSpace.fleetEntities
        self.gameTurn = 0
        self.selectedHex = None #usually a hex
        self.activeFleet = self.gameFleets[0]
        self.activeFleetIndex = 0
        for f in self.gameFleets:
            self._updateShips(f)     


    #fleet Actions
    def fleetTurn(self):
        self.selectedHex = None 
        q = self.activeFleetIndex
        if q == len(self.gameFleets) - 1:
            self.gameTurn += 1
            self.activeFleetIndex = 0
            self.activeFleet = self.gameFleets[0]
        else:
            self.activeFleetIndex += 1
            self.activeFleet = self.gameFleets[q + 1]
        self._updateShips(self.activeFleet)


    #update ships in fleet turn
    def _updateShips(self, aFleet):
        for s in aFleet.fleetShips:
            s.shipMovement = s.shipStats['SPD']
            s.shipAttacks = 1
            s.shipActive = True
            s.reloadGuns()
            s.rechargeDef()


    #select shiphex
    def selectHex(self, aHex):
        #check if there is a previously selected hex
        if self.selectedHex:
            #check if hexShip has any actions
            if self.selectedHex.entity.shipMovement == 0:
                nearbyShipHexes = self.selectedHex.entity.findTargets()
                if not nearbyShipHexes:
                    self.selectedHex.entity.shipActive = False

            result = self._shipActions(aHex)
            if not result:
                self.selectedHex = None 
                self.selectHex(aHex)

        aShip = aHex.entity
        #can only select a ship
        if not aHex.empty and self.activeFleet.fleetCommand[0:3] == aShip.command[0:3]:
            self.selectedHex = aHex
            return True
        return False 
        

    #all availabe ship actions
    def _shipActions(self, aHex):
        result = False
        if not self.selectedHex.entity.shipActive:
            print("No possible actions left")
            return False

        #check if moves available
        if self.selectedHex.entity.shipMovement != 0:
            result = self._moveShipAction(aHex)     
        else:
            print("No Movements available")   

        #if no movement triggered, check for attacks
        if not result:
            result = self._attackShipAction(aHex)

        return result


    #attack action; check for minimum  range, and guns in ranges
    def _attackShipAction(self, aHex):
        aShip = self.selectedHex.entity
        if not aShip.gunsReady():
            aShip.shipAttacks = 0
            print("No guns loaded")
            return False

        #selected hex must be a target
        nearbyShipHexes = aShip.findTargets()
        if not aHex in nearbyShipHexes:
            return False

        result = self._shipSalvoAction(aShip, aHex.entity)
        return result


    #move ship on board
    def _moveShipAction(self, aHex):
        result = False
        selectedShip = self.selectedHex.entity
        #check if selcted hex direction does not match orientation
        if aHex.empty and (aHex in self.selectedHex.neighbors) and (aHex.directions[selectedShip.orientation] != self.selectedHex.hexCoord or selectedShip.shiptype == 'DD' or selectedShip.shiptype == 'CS'):
            if selectedShip.shiptype == 'BB' and self.opsSpace.starHexes[aHex.directions[selectedShip.orientation]] in self.selectedHex.neighbors:
                return result

            if selectedShip.shipMovement != 0:
                result = self.opsSpace.moveClickEntity(selectedShip, aHex)
                if result:
                    selectedShip.shipMovement -= 1
                    #check if hex controlled
                    if selectedShip.shipMovement != 0:
                        enemyControlled = selectedShip.radar.findRadarTargets(1, aHex)
                        enemyNearby = selectedShip.findTargets(1)
                        if enemyControlled or enemyNearby:
                            selectedShip.shipMovement -= 1

            else:
                print("No movements left!") 
        return result


    #fire all guns in range 
    def _shipSalvoAction(self, aShip, bShip):
        #check if guns are loaded
        gunToFire = aShip.gunsReady()
        broadSideE = 0
        for s in gunToFire:
            if s in aShip.armaments['broadsideBattery']:
                if broadSideE % 2 == 1:
                    s.gunLoadTime = 0
                    gunToFire.remove(s)
                broadSideE += 1

        #get the distance
        bDistance = aShip.rangeFinder(bShip)

        totalDamage = 0
        for g in gunToFire:
            if not bShip.operational:
                print("ship Destroyed!")
                return True
            salvoDamage = 0
            trueDamage = 0
            if g.gunStats['RNG'] >= bDistance:
                #find FP distribution ammong batteries
                batPow = 0  
                if g in aShip.armaments['primaryBattery']:
                    batPow = aShip.shipStats['FP'] // len(aShip.armaments['primaryBattery'])
                elif g in aShip.armaments['secondaryBattery']:
                    batPow = aShip.shipStats['FP'] // len(aShip.armaments['secondaryBattery'])
                elif g in aShip.armaments['broadsideBattery']:
                    batPow = aShip.shipStats['FP'] // len(aShip.armaments['broadsideBattery'])

                for a in range(0, g.gunStats['QNT']):
                    if self.gunHitCalc(g.gunStats['HIT'], aShip.shipStats['ACC'], bShip.shipStats['EVA']) is True:
                        salvoDamage += self.gunDamageCalc(g.gunStats['ATK'], aShip.shipStats['FP'], aShip.shipStats['LCK'], bShip.shipStats['LCK'], batPow)

                trueDamage = bShip.takeDamage(salvoDamage)
                if not bShip.operational:
                    m = bShip.placeHex.hexCoord
                    self.gameShips.remove(bShip) 
                    self.opsSpace.hexesFull.remove(self.opsSpace.starHexes[m])
                    self.opsSpace.starHexes[m].entity = []
                    self.opsSpace.starHexes[m].empty = True
                    trueDamage = 0
                    #del bShip
                    return True

                if trueDamage > 0:
                    print(g.batteryID, "Has Hit", bShip.name, "For", trueDamage, "Damage!")
                g.gunLoadTime = 0
            totalDamage += trueDamage
            salvoDamage = 0
        print(aShip.vesselID, aShip.name, "Has done", totalDamage, "Total Damage to", bShip.vesselID, bShip.name)
        return True


    #hit calculator for a gun
    def gunHitCalc(self, aShipGunHit, aShipACC, bShipEVA):
        hitRate = (aShipACC - bShipEVA) + aShipGunHit
        randHit = randint(1, 100)
        if hitRate > randHit:
            return True
        else:
            return False


    #damage calculator for a gun
    def gunDamageCalc(self, aShipGunAtk, aShipFP, aShipLCK, bShipLCK, batDistro):
        critRate = aShipLCK - bShipLCK + 5
        damageMult = 1
        damage = 0
        randCrit = randint(1, 100)
        if critRate > randCrit:
            damageMult = 1.25 + (aShipLCK / 100)

        damage = (aShipGunAtk + (aShipFP // batDistro) * damageMult)
        return damage