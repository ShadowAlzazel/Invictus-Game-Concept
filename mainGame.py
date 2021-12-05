import pygame, sys, time
from pygame.constants import K_DOWN, K_ESCAPE, K_F4, K_LALT, K_LEFT, K_RIGHT, K_SPACE, K_UP, KEYDOWN, KEYUP, MOUSEBUTTONDOWN, QUIT, K_c, K_e, K_i, K_m, K_r, K_x, K_z
from gameField import *
from levelGames import *

#-----------------------------------------------------------------------
#main game function
def main():
    pygame.init()

    #set up main game screen
    pygame.display.set_caption("INVICTUS: SAMAR")
    pygame.display.set_icon(GAME_ICON)
    gameScreen = pygame.display.set_mode((LENGTH, WIDTH))
    gameScreen.blit(FIT_SPACE, (0, 0))
    pygame.display.update()

    global gameFont2A
    gameFont1A = Font(FONT_1A, 3)
    gameFont2A = Font(FONT_2A, 3)

    #variables
    mainRunning = True
    mouseClick = False

    #time
    gameClock = pygame.time.Clock()

    while mainRunning:
        gameClock.tick(FPS)
        gameScreen.blit(FIT_SPACE, (0, 0))
        mx, my = pygame.mouse.get_pos()

        #menu buttons
        button1 = pygame.Rect(50, 100, 200, 50)
        if button1.collidepoint((mx, my)) and mouseClick: 
            combatGameMenu(gameScreen)

        pygame.draw.rect(gameScreen, (2, 2, 2), button1)
        gameFont2A.render_font(gameScreen, 'INVICTUS SAMAR', (50, 100))

        #event loop
        mouseClick = False
        for event in pygame.event.get():
            if event.type == QUIT:
                print("Quitting...")
                mainRunning = False 

            if ((event.type == KEYDOWN and event.key == K_ESCAPE) or (event.type == KEYDOWN and event.key == K_LALT and event.key == K_F4)):
                print("Quitting...")
                mainRunning = False

            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                mouseClick = True 

        pygame.display.update()
    #end game
    pygame.quit()
    sys.exit()


#------------------------------------------------------------------------------------------
#menu for combat 
def combatGameMenu(gameScreen):

    #variables 
    gameRunning = True
    mouseClick = False 

    #time 
    gameClock = pygame.time.Clock()

    while gameRunning:
        gameClock.tick(FPS)
        gameScreen.blit(FIT_SPACE, (0, 0))
        mx, my = pygame.mouse.get_pos()

        button2 = pygame.Rect(50, 200, 200, 50)
        if button2.collidepoint((mx, my)) and mouseClick:
            #WIP currently testing presets
            #have different buttons change level number and create levels
            level = "level_Test" 
            combatGame(gameScreen, level)

        pygame.draw.rect(gameScreen, (2, 2, 2), button2)
        gameFont2A.render_font(gameScreen, 'COMBATGAME', (50, 200))

        #event loop
        mouseClick = False
        for event in pygame.event.get():
            if event.type == QUIT:
                print("Quitting...")
                gameRunning = False 

            if (event.type == KEYDOWN and event.key == K_ESCAPE):
                print("Quitting...")
                gameRunning = False 

            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                mouseClick = True 

        pygame.display.update() 


#-------------------------------------------------------------------------------------------
#combat game
def combatGame(gameScreen, pLevel):
    
    gameLevel = None 
    #levels
    gameLevel = level(pLevel)
    if not gameLevel:
        return

    #create new game window
    currentFleetCom = gameLevel.areaGame.active_fleet.fleetCommand
    combatWindow = spaceWindow(gameLevel.engagementSpace, gameScreen, HEX_SIZE)
    gameLevel.areaGame.next_fleet_turn()
    combatWindow.drawHexes(currentFleetCom)
    pygame.display.update()

    #animation calls
    animateGridHexes = pygame.USEREVENT + 1
    pygame.time.set_timer(animateGridHexes, 300)


    #variables 
    gameRunning = True 
    moveUp, moveDown, moveLeft, moveRight = False, False, False, False
    framerate = FPS

    #time 
    gameClock = pygame.time.Clock()
    lastFrameTime = time.perf_counter()
    lastSec = time.perf_counter()
    a = 0

    while gameRunning:
        gameClock.tick(framerate)
        #frame timing
        dt = time.perf_counter() - lastFrameTime
        dt *= framerate 
        lastFrameTime = time.perf_counter()

        #frame counting 
        a += 1
        if time.perf_counter() > lastSec + 1:
            lastSec = time.perf_counter()
            print("True FPS:", a) 
            a = 0
        
        #move window
        windowMove = combatWindow.hexSize // 16 
        if moveUp:
            combatWindow.windowMoveY -= windowMove
        if moveDown:
            combatWindow.windowMoveY += windowMove
        if moveLeft:
            combatWindow.windowMoveX -= windowMove
        if moveRight:
            combatWindow.windowMoveX += windowMove

        #event loop
        for event in pygame.event.get():
            if event.type == QUIT:
                print("Quitting...")
                gameRunning = False 

            if (event.type == KEYDOWN and event.key == K_ESCAPE):
                print("Quitting...")
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
                combatWindow.windowMoveX = 0
                combatWindow.windowMoveY = 0

            #end turn 
            if event.type == KEYDOWN and event.key == K_e:
                print('Fleet Turn Ended')
                gameLevel.areaGame.next_fleet_turn()
                

            #inspect
            if event.type == KEYDOWN and event.key == K_i:
                if gameLevel.areaGame.selected_hex:
                    gameLevel.areaGame.selected_hex.entity.full_inspect()

            #zooming
            if event.type == KEYDOWN and event.key == K_z:
                combatWindow.zoomInHex()

            if event.type == KEYDOWN and event.key == K_x:
                combatWindow.zoomOutHex()

            #center
            if event.type == KEYDOWN and event.key == K_c:
                if gameLevel.areaGame.selected_hex:
                    combatWindow.centerHex = gameLevel.areaGame.selected_hex.hex_coordinate_index

            #check if animatedc
            if event.type == animateGridHexes:
                combatWindow.aniHexes()
                

            if event.type == pygame.MOUSEBUTTONDOWN:
                someMousePos = pygame.mouse.get_pos()
                hexIndex = combatWindow.getMouseHex(someMousePos)
                combatWindow.selected_hexNum = hexIndex
                if hexIndex >= 0:
                    gameLevel.areaGame.select_hex(gameLevel.engagementSpace.starHexes[hexIndex])
                print(hexIndex)

        combatWindow.drawHexes(gameLevel.areaGame.active_fleet.fleetCommand, gameLevel.areaGame.selected_hex)   
        pygame.display.update()


#-------------------------------------------------------------------------------------------
#this is a runnable script
if __name__ == '__main__':
    main()