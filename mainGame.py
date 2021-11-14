import pygame
from pygame.constants import K_ESCAPE, K_F4, K_LALT, KEYDOWN, K_e, K_i, K_x, K_z
from gameField import *

#start game
def gameOPS(turnGame):

    gameScreen = pygame.display.set_mode((LENGTH, WIDTH))
    gameScreen.blit(FIT_SPACE, (0, 0))

    #start pygame
    pygame.init()
    combatGameBoard = spaceGameBoard(turnGame.opsSpace.l, turnGame.opsSpace.w, HEX_SIZE)

    #create window
    pygame.display.update()
    pygame.display.set_caption("ASCS Fleet Manager")
    pygame.display.set_icon(GAME_ICON)
    combatGameBoard.drawHexes(gameScreen, turnGame.opsSpace)
    pygame.display.update()

    gameRunning = True
    gameClock = pygame.time.Clock()

    while gameRunning:
        gameClock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE) or ((event.type == KEYDOWN and event.key == K_LALT) and (event.type == KEYDOWN and event.key == K_F4)):
                gameRunning = False

            if event.type == KEYDOWN and event.key == K_e:
                print('Fleet Turn Ended')
                turnGame.fleetTurn()
                combatGameBoard.drawHexes(gameScreen, turnGame.opsSpace)

            if event.type == KEYDOWN and event.key == K_i:
                if turnGame.selectedHex:
                    turnGame.selectedHex.entity.fullInspect()

            if event.type == KEYDOWN and event.key == K_z:
                combatGameBoard.zoomInHex()
                combatGameBoard.drawHexes(gameScreen, turnGame.opsSpace, turnGame.selectedHex)

            if event.type == KEYDOWN and event.key == K_x:
                combatGameBoard.zoomOutHex()
                combatGameBoard.drawHexes(gameScreen, turnGame.opsSpace, turnGame.selectedHex)

            if event.type == pygame.MOUSEBUTTONDOWN:
                someMousePos = pygame.mouse.get_pos()
                hexIndex = combatGameBoard.getCoordMouse(someMousePos)
                if hexIndex >= 0:
                    turnGame.selectHex(turnGame.opsSpace.starSpaceHexes[hexIndex])
                combatGameBoard.drawHexes(gameScreen, turnGame.opsSpace, turnGame.selectedHex)
           
                print(hexIndex)

        #combatGameBoard.drawHexes(gameScreen, turnGame.opsSpace)
            pygame.display.update()




    pygame.quit()
