from shipCreater import *
from spaceField import *
from shipCombat import turnCombatGame



fleetASCS = []
fleetASCS.append(EssexClass(66, 'Essex'))
fleetASCS.append(EssexClass(67, 'Intrepid'))
fleetASCS.append(ApocalypseClass(89, 'Kirov'))
fleetASCS.append(ApocalypseClass(101, 'Odessa'))
fleetASCS.append(NewJerseyClass(69, 'New Jersey'))

fleetXLFF = []
fleetXLFF.append(VittorioVenetoClass(302, 'Littorio'))
createShips(fleetXLFF, 'XLFF', 4)

aoe = createCombatSpace(15, 15, 0)

m = 1
for a in fleetASCS:
    aoe.addCustomEntity(aoe.starSpaceHexes[(m * 15) + 2], a)
    m += 1

n = 2
for x in fleetXLFF:
    print(x)
    x.command = 'XLFF'
    aoe.addCustomEntity(aoe.starSpaceHexes[(n * 15) - 3], x)
    n += 1


civ = turnCombatGame(aoe)
civ.runGame()
