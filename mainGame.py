import pygame, sys, time
from pygame.constants import K_DOWN, K_ESCAPE, K_F4, K_LALT, K_LEFT, K_RIGHT, K_SPACE, K_UP, KEYDOWN, KEYUP, MOUSEBUTTONDOWN, QUIT, K_c, K_e, K_i, K_m, K_r, K_x, K_z
from gameField import *
from levelGames import *
from pygame.locals import *

#-----------------------------------------------------------------------
#main game function
def main():
    pygame.init()
    screen_flags = FULLSCREEN | DOUBLEBUF | SCALED

    #set up main game screen
    pygame.display.set_caption("INVICTUS: SAMAR")
    pygame.display.set_icon(GAME_ICON)
    game_screen = pygame.display.set_mode((LENGTH, WIDTH), screen_flags, 32)
    game_screen.blit(FIT_SPACE, (0, 0))
    pygame.display.update()

    global game_font_2A
    game_font_4A = Font(FONT_2A, 3)
    game_font_2A = Font(FONT_1A, 3)

    #variables
    main_running = True
    mouse_clicked = False

    #time
    game_clock = pygame.time.Clock()

    while main_running:
        game_clock.tick(FPS)
        game_screen.blit(FIT_SPACE, (0, 0))
        mx, my = pygame.mouse.get_pos()

        #menu buttons
        button_menu_start = pygame.Rect(16, 16, 48 * 4, 48)
        if button_menu_start.collidepoint((mx, my)) and mouse_clicked: 
            combatGameMenu(game_screen)

        pygame.draw.rect(game_screen, (2, 2, 2), button_menu_start)
        game_font_2A.render_font(game_screen, 'INVICTUS SAMAR', (16, 16))

        #event loop
        mouse_clicked = False
        for event in pygame.event.get():
            if event.type == QUIT:
                print("Quitting...")
                main_running = False 
                pygame.quit()
                sys.exit()

            if (event.type == KEYDOWN and event.key == K_ESCAPE) or (event.type == KEYDOWN and event.key == K_LALT and event.key == K_F4):
                print("Quitting...")
                main_running = False
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                mouse_clicked = True 

        pygame.display.update()
    #end game

#------------------------------------------------------------------------------------------
#menu for combat 
def combatGameMenu(game_screen):

    #variables 
    game_running = True
    mouse_clicked = False 

    #time 
    game_clock = pygame.time.Clock()

    while game_running:
        game_clock.tick(FPS)
        game_screen.blit(FIT_SPACE, (0, 0))
        mx, my = pygame.mouse.get_pos()

        button_game_selecter = pygame.Rect(16, 32, 48 * 4, 48)
        if button_game_selecter.collidepoint((mx, my)) and mouse_clicked:
            #WIP currently testing presets
            #have different buttons change level number and create levels
            level = "level_Test" 
            combatGame(game_screen, level)

        pygame.draw.rect(game_screen, (2, 2, 2), button_game_selecter)
        game_font_2A.render_font(game_screen, 'COMBAT GAME L', (16, 32))

        #event loop
        mouse_clicked = False
        for event in pygame.event.get():
            if event.type == QUIT:
                print("Quitting...")
                game_running = False 

            if event.type == KEYDOWN and event.key == K_ESCAPE:
                print("Quitting...")
                game_running = False 

            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                mouse_clicked = True 

        pygame.display.update() 


