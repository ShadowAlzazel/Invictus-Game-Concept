from shipCreater import *
from fleetManager import *
from fleetLogger import *
from gameField import *
from spaceField import *
from mainGame import *

aoe = createCombatSpace(12, 10, 0)

fleetASCS = spaceFleet(astraFleets[0]['ASC']['fleetNames'][1], 'ASC')
fleetLaunch(fleetASCS)
fleetXNFF = spaceFleet(astraFleets[0]['XNFF']['fleetNames'][0], 'XNFF')
fleetLaunch(fleetXNFF)

fleetASCS.spawnFleet(aoe, 30)
fleetXNFF.spawnFleet(aoe, 114)

aTurnGame = turnCombatGame(aoe)

#start game
gameOPS(aTurnGame)