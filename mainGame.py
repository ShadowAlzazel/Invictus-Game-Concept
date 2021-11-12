import pygame
from pygame.constants import K_ESCAPE, KEYDOWN
from gameField import *
from spaceField import *
from shipCreater import *

aoe = createCombatSpace(10, 10, 0)

fleetXLFF = []
fleetXLFF.append(VittorioVenetoClass(302, 'Littorio'))
fleetXLFF.append(VittorioVenetoClass(304, 'Roma Imperio'))
fleetXLFF[0].command = 'XLFF'
fleetXLFF[1].command = 'XLFF'

aoe.addCustomEntity(aoe.starSpaceHexes[2], fleetXLFF[0])
aoe.addCustomEntity(aoe.starSpaceHexes[15], fleetXLFF[1])

#start game
def gameStart():
    turnGame = turnCombatGame(aoe)

    gameScreen = pygame.display.set_mode((LENGTH, WIDTH))
    gameScreen.fill(SCREEN_RGB)

    HEX_ENTF_IMG.convert()
    HEX_Y_IMG.convert()

    pygame.init()

    combatGameBoard = spaceGameBoard(turnGame.opsSpace.l, turnGame.opsSpace.w)

    #create window
    pygame.display.update()
    pygame.display.set_caption("ASCS Fleet Manager")
    pygame.display.set_icon(GAME_ICON)

    gameRunning = True
    gameClock = pygame.time.Clock()

    while gameRunning:
        gameClock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                gameRunning = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                someMousePos = pygame.mouse.get_pos()
                hexIndex = combatGameBoard.getCoordMouse(someMousePos)
                if hexIndex >= 0:
                    turnGame.selectHex(turnGame.opsSpace.starSpaceHexes[hexIndex])

                print(hexIndex)

        combatGameBoard.drawHexes(gameScreen, turnGame.opsSpace)
        pygame.display.update()

    pygame.quit()

gameStart()