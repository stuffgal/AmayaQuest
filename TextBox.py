import os, sys
import pygame
from pygame.locals import *
pygame.init()

class TextBox(pygame.font.Font):
    def __init__(self, text):
        pygame.font.Font.__init__(self)
        self.text = text
        