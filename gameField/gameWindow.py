#class for game display
from gameField.gameAssets import *

from multiprocessing.dummy import Pool as thread_pool
from functools import lru_cache
from multiprocessing import Manager, Process
from itertools import repeat

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

        #ship images
        self.ASCS_SHIP_HEX_IMG = ASCS_SHIP_HEX_IMG
        self.ROT_ASCS_SHIP_HEX_IMG = ASCS_SHIP_HEX_IMG
        self.XNFF_SHIP_HEX_IMG = XNFF_SHIP_HEX_IMG
        self.ROT_XNFF_SHIP_HEX_IMG = XNFF_SHIP_HEX_IMG

        #selections
        self.selected_hex_index_coordinate = -1
        self.center_hex = -1
        self.selected_hex = []
        self.ship_selected = False 
        self.targets_hexes = []
        self.active_fleet_command = 'NNNN'

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

        #scale
        self._scale_hexes(self.measurements['hex_pixel_size'])


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


        #rn calling multiple self classes need to change'


        self._distrubute_draw_jobs(self.ops_hex_map.space_hexes, self.game_screen, self.measurements, self.animated_hexes_IMG)
        #draw_pool = thread_pool(processes=2)
        ##draw_pool.map(self._draw_a_hex, self.ops_hex_map.space_hexes)
        #draw_pool.map(self._draw_some_hexes, self.ops_hex_map.space_hexes)
        #draw_pool.close()
        #draw_pool.join()

        #with thread_pool(processes=2) as draw_pool:
        #    draw_pool.map(self._draw_a_hex, self.ops_hex_map.space_hexes)
    
        
        #for x in self.ops_hex_map.space_hexes:
        #    self._draw_a_hex(x)



    @staticmethod
    def _distrubute_draw_jobs(map_space_hexes, game_screen, screen_measurements, animated_hexes_IMG):

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


        @lru_cache(maxsize=(LENGTH*2))
        def l_draw_some_hex(some_hex):
            nonlocal screen_measurements
            nonlocal game_screen
            x, y = l_get_hex_x_y(some_hex)
            if x < LENGTH + screen_measurements['hex_pixel_size'] and y < WIDTH + screen_measurements['hex_pixel_size'] and x > -screen_measurements['hex_pixel_size'] and y > -screen_measurements['hex_pixel_size']:
                game_screen.blit(animated_hexes_IMG['animated_hex_base'], (x, y))


        #draw_pool = thread_pool(processes=4)
        #draw_pool.map(l_draw_some_hex, map_space_hexes)
        #draw_pool.close()
        #draw_pool.join() 

        #with thread_pool(processes=4) as draw_pool:
        #    draw_pool.map(l_draw_some_hex, map_space_hexes)

        for x in map_space_hexes:
            l_draw_some_hex(x)


    #draw an individual hex
    @lru_cache(maxsize=1)
    def _draw_a_hex(self, some_hex):
        #check if hex in render space
        x, y = self._get_hex_x_y(some_hex, self.measurements['hex_length'], self.measurements['hex_width'], self.measurements['hex_pixel_size'], self.measurements['border_X'], self.measurements['border_Y'], self.measurements['moved_X'], self.measurements['moved_Y'])
        if x < LENGTH + self.measurements['hex_pixel_size'] and y < WIDTH + self.measurements['hex_pixel_size'] and x > -self.measurements['hex_pixel_size'] and y > -self.measurements['hex_pixel_size']:
            self._blit_a_hex(self.animated_hexes_IMG['animated_hex_base'], self.game_screen, (x, y))
            #check if empty for move
            if some_hex.empty:
                if self.ship_selected:
                    some_ship = self.selected_hex.entity
                    if some_hex in self.selected_hex.neighbors and some_ship.ship_moves != 0 and (some_hex.directions[some_ship.orientation] != self.selected_hex.hex_coordinate_index or some_ship.ship_type == 'DD' or some_ship.ship_type == 'CS'):
                        if not (some_ship.ship_type == 'BB' and self.ops_hex_map.space_hexes[some_hex.directions[some_ship.orientation]] in self.selected_hex.neighbors):
                            self._blit_a_hex(self.animated_hexes_IMG['animated_hex_move'], self.game_screen, (x, y))

            #check if ship
            elif some_hex.entity.entity_type == 'ship_entity':
                #check if ally or enemy
                if self.active_fleet_command[0:3] != some_hex.entity.command[0:3] and some_hex.entity.detected:
                    self._blit_a_hex(self.animated_hexes_IMG['animated_hex_enemy'], self.game_screen, (x, y))
                elif self.active_fleet_command[0:3] == some_hex.entity.command[0:3]:
                    self._blit_a_hex(self.animated_hexes_IMG['animated_hex_ally'], self.game_screen, (x, y))


                #WIP special ship images 
                if some_hex.entity.command[0:3] == 'ASC' and some_hex.entity.detected:
                    self.rotation_orientation(some_hex.entity)
                    self._blit_a_hex(self.ROT_ASCS_SHIP_HEX_IMG, self.game_screen, (x, y))
                elif some_hex.entity.command[0:3] == 'XNF' and some_hex.entity.detected:
                    self.rotation_orientation(some_hex.entity)
                    self._blit_a_hex(self.ROT_XNFF_SHIP_HEX_IMG, self.game_screen, (x, y))

                #check if target in range
                if self.ship_selected:
                    if some_hex in self.targets_hexes:
                        self._blit_a_hex(self.animated_hexes_IMG['animated_hex_target'], self.game_screen, (x, y))
        
                #clicked
                if self.ship_selected:
                    if some_hex.hex_coordinate_index == self.selected_hex.hex_coordinate_index:
                        self._blit_a_hex(self.animated_hexes_IMG['animated_hex_clicked'], self.game_screen, (x, y))


    #get x, y and cache it
    @staticmethod
    @lru_cache(maxsize=(LENGTH+1))
    def _get_hex_x_y(some_hex, screen_measurements):
        row_height = screen_measurements['hex_width'] - (some_hex.hex_coordinate_index // screen_measurements['hex_length']) - 1
        indent = 0
        if row_height % 2 == screen_measurements['hex_width'] % 2:
            indent = screen_measurements['hex_pixel_size'] // 2

        y = (screen_measurements['border_Y']) + (row_height * screen_measurements['hex_pixel_size']) + screen_measurements['moved_Y']
        x = (screen_measurements['border_X']) + ((some_hex.hex_coordinate_index % screen_measurements['hex_length']) * screen_measurements['hex_pixel_size']) + indent - (screen_measurements['hex_pixel_size'] // 2) + screen_measurements['moved_X']
        return x, y


    #blit the hex on screen and cache it
    @staticmethod
    @lru_cache(maxsize=2)
    def _blit_a_hex(some_image, game_screen, hex_position):
        game_screen.blit(some_image, hex_position)


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
        self._scale_hexes(self.measurements['hex_pixel_size'])

    #WIP zoom out
    def zoom_out_window(self):
        self.measurements['hex_pixel_size'] -= 8
        self._scale_hexes(self.measurements['hex_pixel_size'])

    #rotate an image based on ship orientation
    def rotation_orientation(self, some_ship):
        orients = {'R': -90.0, 'L': -270.0, 'UR': -30.0, 'UL': -330.0, 'DR': -150.0, 'DL': -210.0}
        self._scale_hexes(self.measurements['hex_pixel_size'])
        if some_ship.command == 'ASCS':
            self.ROT_ASCS_SHIP_HEX_IMG = self._rotate_center(self.ASCS_SHIP_HEX_IMG, orients[some_ship.orientation]) 
        elif some_ship.command == 'XNFFS':
            self.ROT_XNFF_SHIP_HEX_IMG = self._rotate_center(self.XNFF_SHIP_HEX_IMG, orients[some_ship.orientation])

    #rotate an image with pivot center
    #WIP change to class method
    def _rotate_center(self, some_image, some_angle):
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
       
    #scale the hexes
    def _scale_hexes(self, size_of_hexes):
        self.ASCS_SHIP_HEX_IMG.convert()
        self.XNFF_SHIP_HEX_IMG.convert()
        self.ASCS_SHIP_HEX_IMG = pygame.transform.smoothscale(ASCS_SHIP_HEX_IMG, (size_of_hexes, size_of_hexes))
        self.XNFF_SHIP_HEX_IMG = pygame.transform.smoothscale(XNFF_SHIP_HEX_IMG, (size_of_hexes, size_of_hexes))
