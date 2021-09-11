# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 14:04:53 2020

@author: stavy
"""



import sys
import pygame
import sys, os


sys.path.append("C:/Users/stavy/Documents/Python/alien invasion")



from settings import Settings

from ship import Ship

def run_game():
    #initialize game and create a screen object.
    pygame.init()
    gamesettings = Settings()
    screen = pygame.display.set_mode((gamesettings.screen_width,gamesettings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    #make a ship
    
    ship = Ship(screen)
    
    
    #start main loop for game
    while True:
        
        #watch for keyboard and mouse events
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
                
        #redraw the screen during each pass through the loop
        screen.fill(gamesettings.bg_color)
        ship.blitme()
        # make the most recently drawn screen visible.
        pygame.display.flip()
    
    

run_game()