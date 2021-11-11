from spaceField import *
from shipCombat import turnCombatGame
from fleetManager import *
from fleetLogger import *
from shipCreater import *

aoe = createCombatSpace(20, 20, 0) 

#create fleet 1
f1 = spaceFleet(astraFleets[0]['ASC']['fleetNames'][0], 'ASC')
fleetLaunch(f1)

#create fleet 2
f2 = spaceFleet('Pirate 1', 'UVF')
createShips(f2.fleetShips, 'UVFF', 7)

#spawn the fleet in the zone
f1.spawnFleet(aoe)
f2.spawnFleet(aoe)

#create the game
civ = turnCombatGame(aoe)
civ.runGame()

