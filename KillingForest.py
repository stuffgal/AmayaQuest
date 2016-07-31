import os, sys
import pygame
from pygame.locals import *
pygame.init()

if not pygame.font: print "Warning: fonts disabled."
if not pygame.mixer: print "Warning: sounds disabled."

from random import randint
import time

gametime = 600
day = 0
        
# This function allows you to modify the game time. Returns a string with the time in AM/PM format (eg. "12:15 AM")
def clock(assign=0, add=0, newday=False):   # First argument sets the time to a value, second argument adds a value to the time (must be divisible by 25), third argument can be used to designate a new day.
    global gametime, day
    display = ""   # The string that eventually becomes the function's output.
    
    # If the time is assigned, do so.
    if assign != 0:
        gametime = assign
        
    # If the time added is divisible by 25, do so.
    if add % 25 == 0:
        gametime += add
        
    # Increment the day if true.
    if newday == True:
        day += 1

    # If the time exceeds 24:00, reset to 00:00 and increment the day.
    if gametime >= 2400:
        gametime -= 2400
        day += 1
    
    # Figures out what the hour digits are and appends them to display. Also determines whether the current time is AM or PM.
    if gametime < 100:
        display = "12"
        pm = False
    elif gametime >= 100 and gametime < 1200:
        display = str(gametime/100)
        pm = False
    elif gametime >= 1200 and gametime < 1300:
        display = "12"
        pm = True
    elif gametime >= 1300:
        display = str((gametime-1200)/100)
        pm = True
        
    # Appends a colon to display.
    display = display + ":"
    
    # Figures out what the minutes digits are and appends them to display.
    if gametime - 100*(gametime/100) == 00:
        display = display + "00"
    elif gametime - 100*(gametime/100) == 25:
        display = display + "15"
    elif gametime - 100*(gametime/100) == 50:
        display = display + "30"
    elif gametime - 100*(gametime/100) == 75:
        display = display + "45"
        
    # Appends AM or PM to display.
    if pm == False:
        display = display + " AM"
    else:
        display = display + " PM"
        
    return display
    
def happening(location):
    resolution = (1920, 1080)
    screen = pygame.display.set_mode(resolution, pygame.FULLSCREEN)
    bg = pygame.image.load("kf.png")
    
    kfevents = 1
    
    if location == "kf":
        rnd = randint(0,0)
        while kfevents == 1:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    
            key = pygame.key.get_pressed()
            
            if key[K_ESCAPE] == True:
                sys.exit()
                    
            font = pygame.font.Font(None, 36)
            text1 = font.render("You happen upon a fast-flowing river. Your treasure senses are telling you that much better loot can be found on the other side!", 1, (255, 255, 255))
            text1pos = (20, 20)
            text2 = font.render("What would you like to do?", 1, (255, 255, 255))
            text2pos = (20, 40)
            text3 = font.render("1 - Cross the river.", 1, (255, 255, 255))
            text3pos = (20, 80)
            text4 = font.render("2 - Look around for something to help you cross.", 1, (255, 255, 255))
            text4pos = (20, 100)
            
            if key[K_1] == True:
                while 1:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            sys.exit()
                            
                    key = pygame.key.get_pressed()
                    
                    if key[K_ESCAPE] == True:
                        sys.exit()
                        
                    if key[K_RETURN] == True:
                        clock(0,50)
                        killing_forest()
                            
                    font = pygame.font.Font(None, 36)
                    text1 = font.render("You struggle, but manage to swim to the other side!", 1, (255, 255, 255))
                    text1pos = (20, 20)
                    text2 = font.render("(Pretend you're in the Deep Killing Forest now.) Press ENTER to continue.", 1, (255, 255, 255))
                    text2pos = (20, 40)
                    
                    screen.blit(bg, (0,0))
                    screen.blit(text1, text1pos)
                    screen.blit(text2, text2pos)
                    pygame.display.flip()
                    
            if key[K_2] == True:
                while 1:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            sys.exit()
                            
                    key = pygame.key.get_pressed()
                    
                    if key[K_ESCAPE] == True:
                        sys.exit()
                        
                    if key[K_RETURN] == True:
                        clock(0,100)
                        killing_forest()
                            
                    font = pygame.font.Font(None, 36)
                    text1 = font.render("You don't find anything, because programming events is too hard.", 1, (255, 255, 255))
                    text1pos = (20, 20)
                    text2 = font.render("Also you can't try again, because fuck you. Press ENTER to continue.", 1, (255, 255, 255))
                    text2pos = (20, 40)
                    
                    screen.blit(bg, (0,0))
                    screen.blit(text1, text1pos)
                    screen.blit(text2, text2pos)
                    pygame.display.flip()
            
            screen.blit(bg, (0,0))
            screen.blit(text1, text1pos)
            screen.blit(text2, text2pos)
            screen.blit(text3, text3pos)
            screen.blit(text4, text4pos)
            pygame.display.flip()

def killing_forest():
    resolution = (1920, 1080)
    screen = pygame.display.set_mode(resolution, pygame.FULLSCREEN)
    bg = pygame.image.load("kf.png")
    
    font = pygame.font.Font(None, 36)
    text1 = font.render("Welcome to the killing forest! It is now "+str(clock())+".", 1, (255, 255, 255))
    text1pos = (20, 20)
    text2 = font.render("Press 1 to go looking for trouble!", 1, (255, 255, 255))
    text2pos = (20, 120)
    
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
        key = pygame.key.get_pressed()
        
        if key[K_ESCAPE] == True:
            sys.exit()
        
        if key[K_1] == True:
            happening("kf")
    
        screen.blit(bg, (0,0))
        screen.blit(text1, text1pos)
        screen.blit(text2, text2pos)
        pygame.display.flip()
