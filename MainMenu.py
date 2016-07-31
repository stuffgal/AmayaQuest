import os, sys
import pygame
from pygame.locals import *
pygame.init()

if not pygame.font: print "Warning: fonts disabled."
if not pygame.mixer: print "Warning: sounds disabled."

class MenuItem(pygame.sprite.Sprite):
    def __init__(self, filenameUnselec, filenameSelec, topleftpos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("MenuImg\\" + filenameUnselec)
        self.rect = self.image.get_rect()
        self.rect.topleft = topleftpos
        self.filenameForUnselec = filenameUnselec
        self.filenameForSelec = filenameSelec
        self.isSelected = False
    
    def deselect(self):
        self.isSelected = False
        self.image = pygame.image.load("MenuImg\\" + self.filenameForUnselec)
    
    def select(self):
        self.isSelected = True
        self.image = pygame.image.load("MenuImg\\" + self.filenameForSelec)

class MenuBox(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("MenuImg\\MenuBg.png")
        self.rect = self.image.get_rect()
    
    def select(self):
        pass
    
    def deselect(self):
        pass

class MenuObject(pygame.sprite.OrderedUpdates):
    def __init__(self):    
        firstMenuBox = MenuBox()
        firstMenuItem = MenuItem("KFunselec.png", "KFselec.png", (0, 15))
        secondMenuItem = MenuItem("EscUnselec.png", "EscSelec.png", (0, 115))
        
        pygame.sprite.OrderedUpdates.__init__(self)
        self.add(firstMenuBox)
        self.add(firstMenuItem)
        self.add(secondMenuItem)
        self.selected = 0
    
    def decrementSelected(self):
        if self.selected == 0:
            self.selected = len(self.sprites()) - 1
        else:
            self.selected -= 1
    
    def incrementSelected(self):
        if self.selected == len(self.sprites()) - 1:
            self.selected = 0
        else:
            self.selected += 1
        
    def handleMenu(self):
        while 1:
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    sys.exit()
                    
                if event.type == KEYDOWN and event.key == K_ESCAPE:
                    sys.exit()
                    
                if event.type == KEYDOWN and event.key == K_w:
                    self.sprites()[self.selected].deselect()
                    self.decrementSelected()
                    self.sprites()[self.selected].select()
                    return "mainMenu"
                
                elif event.type == KEYDOWN and event.key == K_s:
                    self.sprites()[self.selected].deselect()
                    self.incrementSelected()
                    self.sprites()[self.selected].select()
                    return "mainMenu"