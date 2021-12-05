import json 

def starLevelOpen():
    with open("levelManager\starLevels.json", "r") as game_levels_file:
        game_levels = game_levels_file
        return json.load(game_levels)