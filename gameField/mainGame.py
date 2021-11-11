import pygame
from pygame.constants import K_ESCAPE, KEYDOWN

LENGTH = 1000
WIDTH = 700

SCREEN_RGB = [38, 38, 51]
GAME_ICON = pygame.image.load('shipIconP2.png')

FPS = 60
#start game
def gameStart(): 
    pygame.init()

    gameScreen = pygame.display.set_mode((LENGTH, WIDTH))
    gameScreen.fill(SCREEN_RGB)
    pygame.display.update()
    pygame.display.set_caption("ASCS Fleet Manager")
    pygame.display.set_icon(GAME_ICON)
    
    #pygame.display.set_

    gameRunning = True
    gameClock = pygame.time.Clock()

    while gameRunning:
        gameClock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                gameRunning = False