#-------------------------------------------------------------------------------------------
#combat game
def combatGame(game_screen, selcted_level):
    
    combat_level = None 
    #levels
    combat_level = level(selcted_level)
    if not combat_level:
        return

    #create new game window
    active_fleet_command = combat_level.areaGame.active_fleet.fleet_command
    combat_screen = spaceWindow(combat_level.level_hex_map, game_screen, HEX_SIZE)
    combat_level.areaGame.next_fleet_turn()
    combat_screen.draw_hexes(active_fleet_command)
    pygame.display.update()

    #animation calls
    animate_game_hexes = pygame.USEREVENT + 1
    pygame.time.set_timer(animate_game_hexes, 250)


    #variables 
    game_running = True 
    move_window_up, move_window_down, move_window_left, move_window_right = False, False, False, False
    framerate = FPS

    #time 
    game_clock = pygame.time.Clock()
    last_frame_time = time.perf_counter()
    last_second = time.perf_counter()
    a = 0

    windowMove = combat_screen.size_of_hexes // 16

    while game_running:
        game_clock.tick(framerate)
        #frame timing
        dt = time.perf_counter() - last_frame_time
        dt *= framerate 
        last_frame_time = time.perf_counter()

        #frame counting 
        a += 1
        if time.perf_counter() > last_second + 1:
            last_second = time.perf_counter()
            print("True FPS:", a) 
            a = 0
        
        #event loop
        for event in pygame.event.get():
            if event.type == QUIT:
                print("Quitting...")
                game_running = False 

            if event.type == KEYDOWN and event.key == K_ESCAPE:
                print("Quitting...")
                game_running = False 

            #window movement
            if event.type == KEYDOWN and event.key == K_UP:
                move_window_up = True
            if event.type == KEYUP and event.key == K_UP:
                move_window_up = False

            if event.type == KEYDOWN and event.key == K_DOWN:
                move_window_down = True
            if event.type == KEYUP and event.key == K_DOWN:
                move_window_down = False

            if event.type == KEYDOWN and event.key == K_LEFT:
                move_window_left = True
            if event.type == KEYUP and event.key == K_LEFT:
                move_window_left = False

            if event.type == KEYDOWN and event.key == K_RIGHT:
                move_window_right = True
            if event.type == KEYUP and event.key == K_RIGHT:
                move_window_right = False

            #reset window
            if event.type == KEYDOWN and event.key == K_c:
                combat_screen.move_window_X = 0
                combat_screen.move_window_Y = 0

            #end turn 
            if event.type == KEYDOWN and event.key == K_e:
                print('Fleet Turn Ended')
                combat_level.areaGame.next_fleet_turn()

            #inspect
            if event.type == KEYDOWN and event.key == K_i:
                if combat_level.areaGame.selected_hex:
                    combat_level.areaGame.selected_hex.entity.full_inspect()

            #zooming
            if event.type == KEYDOWN and event.key == K_z:
                combat_screen.zoom_in_window()
                windowMove = combat_screen.size_of_hexes // 16
                combat_screen.draw_hexes(combat_level.areaGame.active_fleet.fleet_command, combat_level.areaGame.selected_hex)

            if event.type == KEYDOWN and event.key == K_x:
                combat_screen.zoom_out_window()
                windowMove = combat_screen.size_of_hexes // 16
                combat_screen.draw_hexes(combat_level.areaGame.active_fleet.fleet_command, combat_level.areaGame.selected_hex)

            #center
            if event.type == KEYDOWN and event.key == K_SPACE:
                if combat_level.areaGame.selected_hex:
                    combat_screen.center_hex = combat_level.areaGame.selected_hex.hex_coordinate_index

            #check if animatedc
            if event.type == animate_game_hexes and not(move_window_right or move_window_left or move_window_up or move_window_down):
                combat_screen.animate_hexes()
                combat_screen.draw_hexes(combat_level.areaGame.active_fleet.fleet_command, combat_level.areaGame.selected_hex)

            if event.type == pygame.MOUSEBUTTONDOWN:
                someMousePos = pygame.mouse.get_pos()
                some_hex_coordinate_index = combat_screen.get_mouse_hex(someMousePos)
                combat_screen.selected_hex_index_coordinate = some_hex_coordinate_index
                if some_hex_coordinate_index >= 0:
                    combat_level.areaGame.select_hex(combat_level.level_hex_map.space_hexes[some_hex_coordinate_index])
                print(some_hex_coordinate_index)
                combat_screen.draw_hexes(combat_level.areaGame.active_fleet.fleet_command, combat_level.areaGame.selected_hex)


        #move window
        if move_window_up:
            combat_screen.move_window_Y -= windowMove
        if move_window_down:
            combat_screen.move_window_Y += windowMove
        if move_window_left:
            combat_screen.move_window_X -= windowMove
        if move_window_right:
            combat_screen.move_window_X += windowMove

        if move_window_right or move_window_left or move_window_up or move_window_down:
            combat_screen.draw_hexes(combat_level.areaGame.active_fleet.fleet_command, combat_level.areaGame.selected_hex)


        pygame.display.update()

#-------------------------------------------------------------------------------------------
#this is a runnable script
if __name__ == '__main__':
    main()