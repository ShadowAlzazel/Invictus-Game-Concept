from shipCreater import *
from fleetManager import *
from fleetLogger import *
from gameField import *
from spaceField import *
from mainGame import *

aoe = createCombatSpace(12, 10, 0)

fleetASCS = spaceFleet(astraFleets[0]['ASC']['fleetNames'][0], 'ASC')
fleetLaunch(fleetASCS)

fleetXLFF = spaceFleet('Xtralis New Frontier Fleet', 'XNFF')
fleetXLFF.fleetShips.append(VittorioVenetoClass(302, 'Littorio'))
fleetXLFF.fleetShips.append(VittorioVenetoClass(304, 'Roma Imperio'))
fleetXLFF.fleetShips.append(ShimakazeClass(4404, 'Himiwari'))

fleetXLFF.fleetShips[0].command = 'XNFF'
fleetXLFF.fleetShips[1].command = 'XNFF'
fleetXLFF.fleetShips[2].command = 'XNFF'

fleetASCS.spawnFleet(aoe)
fleetXLFF.spawnFleet(aoe)

aTurnGame = turnCombatGame(aoe)

#start game
gameOPS(aTurnGame)