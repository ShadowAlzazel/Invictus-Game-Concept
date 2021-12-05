import json 

def starLevelOpen():
    with open("levelManager\starLevels.json", "r") as starLevelsFile:
        starLevels = starLevelsFile
        return json.load(starLevels)