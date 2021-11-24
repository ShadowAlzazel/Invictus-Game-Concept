hexCoord = 29
length = 5
width = 5

if not (hexCoord + 1) % length == 0:
    print('Can move Right')
else:
    print('Cannot move Right')

if not hexCoord % length == 0:
    print('Can Move Left')
else: 
    print("Cannot move Left")

if not (hexCoord >= length * (width - 1)) and not ((hexCoord // length) % 2 == 1 and (hexCoord + 1) % length == 0):
    print('Can Move Upright')
else: 
    print("Cannot move upright")

if not (hexCoord) >= length * (width - 1) and not((hexCoord // length) % 2 == 0 and hexCoord % length == 0):
    print('Can Move Upleft')
else: 
    print("Cannot move upleft")

if not (hexCoord) // length == 0 and not ((hexCoord // length) % 2 == 1 and (hexCoord + 1) % length == 0):
    print('Can Move downright')
else: 
    print("Cannot move downright")

if not (hexCoord) // length == 0 and not ((hexCoord // length) % 2 == 0 and hexCoord % length == 0):
    print('Can Move downleft')
else: 
    print("Cannot move downleft")