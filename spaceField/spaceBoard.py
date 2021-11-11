#print a game board

def makeGameBoard(opsSpace):
    n = 1
    lane = []
    row = ''
    indent = False
    if opsSpace.w % 2 == 0:
        indent = True
    print('----------------------MAP----------------------')

    def showHexGrid(opsHex):
        if opsHex.empty == True:
            return '[ ]'
        else:
            s = opsHex.entity.command
            return ''.join(['[', str(s[0]), ']'])

    while n != len(opsSpace.starSpaceHexes) + 1:
        lane.append(showHexGrid(opsSpace.starSpaceHexes[-n]))
        row = ''.join([showHexGrid(opsSpace.starSpaceHexes[-n]), row])
        if len(lane) == opsSpace.l:
            if indent:
                print(' ', row)
            elif not indent:
                print(row)
            indent = not indent
            lane = []
            row = ''
        n += 1 


def showShipVision(opsSpace, someShip):
    n = 1
    lane = []
    row = ''
    indent = False
    if opsSpace.w % 2 == 0:
        indent = True
    print('----------------------MAP----------------------')
#show ship vison

    def showHexGrid(opsHex):
        if opsHex.empty == True:
            return '[ ]'
        elif opsHex.entity.vesselID == someShip.vesselID:
            return ''.join(['[', '*', ']'])
        else:
            s = opsHex.entity.command
            return ''.join(['[', str(s[0]), ']'])

    while n != len(opsSpace.starSpaceHexes) + 1:
        lane.append(showHexGrid(opsSpace.starSpaceHexes[-n]))
        row = ''.join([showHexGrid(opsSpace.starSpaceHexes[-n]), row])
        if len(lane) == opsSpace.l:
            if indent:
                print(' ', row)
            elif not indent:
                print(row)
            indent = not indent
            lane = []
            row = ''
        n += 1 