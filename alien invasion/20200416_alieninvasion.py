# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 14:04:53 2020

@author: stavy
"""


import sys
import pygame
import sys, os 



sys.path.append("C:/Users/stavy/Documents/Python/alien invasion")


from pygame.sprite import Group
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
    
    #make a group to store bullets
    
    bullets = Group()
    
    
    #start main loop for game
    while True:
        gf.check_events(gamesettings, screen, ship, bullets)
        ship.update()
        
        print(len(bullets))
        gf.update_bullets
        gf.update_screen(gamesettings, screen, ship, bullets)     
                
        
        
run_game()