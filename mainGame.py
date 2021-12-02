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
        gameFont2A.renderFont(gameScreen, 'INVICTUS SAMAR', (50, 100))

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
            level = 64 
            combatGame(gameScreen, level)

        pygame.draw.rect(gameScreen, (2, 2, 2), button2)
        gameFont2A.renderFont(gameScreen, 'COMBATGAME', (50, 200))

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
    if pLevel == 43:
        fleet1 = spaceFleet(astraFleets[0]['ASC']['fleetNames'][0], 'ASC')
        fleet2 = spaceFleet(astraFleets[0]['XNFF']['fleetNames'][0], 'XNFF')
        gameLevel = level(14, 10, 0 ,(fleet1, fleet2), [70, 104])
    elif pLevel == 64:
        fleet1 = spaceFleet(astraFleets[0]['ASC']['fleetNames'][1], 'ASC')
        fleet2 = spaceFleet(astraFleets[0]['XNFF']['fleetNames'][0], 'XNFF')
        gameLevel = level(15, 12, 0 ,(fleet1, fleet2), [35, 76])
    elif pLevel == 77:
        fleet1 = spaceFleet(astraFleets[0]['ASC']['fleetNames'][2], 'ASC')
        fleet2 = spaceFleet(astraFleets[0]['XNFF']['fleetNames'][0], 'XNFF')
        gameLevel = level(10, 10, 0 ,(fleet1, fleet2), [25, 85])

    if not gameLevel:
        return

    #create new game window
    currentFleetCom = gameLevel.areaGame.activeFleet.fleetCommand
    combatWindow = spaceWindow(gameLevel.areaOfEngagement.l, gameLevel.areaOfEngagement.w, HEX_SIZE)
    gameLevel.areaGame.fleetTurn()
    combatWindow.drawHexes(gameScreen, gameLevel.areaOfEngagement, currentFleetCom)
    pygame.display.update()

    #animation calls
    animateGridHexes = pygame.USEREVENT + 1
    pygame.time.set_timer(animateGridHexes, 200)


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

        gameClock.tick(framerate)

        currentFleetCom = gameLevel.areaGame.activeFleet.fleetCommand
        
        #move window
        windowMove = combatWindow.hexSize / 8
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
                gameLevel.areaGame.fleetTurn()
                combatWindow.drawHexes(gameScreen, gameLevel.areaOfEngagement, currentFleetCom)

            #inspect
            if event.type == KEYDOWN and event.key == K_i:
                if gameLevel.areaGame.selectedHex:
                    gameLevel.areaGame.selectedHex.entity.fullInspect()

            #zooming
            if event.type == KEYDOWN and event.key == K_z:
                combatWindow.zoomInHex()

            if event.type == KEYDOWN and event.key == K_x:
                combatWindow.zoomOutHex()

            #center
            if event.type == KEYDOWN and event.key == K_c:
                if gameLevel.areaGame.selectedHex:
                    combatWindow.centerHex = gameLevel.areaGame.selectedHex.hexCoord

            #check if animatedc
            if event.type == animateGridHexes:
                combatWindow.aniHexes()
                combatWindow.drawHexes(gameScreen, gameLevel.areaOfEngagement, currentFleetCom, gameLevel.areaGame.selectedHex)

            if event.type == pygame.MOUSEBUTTONDOWN:
                someMousePos = pygame.mouse.get_pos()
                hexIndex = combatWindow.getMouseHex(someMousePos)
                if hexIndex >= 0:
                    gameLevel.areaGame.selectHex(gameLevel.areaOfEngagement.starHexes[hexIndex])
                print(hexIndex)

        #combatWindow.drawHexes(gameScreen, gameLevel.areaOfEngagement, currentFleetCom, gameLevel.areaGame.selectedHex)   
        pygame.display.update()


#-------------------------------------------------------------------------------------------
#this is a runnable script
if __name__ == '__main__':
    main()