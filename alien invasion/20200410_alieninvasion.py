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
import game_functions as gf
def run_game():
    #initialize game and create a screen object.
    pygame.init()
    gamesettings = Settings()
    screen = pygame.display.set_mode((gamesettings.screen_width,gamesettings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    #make a ship
    
    ship = Ship(gamesettings ,screen)
    
    
    #start main loop for game
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(gamesettings, screen, ship)     
    
                
        
        
run_game()