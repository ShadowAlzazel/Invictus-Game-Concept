import pygame, sys 

# Char Order: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', ' Z', ' ,', '.', '!', '?', '@', '#', '&', '%']

def clipImg(image, x, y, xSize, ySize):
    newImage = image.copy()
    rectClip = pygame.Rect(x, y, xSize, ySize)
    newImage.setClip(rectClip)
    clipImage = image.subsurface(newImage.getClip())
    return clipImage.copy()

class Font():

    def __init__(self, imgFonts):
        self.spacing = 2
        self.characterOrder = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', ' Z', ' ,', '.', '!', '?', '@', '#', '&', '%']