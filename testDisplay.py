from gameField import *
from spaceField import *
from shipCreater import *

aoe = createCombatSpace(10, 10, 0)

fleetXLFF = []
fleetXLFF.append(VittorioVenetoClass(302, 'Littorio'))
fleetXLFF.append(VittorioVenetoClass(304, 'Roma Imperio'))

aoe.addCustomEntity(aoe.starSpaceHexes[2], fleetXLFF[0])
aoe.addCustomEntity(aoe.starSpaceHexes[15], fleetXLFF[1])

gameStart(aoe)