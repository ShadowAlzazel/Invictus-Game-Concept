#class for game display
from gameField.gameAssets import *

from multiprocessing.dummy import Pool as thread_pool
from functools import lru_cache
from multiprocessing import Manager

#----------------------------------------------------------------------

class map_screen:

    def __init__(self, ops_hex_map, game_screen, size_of_hexes):
        self.hex_map_length = ops_hex_map.map_length
        self.hex_map_width = ops_hex_map.map_width
        self.ops_hex_map = ops_hex_map
        self.size_of_hexes = size_of_hexes
        self.game_screen = game_screen

        #movement variables
        self.move_window_X = 0
        self.move_window_Y = 0
        self.center_hex = -1
        self.window_border_Y = ((WIDTH - (self.size_of_hexes * self.hex_map_width)) // 2) - self.move_window_Y
        self.window_border_X = ((LENGTH - (self.size_of_hexes * self.hex_map_length)) // 2) + self.move_window_X

        #ship images
        self.ASCS_SHIP_HEX_IMG = ASCS_SHIP_HEX_IMG
        self.ROT_ASCS_SHIP_HEX_IMG = ASCS_SHIP_HEX_IMG
        self.XNFF_SHIP_HEX_IMG = XNFF_SHIP_HEX_IMG
        self.ROT_XNFF_SHIP_HEX_IMG = XNFF_SHIP_HEX_IMG

        #selections
        self.selected_hex_index_coordinate = -1
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
        self._scale_hexes(self.size_of_hexes)


    #draw hexes on board
    def draw_hexes(self, active_fleet_command, some_ship_hex=[]):
        self.selected_hex = some_ship_hex
        self.active_fleet_command = active_fleet_command
        self.game_screen.blit(FIT_SPACE, (0, 0))

        if self.center_hex > -1:
            c = 0
            if (self.center_hex // self.hex_map_length) % 2 != 0:
                c = int(self.size_of_hexes / 2)
            self.move_window_X = int((self.hex_map_length / 2) - ((self.center_hex % self.hex_map_length) + 1)) * self.size_of_hexes + c
            self.move_window_Y = int(((self.center_hex // self.hex_map_length)) - (self.hex_map_width / 2) + 0.5) * self.size_of_hexes
            self.center_hex = -1
            
        #check of ship_selected
        self.ship_selected = False
        if some_ship_hex and not some_ship_hex.empty:
            self.targets_hexes = []
            some_ship = some_ship_hex.entity
            if some_ship.guns_primed():
                self.targets_hexes = some_ship.track_targets()
            self.ship_selected = True

        with thread_pool(processes=2) as draw_pool:
            draw_pool.map(self._draw_a_hex, self.ops_hex_map.space_hexes)


    #draw an individual hex
    @lru_cache(maxsize=3)
    def _draw_a_hex(self, some_hex):
        row_height = self.hex_map_width - (some_hex.hex_coordinate_index // self.hex_map_length) - 1
        indent = 0
        if row_height % 2 == self.hex_map_width % 2:
            indent = self.size_of_hexes // 2

        y = (self.window_border_Y) + (row_height * self.size_of_hexes) + self.move_window_Y
        x = (self.window_border_X) + ((some_hex.hex_coordinate_index % self.hex_map_length) * self.size_of_hexes) + indent - (self.size_of_hexes // 2) + self.move_window_X
        #check if hex in render space
        if x < LENGTH + self.size_of_hexes and y < WIDTH + self.size_of_hexes and x > -self.size_of_hexes and y > -self.size_of_hexes:
            self.game_screen.blit(self.animated_hexes_IMG['animated_hex_base'], (x, y))
            #check if empty for move
            if some_hex.empty:
                if self.ship_selected:
                    some_ship = self.selected_hex.entity
                    if some_hex in self.selected_hex.neighbors and some_ship.ship_moves != 0 and (some_hex.directions[some_ship.orientation] != self.selected_hex.hex_coordinate_index or some_ship.ship_type == 'DD' or some_ship.ship_type == 'CS'):
                        if not (some_ship.ship_type == 'BB' and self.ops_hex_map.space_hexes[some_hex.directions[some_ship.orientation]] in self.selected_hex.neighbors):
                            self.game_screen.blit(self.animated_hexes_IMG['animated_hex_move'], (x, y))

            #check if ship
            elif some_hex.entity.entity_type == 'ship_entity':
                #check if ally or enemy
                if self.active_fleet_command[0:3] != some_hex.entity.command[0:3] and some_hex.entity.detected:
                    self.game_screen.blit(self.animated_hexes_IMG['animated_hex_enemy'], (x, y))
                elif self.active_fleet_command[0:3] == some_hex.entity.command[0:3]:
                    self.game_screen.blit(self.animated_hexes_IMG['animated_hex_ally'], (x, y))


                #WIP special ship images 
                if some_hex.entity.command[0:3] == 'ASC' and some_hex.entity.detected:
                    self.rotation_orientation(some_hex.entity)
                    self.game_screen.blit(self.ROT_ASCS_SHIP_HEX_IMG, (x, y))
                elif some_hex.entity.command[0:3] == 'XNF' and some_hex.entity.detected:
                    self.rotation_orientation(some_hex.entity)
                    self.game_screen.blit(self.ROT_XNFF_SHIP_HEX_IMG, (x, y))

                #check if target in range
                if self.ship_selected:
                    if some_hex in self.targets_hexes:
                        self.game_screen.blit(self.animated_hexes_IMG['animated_hex_target'], (x, y))
        
                #clicked
                if self.ship_selected:
                    if some_hex.hex_coordinate_index == self.selected_hex.hex_coordinate_index:
                        self.game_screen.blit(self.animated_hexes_IMG['animated_hex_clicked'], (x, y))


    #get hexNums from coord mouse
    def get_mouse_hex(self, mouse_position):
        i = 0
        a, b = mouse_position
        a_position_active = False
        b_position_active = False 
        column, row = 0, 0

        if b in range(self.window_border_Y + self.move_window_Y, (self.size_of_hexes * self.hex_map_width) + (self.window_border_Y) + self.move_window_Y):
            b_position_active = True
            #reverse y coords
            row = abs(((b - (self.window_border_Y + self.move_window_Y)) // self.size_of_hexes) - self.hex_map_width) - 1
            #check even/odd rows
            if ((b - (self.window_border_Y + self.move_window_Y)) // self.size_of_hexes) % 2 == (self.hex_map_width + 1) % 2:
                i = self.size_of_hexes // 2  

        if a in range((self.window_border_X) - i + self.move_window_X, ((self.size_of_hexes * self.hex_map_length) + (self.window_border_X) - i) + self.move_window_X):
            a_position_active = True
            column = ((a - (self.window_border_X + self.move_window_X)) + i) // self.size_of_hexes

        if a_position_active and b_position_active:
            mouse_hex_coordinate_index = (row * self.hex_map_length) + column
            return mouse_hex_coordinate_index
        else:
            print("No Hexes In this space")
            return -1

    #WIP zoom in
    def zoom_in_window(self):
        self.size_of_hexes += 8
        self._scale_hexes(self.size_of_hexes)

    #WIP zoom out
    def zoom_out_window(self):
        self.size_of_hexes -= 8
        self._scale_hexes(self.size_of_hexes)

    #rotate an image based on ship orientation
    def rotation_orientation(self, some_ship):
        orients = {'R': -90.0, 'L': -270.0, 'UR': -30.0, 'UL': -330.0, 'DR': -150.0, 'DL': -210.0}
        self._scale_hexes(self.size_of_hexes)
        if some_ship.command == 'ASCS':
            self.ROT_ASCS_SHIP_HEX_IMG = self._rotate_center(self.ASCS_SHIP_HEX_IMG, orients[some_ship.orientation]) 
        elif some_ship.command == 'XNFFS':
            self.ROT_XNFF_SHIP_HEX_IMG = self._rotate_center(self.XNFF_SHIP_HEX_IMG, orients[some_ship.orientation])

    #rotate an image with pivot center
    def _rotate_center(self, some_image, some_angle):
        original_rectangle = some_image.get_rect()
        rotated_image = pygame.transform.rotate(some_image, some_angle)
        rotated_rectangle = original_rectangle.copy()
        rotated_rectangle.center = rotated_image.get_rect().center
        rotated_image = rotated_image.subsurface(rotated_rectangle).copy()
        return rotated_image

    def animate_hexes(self):
        animation_order = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
        w = self.counter_animation_1 
        
        for temporary_hexes, animated_hex_keys in zip(self.template_hexes_IMG.values(), self.animated_hexes_IMG.keys()):
            base_hex_image = self.base_hex_IMG.copy()
            new_animated_hex = temporary_hexes.copy()
            base_hex_image.blit(new_animated_hex, (0, -animation_order[w]))
            new_animated_image = pygame.transform.scale(base_hex_image, (self.size_of_hexes, self.size_of_hexes))
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
