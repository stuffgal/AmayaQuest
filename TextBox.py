import os, sys
import pygame
from pygame.locals import *
pygame.init()

"""class TextBox(pygame.font.Font):
    def __init__(self, text):
        pygame.font.Font.__init__(self)
        self.text = text"""

class TextBox(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("TextBox.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 500)

class RenderedText(pygame.sprite.Sprite):
    def __init__(self, text):
        pygame.sprite.Sprite.__init__(self)
        self.text = text
        font = pygame.font.Font(None, 36)
        self.image = font.render(text, 1, (255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.topleft = (10, 510)

class TextBoxObject(pygame.sprite.OrderedUpdates):
    def __init__(self, text):            
        pygame.sprite.OrderedUpdates.__init__(self)
        
        textBox = TextBox()
        displayText = RenderedText(text)
        
        self.add(textBox)
        self.add(displayText)
        