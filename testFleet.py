#fleet tester
from fleetManager import *
from fleetLogger import *
from spaceField import *
from shipCreater import *

aoe = createCombatSpace(15, 15, 0) 

f1 = spaceFleet(astraFleets[0]['ASC']['fleetNames'][1], 'ASC')
fleetLaunch(f1)

f2 = spaceFleet('Pirate 1', 'UVF')
createShips(f2.fleetShips, 'UVFF', 7)


"""
fleetXLFF = spaceFleet('Xtralis New Frontier Fleet', 'XNFF')
fleetXLFF.fleetShips.append(VittorioVenetoClass(302, 'Littorio'))
fleetXLFF.fleetShips.append(VittorioVenetoClass(304, 'Roma Imperio'))
fleetXLFF.fleetShips.append(ShimakazeClass(4404, 'Himiwari'))

fleetXLFF.fleetShips[0].command = 'XNFF'
fleetXLFF.fleetShips[1].command = 'XNFF'
fleetXLFF.fleetShips[2].command = 'XNFF'
"""