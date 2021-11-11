#fleet tester
from fleetManager import *
from fleetLogger import *
from spaceField import *
from shipCreater import *

aoe = createCombatSpace(15, 15, 0) 

f1 = spaceFleet(astraFleets[0]['ASC']['fleetNames'][0], 'ASC')
fleetLaunch(f1)

f2 = spaceFleet('Pirate 1', 'UVF')
createShips(f2.fleetShips, 'UVFF', 7)