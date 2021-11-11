import pygame
from pygame.constants import K_ESCAPE, KEYDOWN
from gameField.gameBoard import *
from gameField.gameConstants import *

FPS = 60

gameScreen = pygame.display.set_mode((LENGTH, WIDTH))
gameScreen.fill(SCREEN_RGB)

#start game
def gameStart(aCombatSpace): 
    pygame.init()

    combatGameBoard = spaceGameBoard(aCombatSpace)

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
                pass

        combatGameBoard.drawHexes(gameScreen)
        pygame.display.update()

    pygame.quit()