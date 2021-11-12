import pygame
from pygame.constants import K_ESCAPE, KEYDOWN
from gameField.gameBoard import *
from gameField.gameAssets import *

#start game
def gameStart(operationSpace):

    gameScreen = pygame.display.set_mode((LENGTH, WIDTH))
    gameScreen.fill(SCREEN_RGB)

    HEX_ENTF_IMG.convert()
    HEX_Y_IMG.convert()

    pygame.init()

    combatGameBoard = spaceGameBoard(operationSpace.l, operationSpace.w)

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
                hexIndex  = combatGameBoard.getCoordMouse(someMousePos)
                if hexIndex >= 0:
                    print(operationSpace.starSpaceHexes[hexIndex].empty)
                    if not operationSpace.starSpaceHexes[hexIndex].empty:
                        operationSpace.moveEntity(operationSpace.starSpaceHexes[hexIndex].entity, 'UR')

                print(hexIndex)

        combatGameBoard.drawHexes(gameScreen, operationSpace)
        pygame.display.update()

    pygame.quit()