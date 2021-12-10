#class for game display
from gameField.gameAssets import *

from multiprocessing.dummy import Pool as thread_pool
from functools import lru_cache

#----------------------------------------------------------------------

class map_screen:

    def __init__(self, ops_hex_map, game_screen, size_of_hexes):
        self.ops_hex_map = ops_hex_map
        self.game_screen = game_screen
        #measurements
        brd_X = ((LENGTH - (size_of_hexes * ops_hex_map.map_length)) // 2) 
        brd_Y = ((WIDTH - (size_of_hexes * ops_hex_map.map_width)) // 2) 
        self.measurements = {'hex_length': ops_hex_map.map_length, 'hex_width': ops_hex_map.map_width, 
                             'hex_pixel_size': size_of_hexes, 'moved_X': 0, 'moved_Y': 0, 'border_X': brd_X, 'border_Y': brd_Y}
        #selections
        self.selected_hex_index_coordinate = -1
        self.center_hex = -1
        self.selected_hex = []
        self.ship_selected = False 
        self.targets_hexes = []
        self.active_fleet_command = 'NNNN'
        #ship images
        self.ship_images = {'ASC_template': ASCS_SHIP_HEX_IMG, 'ASC_rotated': ASCS_SHIP_HEX_IMG, 
                            'XNF_template': XNFF_SHIP_HEX_IMG, 'XNF_rotated': XNFF_SHIP_HEX_IMG}
        for j in self.ship_images.values():
            j.convert_alpha()
        #animations
        self.base_hex_IMG = GRID_HEX_ANI_BASE
        self.base_hex_IMG.convert_alpha()
        self.template_hexes_IMG = {'template_hex_base': GRID_HEX_ANI_EMPTY, 'template_hex_enemy': GRID_HEX_ANI_ENEMY, 'template_hex_clicked': GRID_HEX_ANI_CLICK, 
                            'template_hex_move': GRID_HEX_ANI_MOVE, 'template_hex_target': GRID_HEX_ANI_TARGET, 'template_hex_ally': GRID_HEX_ANI_ALLY}
        for v in self.template_hexes_IMG.values():
            v.convert_alpha()
        self.animated_hexes_IMG = {'animated_hex_base': self.template_hexes_IMG['template_hex_base'], 'animated_hex_enemy': self.template_hexes_IMG['template_hex_enemy'], 
                            'animated_hex_clicked': self.template_hexes_IMG['template_hex_clicked'], 'animated_hex_move': self.template_hexes_IMG['template_hex_move'], 
                            'animated_hex_target': self.template_hexes_IMG['template_hex_target'], 'animated_hex_ally': self.template_hexes_IMG['template_hex_ally']}
        self.counter_animation_1 = 0
        self.counter_animation_2 = 0


    #draw hexes on board
    def draw_hexes(self, active_fleet_command, some_ship_hex=[]):
        self.selected_hex = some_ship_hex
        self.active_fleet_command = active_fleet_command
        self.game_screen.blit(FIT_SPACE, (0, 0))

        if self.center_hex > -1:
            c = 0
            if (self.center_hex // self.measurements['hex_length']) % 2 != 0:
                c = int(self.measurements['hex_pixel_size'] / 2)
            self.measurements['moved_X'] = int((self.measurements['hex_length'] / 2) - ((self.center_hex % self.measurements['hex_length']) + 1)) * self.measurements['hex_pixel_size'] + c
            self.measurements['moved_Y'] = int(((self.center_hex // self.measurements['hex_length'])) - (self.measurements['hex_width'] / 2) + 0.5) * self.measurements['hex_pixel_size']
            self.center_hex = -1
            
        #check of ship_selected
        self.ship_selected = False
        if some_ship_hex and not some_ship_hex.empty:
            self.targets_hexes = []
            some_ship = some_ship_hex.entity
            if some_ship.guns_primed():
                self.targets_hexes = some_ship.track_targets()
            self.ship_selected = True

        self._distrubute_draw_jobs(self.ops_hex_map.space_hexes, self.game_screen, self.measurements, self.animated_hexes_IMG, self.ship_selected, 
                                    self.selected_hex, self.active_fleet_command, self.targets_hexes, self.ship_images)
        return 



    #an environment for threading pool
    @staticmethod
    def _distrubute_draw_jobs(map_space_hexes, game_screen, screen_measurements, animated_hexes_IMG, 
                            ship_selected, selected_hex, active_fleet_command, targets_hexes, ship_IMG):

        #get x y coord
        @lru_cache(maxsize=2)
        def l_get_hex_x_y(some_hex):
            nonlocal screen_measurements
            row_height = screen_measurements['hex_width'] - (some_hex.hex_coordinate_index // screen_measurements['hex_length']) - 1
            indent = 0
            if row_height % 2 == screen_measurements['hex_width'] % 2:
                indent = screen_measurements['hex_pixel_size'] // 2

            y = (screen_measurements['border_Y']) + (row_height * screen_measurements['hex_pixel_size']) + screen_measurements['moved_Y']
            x = (screen_measurements['border_X']) + ((some_hex.hex_coordinate_index % screen_measurements['hex_length']) * screen_measurements['hex_pixel_size']) + indent - (screen_measurements['hex_pixel_size'] // 2) + screen_measurements['moved_X']
            return x, y


        #rotate an image
        @lru_cache(maxsize=2)
        def rotate_a_center(some_image, some_angle):
            original_rectangle = some_image.get_rect()
            rotated_image = pygame.transform.rotate(some_image, some_angle)
            rotated_rectangle = original_rectangle.copy()
            rotated_rectangle.center = rotated_image.get_rect().center
            rotated_image = rotated_image.subsurface(rotated_rectangle).copy()
            return rotated_image


        #draw a ship function
        #@lru_cache(maxsize=1)
        def draw_a_ship(some_ship, game_screen, ship_IMG, ship_size, position):
            h = ship_size
            ship_images = ship_IMG
            #some_ship_image = ship_images['ASC_template'].copy()
            ship_rotations = {'R': -90.0, 'L': -270.0, 'UR': -30.0, 'UL': -330.0, 'DR': -150.0, 'DL': -210.0}
            #WIP special ship images 
            if some_ship.command[0:3] == 'ASC' and some_ship.detected:
                some_ship_image = ship_images['ASC_template'].copy()
            elif some_ship.command[0:3] == 'XNF' and some_ship.detected:
                some_ship_image = ship_images['XNF_template'].copy()
            else:
                return

            some_ship_image.convert()
            rotated_ship_image = rotate_a_center(some_ship_image, ship_rotations[some_ship.orientation])
            scaled_ship_image = pygame.transform.scale(rotated_ship_image, (h, h))
            game_screen.blit(scaled_ship_image, position)


        #main blit call
        @lru_cache(maxsize=(LENGTH*3))
        def l_draw_some_hex(some_hex):
            nonlocal screen_measurements
            nonlocal game_screen
            nonlocal ship_selected
            nonlocal selected_hex
            nonlocal active_fleet_command
            nonlocal targets_hexes
            nonlocal ship_IMG
            x, y = l_get_hex_x_y(some_hex)
            if x < LENGTH + (screen_measurements['hex_pixel_size'] // 2) and y < WIDTH + (screen_measurements['hex_pixel_size'] // 2) and x > -(screen_measurements['hex_pixel_size']) and y > -(screen_measurements['hex_pixel_size']):
                game_screen.blit(animated_hexes_IMG['animated_hex_base'], (x, y))
                #check if empty for move
                if some_hex.empty:
                    if ship_selected:
                        some_ship = selected_hex.entity
                        if some_hex in selected_hex.neighbors and some_ship.ship_moves != 0 and (some_hex.directions[some_ship.orientation] != selected_hex.hex_coordinate_index or some_ship.ship_type == 'DD' or some_ship.ship_type == 'CS'):
                            if not (some_ship.ship_type == 'BB' and map_space_hexes[some_hex.directions[some_ship.orientation]] in selected_hex.neighbors):
                                game_screen.blit(animated_hexes_IMG['animated_hex_move'], (x, y))
                #check if ship
                elif some_hex.entity.entity_type == 'ship_entity':
                    #check if ally or enemy
                    if active_fleet_command[0:3] != some_hex.entity.command[0:3] and some_hex.entity.detected:
                        game_screen.blit(animated_hexes_IMG['animated_hex_enemy'], (x, y))
                    elif active_fleet_command[0:3] == some_hex.entity.command[0:3]:
                        game_screen.blit(animated_hexes_IMG['animated_hex_ally'], (x, y))

                    if some_hex.entity.detected:
                        draw_a_ship(some_hex.entity, game_screen, ship_IMG, screen_measurements['hex_pixel_size'], (x, y))

                    #check if target in range
                    if ship_selected:
                        if some_hex in targets_hexes:
                            game_screen.blit(animated_hexes_IMG['animated_hex_target'], (x, y))
                #clicked
                if ship_selected:
                    if some_hex.hex_coordinate_index == selected_hex.hex_coordinate_index:
                        game_screen.blit(animated_hexes_IMG['animated_hex_clicked'], (x, y))


        #make a multiprocess pool
        draw_pool = thread_pool(processes=2)
        draw_pool.map(l_draw_some_hex, map_space_hexes)
        draw_pool.close()
        draw_pool.join() 

        #with thread_pool(processes=4) as draw_pool:
        #    draw_pool.map(l_draw_some_hex, map_space_hexes)

        #for x in map_space_hexes:
        #    l_draw_some_hex(x)


    #get hexNums from coord mouse
    def get_mouse_hex(self, mouse_position):
        i = 0
        a, b = mouse_position
        a_position_active = False
        b_position_active = False 
        column, row = 0, 0

        if b in range(self.measurements['border_Y'] + self.measurements['moved_Y'], (self.measurements['hex_pixel_size'] * self.measurements['hex_width']) + (self.measurements['border_Y']) + self.measurements['moved_Y']):
            b_position_active = True
            #reverse y coords
            row = abs(((b - (self.measurements['border_Y'] + self.measurements['moved_Y'])) // self.measurements['hex_pixel_size']) - self.measurements['hex_width']) - 1
            #check even/odd rows
            if ((b - (self.measurements['border_Y'] + self.measurements['moved_Y'])) // self.measurements['hex_pixel_size']) % 2 == (self.measurements['hex_width'] + 1) % 2:
                i = self.measurements['hex_pixel_size'] // 2  

        if a in range((self.measurements['border_X']) - i + self.measurements['moved_X'], ((self.measurements['hex_pixel_size'] * self.measurements['hex_length']) + (self.measurements['border_X']) - i) + self.measurements['moved_X']):
            a_position_active = True
            column = ((a - (self.measurements['border_X'] + self.measurements['moved_X'])) + i) // self.measurements['hex_pixel_size']

        if a_position_active and b_position_active:
            mouse_hex_coordinate_index = (row * self.measurements['hex_length']) + column
            return mouse_hex_coordinate_index
        else:
            print("No Hexes In this space")
            return -1


    #WIP zoom in
    def zoom_in_window(self):
        self.measurements['hex_pixel_size'] += 8


    #WIP zoom out
    def zoom_out_window(self):
        self.measurements['hex_pixel_size'] -= 8


    #rotate an image with pivot center
    @staticmethod
    def _rotate_center(some_image, some_angle):
        original_rectangle = some_image.get_rect()
        rotated_image = pygame.transform.rotate(some_image, some_angle)
        rotated_rectangle = original_rectangle.copy()
        rotated_rectangle.center = rotated_image.get_rect().center
        rotated_image = rotated_image.subsurface(rotated_rectangle).copy()
        return rotated_image


    #animate instance images
    def animate_hexes(self):
        animation_order = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
        w = self.counter_animation_1 
        
        for temporary_hexes, animated_hex_keys in zip(self.template_hexes_IMG.values(), self.animated_hexes_IMG.keys()):
            base_hex_image = self.base_hex_IMG.copy()
            new_animated_hex = temporary_hexes.copy()
            base_hex_image.blit(new_animated_hex, (0, -animation_order[w]))
            new_animated_image = pygame.transform.scale(base_hex_image, (self.measurements['hex_pixel_size'], self.measurements['hex_pixel_size']))
            self.animated_hexes_IMG[animated_hex_keys] = new_animated_image
        
        if self.counter_animation_1 == 9:
            self.counter_animation_1 = 0
        else:
            self.counter_animation_1 += 1