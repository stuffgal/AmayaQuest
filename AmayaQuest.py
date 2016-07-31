import os, sys
import pygame
from pygame.locals import *
pygame.init()

if not pygame.font: print "Warning: fonts disabled."
if not pygame.mixer: print "Warning: sounds disabled."

from KillingForest import killing_forest
from MainMenu import MenuObject
from TextBox import TextBoxObject

resolution = (1920, 1080)
screen = pygame.display.set_mode(resolution) 

bg = pygame.image.load("start.png")

font = pygame.font.Font(None, 36)
words = font.render("Welcome to Amaya Quest! :) Press K to go to the Killing Forest", 1, (255, 255, 255), (0, 0, 0))
wordspos = (20, 20)

menuBox = MenuObject()
textBox = TextBoxObject("tweet")

active = "mainMenu"

menus = {"mainMenu" : menuBox, "kitty" : "kitty"}

screen.blit(bg, (0,0))
screen.blit(words, wordspos)
menuBox.draw(screen)
textBox.draw(screen)
pygame.display.flip()

while 1:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            sys.exit()
            
    key = pygame.key.get_pressed()
    
    active = menus[active].handleMenu()
    
    if key[K_ESCAPE] == True:
        sys.exit()
        
    if key[K_k] == True:
        killing_forest()
    
    screen.blit(bg, (0,0))
    screen.blit(words, wordspos)
    menuBox.draw(screen)
    textBox.draw(screen)
    pygame.display.flip()