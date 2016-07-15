import os, sys
import pygame
from pygame.locals import *

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

class AQMain:
    
    def __init__(self, width=1920,height=1080):
        """Initialize"""
        """Initialize PyGame"""
        pygame.init()
        """Set the window Size"""
        self.width = width
        self.height = height
        """Create the Screen"""
        self.screen = pygame.display.set_mode((self.width,self.height), pygame.FULLSCREEN)
        """Draws the Killing Forest background"""
        bg = pygame.image.load("kf.png")
        self.screen.blit(bg, (0,0))
        pygame.display.flip()

    def MainLoop(self):
        """This is the Main Loop of the Game"""
        fullscreen = True
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                key = pygame.key.get_pressed()
                if key[K_f] == True:
                    if fullscreen == True:
                        pygame.display.set_mode((self.width,self.height))
                        fullscreen = False
                        bg = pygame.image.load("kf.png")
                        self.screen.blit(bg, (0,0))
                        pygame.display.flip()
                    else:
                        pygame.display.set_mode((self.width,self.height), pygame.FULLSCREEN)
                        fullscreen = True
                        bg = pygame.image.load("kf.png")
                        self.screen.blit(bg, (0,0))
                        pygame.display.flip()
                

if __name__ == "__main__":
    MainWindow = AQMain()
    MainWindow.MainLoop()
