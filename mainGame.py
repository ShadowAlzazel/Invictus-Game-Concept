import pygame
from pygame.constants import K_DOWN, K_ESCAPE, K_F4, K_LALT, K_LEFT, K_RIGHT, K_SPACE, K_UP, KEYDOWN, KEYUP, K_c, K_e, K_i, K_m, K_r, K_x, K_z
from gameField import *

#start game
def levelGame(turnLevel):

    
    gameScreen = pygame.display.set_mode((LENGTH, WIDTH))
    gameScreen.blit(FIT_SPACE, (0, 0))

    #start pygame
    pygame.init()
    combatGameBoard = spaceGameBoard(turnLevel.opsSpace.l, turnLevel.opsSpace.w, HEX_SIZE)

    #create window
    pygame.display.update()
    pygame.display.set_caption("ASCS Fleet Manager")
    pygame.display.set_icon(GAME_ICON)

    animateGridHexes = pygame.USEREVENT + 1
    pygame.time.set_timer(animateGridHexes, 250)

    combatGameBoard.drawHexes(gameScreen, turnLevel.opsSpace)
    pygame.display.update()


    #variables
    moveUp, moveDown, moveLeft, moveRight = False, False, False, False

    gameRunning = True
    gameClock = pygame.time.Clock()

    while gameRunning:
        gameClock.tick(FPS)

        if moveUp:
            combatGameBoard.windowMoveY -= 3
        if moveDown:
            combatGameBoard.windowMoveY += 3
        if moveLeft:
            combatGameBoard.windowMoveX -= 3
        if moveRight:
            combatGameBoard.windowMoveX += 3
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE) or ((event.type == KEYDOWN and event.key == K_LALT) and (event.type == KEYDOWN and event.key == K_F4)):
                print("Quiting")
                gameRunning = False

            #window movement
            if event.type == KEYDOWN and event.key == K_UP:
                moveUp = True
            if event.type == KEYUP and event.key == K_UP:
                moveUp = False

            if event.type == KEYDOWN and event.key == K_DOWN:
                moveDown = True
            if event.type == KEYUP and event.key == K_DOWN:
                moveDown = False

            if event.type == KEYDOWN and event.key == K_LEFT:
                moveLeft = True
            if event.type == KEYUP and event.key == K_LEFT:
                moveLeft = False

            if event.type == KEYDOWN and event.key == K_RIGHT:
                moveRight = True
            if event.type == KEYUP and event.key == K_RIGHT:
                moveRight = False

            #reset window
            if event.type == KEYDOWN and event.key == K_SPACE:
                combatGameBoard.windowMoveX = 0
                combatGameBoard.windowMoveY = 0

            if event.type == KEYDOWN and event.key == K_e:
                print('Fleet Turn Ended')
                turnLevel.fleetTurn()
                combatGameBoard.drawHexes(gameScreen, turnLevel.opsSpace)

            if event.type == KEYDOWN and event.key == K_i:
                if turnLevel.selectedHex:
                    turnLevel.selectedHex.entity.fullInspect()

            #zooming
            if event.type == KEYDOWN and event.key == K_z:
                combatGameBoard.zoomInHex()

            if event.type == KEYDOWN and event.key == K_x:
                combatGameBoard.zoomOutHex()

            if event.type == KEYDOWN and event.key == K_c:
                if turnLevel.selectedHex:
                    combatGameBoard.centerHex = turnLevel.selectedHex.hexCoord

            if event.type == animateGridHexes:
                combatGameBoard.aniHexes()
                combatGameBoard.drawHexes(gameScreen, turnLevel.opsSpace, turnLevel.selectedHex) 

            if event.type == pygame.MOUSEBUTTONDOWN:
                someMousePos = pygame.mouse.get_pos()
                hexIndex = combatGameBoard.getMouseHex(someMousePos)
                if hexIndex >= 0:
                    turnLevel.selectHex(turnLevel.opsSpace.starHexes[hexIndex])
                print(hexIndex)

        combatGameBoard.drawHexes(gameScreen, turnLevel.opsSpace, turnLevel.selectedHex)    
        pygame.display.update()

    pygame.quit()
