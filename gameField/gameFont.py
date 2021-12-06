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
        characterCount = 0
        currentCharacterWidth = 0 

        for x in range(font_img.get_width()):
            i = font_img.get_at((x, 0))
            if i[0] >= 250 and i[1] >= 250 and i[2] >= 250:
                chracterImg = self.clip_image(font_img, x - currentCharacterWidth, 0, currentCharacterWidth, h) 
                #pygame.transform.scale(chracterImg, (chracterImg.get_width() * scale, h * scale))
                self.font_characters[self.character_order[characterCount]] = chracterImg.copy()
                #pygame.transform.scale(self.font_characters[self.character_order[characterCount]], (self.font_characters[self.character_order[characterCount]].get_width() * scale, h * scale))
                currentCharacterWidth = 0
                characterCount += 1
            else:
                currentCharacterWidth += 1
        self.spacing_width = self.font_characters['A'].get_width()


    #clip img
    def clip_image(self, image, x, y, xSize, ySize):
        newImage = image.copy()
        rect_clip = pygame.Rect(x, y, xSize, ySize)
        newImage.set_clip(rect_clip)
        clipped_image = image.subsurface(newImage.get_clip())
        return clipped_image.copy()


    #draw font
    def render_font(self, surf, text, location):
        xOffset = 0
        for x in text:
            if x != ' ':
                surf.blit(self.font_characters[x], (location[0] + xOffset, location[1]))
                xOffset += self.font_characters[x].get_width() + self.spacing
            else: 
                xOffset += self.spacing_width + self.spacing