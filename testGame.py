from shipCreater import *
from fleetManager import *
from fleetLogger import *
from gameField import *
from spaceField import *
from mainGame import *


aoe = createCombatSpace(10, 10, 0)

fleetASCS = spaceFleet(astraFleets[0]['ASC']['fleetNames'][0], 'ASC')
fleetLaunch(fleetASCS)

fleetXLFF = spaceFleet('Xtralis Line Frontier Fleet', 'XNFF')
fleetXLFF.fleetShips.append(VittorioVenetoClass(302, 'Littorio'))
fleetXLFF.fleetShips.append(VittorioVenetoClass(304, 'Roma Imperio'))
fleetXLFF.fleetShips[0].command = 'XLFF'
fleetXLFF.fleetShips[1].command = 'XLFF'

fleetASCS.spawnFleet(aoe)
fleetXLFF.spawnFleet(aoe)

aTurnGame = turnCombatGame(aoe)

#start game
gameOperationSpace(aTurnGame)