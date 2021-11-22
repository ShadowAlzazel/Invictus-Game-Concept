import pygame 

# Char Order: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', ' Z', ',', '.', '!', '?', '@', '#', '&', '%']

class Font():

    def __init__(self, fontPath, scale=1):
        self.spacing = 1
        self.characterOrder = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', ' Z', ',', '.', '!', '?', '@', '#', '&', '%']
        fontImg = fontPath
        fontImg.convert()
        h = fontImg.get_height()
        self.fontCharacters = {}
        characterCount = 0
        currentCharacterWidth = 0 

        for x in range(fontImg.get_width()):
            i = fontImg.get_at((x, 0))
            if i[0] >= 250 and i[1] >= 250 and i[2] >= 250:
                chracterImg = self.clipImg(fontImg, x - currentCharacterWidth, 0, currentCharacterWidth, h) 
                #pygame.transform.scale(chracterImg, (chracterImg.get_width() * scale, h * scale))
                self.fontCharacters[self.characterOrder[characterCount]] = chracterImg.copy()
                #pygame.transform.scale(self.fontCharacters[self.characterOrder[characterCount]], (self.fontCharacters[self.characterOrder[characterCount]].get_width() * scale, h * scale))
                currentCharacterWidth = 0
                characterCount += 1
            else:
                currentCharacterWidth += 1
        self.spacingWidth = self.fontCharacters['A'].get_width()


    #clip img
    def clipImg(self, image, x, y, xSize, ySize):
        newImage = image.copy()
        rectClip = pygame.Rect(x, y, xSize, ySize)
        newImage.set_clip(rectClip)
        clipImage = image.subsurface(newImage.get_clip())
        return clipImage.copy()

    #draw font
    def renderFont(self, surf, text, location):
        xOffset = 0
        for x in text:
            if x != ' ':
                surf.blit(self.fontCharacters[x], (location[0] + xOffset, location[1]))
                xOffset += self.fontCharacters[x].get_width() + self.spacing
            else: 
                xOffset += self.spacingWidth + self.spacing