import pygame 

# Char Order: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', ' Z', ',', '.', '!', '?', '@', '#', '&', '%']

class Font():

    def __init__(self, font_path, scale=1):
        self.spacing = 1
        self.character_order = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', ' Z', ',', '.', '!', '?', '@', '#', '&', '%']
        self.font_characters = {}
        font_img = font_path
        font_img.convert()
        h = font_img.get_height()
        character_count = 0
        current_character_width = 0 

        for x in range(font_img.get_width()):
            i = font_img.get_at((x, 0))
            if i[0] >= 250 and i[1] >= 250 and i[2] >= 250:
                character_image = self.clip_image(font_img, x - current_character_width, 0, current_character_width, h) 
                #pygame.transform.scale(character_image, (character_image.get_width() * scale, h * scale))
                self.font_characters[self.character_order[character_count]] = character_image.copy()
                #pygame.transform.scale(self.font_characters[self.character_order[character_count]], (self.font_characters[self.character_order[character_count]].get_width() * scale, h * scale))
                current_character_width = 0
                character_count += 1
            else:
                current_character_width += 1
        self.spacing_width = self.font_characters['A'].get_width()


    #clip img
    def clip_image(self, image, x, y, x_size, y_size):
        new_image = image.copy()
        rect_clip = pygame.Rect(x, y, x_size, y_size)
        new_image.set_clip(rect_clip)
        clipped_image = image.subsurface(new_image.get_clip())
        return clipped_image.copy()


    #draw font
    def render_font(self, surf, text, location):
        x_offset = 0
        for x in text:
            if x != ' ':
                surf.blit(self.font_characters[x], (location[0] + x_offset, location[1]))
                x_offset += self.font_characters[x].get_width() + self.spacing
            else: 
                x_offset += self.spacing_width + self.spacing