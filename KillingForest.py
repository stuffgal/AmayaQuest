import os, sys
import pygame
from pygame.locals import *
pygame.init()

if not pygame.font: print "Warning: fonts disabled."
if not pygame.mixer: print "Warning: sounds disabled."

def killing_forest():
    resolution = (1920, 1080)
    screen = pygame.display.set_mode(resolution, pygame.FULLSCREEN)
    fullscreen = True
    bg = pygame.image.load("kf.png")
    
    font = pygame.font.Font(None, 36)
    words = font.render("Welcome to Amaya Quest! You are now at the Killing Forest.", 1, (255, 255, 255))
    wordspos = (20, 20)
    
    while 1:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                sys.exit()
                
        key = pygame.key.get_pressed()
        
        if key[K_f] == True:
            if fullscreen == True:
                pygame.display.set_mode(resolution)
                fullscreen = False
            else:
                pygame.display.set_mode(resolution, pygame.FULLSCREEN)
                fullscreen = True
        
        if key[K_ESCAPE] == True:
            sys.exit()
        
        screen.blit(bg, (0,0))
        screen.blit(words, wordspos)
        pygame.display.flip()