from shipCreater import *
from fleetManager import *
from fleetLogger import *
from gameField import *
from spaceField import *
from mainGame import *

aoe = createCombatSpace(14, 10, 0)

#fleetASCS = spaceFleet(astraFleets[0]['ASC']['fleetNames'][1], 'ASC')
#fleetLaunch(fleetASCS) 

fleet2 = spaceFleet(astraFleets[0]['ASC']['fleetNames'][2], 'ASC')
fleetLaunch(fleet2)

fleetXNFF = spaceFleet(astraFleets[0]['XNFF']['fleetNames'][0], 'XNFF')
fleetLaunch(fleetXNFF) 

#fleetASCS.spawnFleet(aoe, 30)

fleet2.spawnFleet(aoe, 40)
fleetXNFF.spawnFleet(aoe, 104)



aTurnGame = turnCombatGame(aoe)

#start game
levelGame(aTurnGame)