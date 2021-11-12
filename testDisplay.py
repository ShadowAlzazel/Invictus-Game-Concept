from gameField import *
from spaceField import *
from shipCreater import *

aoe = createCombatSpace(10, 10, 0)

fleetXLFF = []
fleetXLFF.append(VittorioVenetoClass(302, 'Littorio'))

aoe.addCustomEntity(aoe.starSpaceHexes[2], fleetXLFF[0])
gameStart(aoe)