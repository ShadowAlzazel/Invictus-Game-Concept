#levels 
from gameField.gameClass import spaceField
from shipCreater import *
from fleetManager import *
from fleetLogger import *
from spaceField import *

class level():

    def __init__(self, l, y, o, fleets, loc):
        self.areaOfEngagement =  createCombatSpace(l, y, o)
        self.levelFleets = [x for x in fleets]
        self.fleetSpawns = loc 
        for i, x in enumerate(self.levelFleets):
            fleetLaunch(x)
            x.spawnFleet(self.areaOfEngagement, loc[i])
        self.areaGame = spaceField(self.areaOfEngagement)


#fleet1 = spaceFleet(astraFleets[0]['ASC']['fleetNames'][1], 'ASC')
#fleet2 = spaceFleet(astraFleets[0]['XNFF']['fleetNames'][0], 'XNFF')
#level1 = level(14, 10, 0 ,(fleet1, fleet2), [40, 104])
