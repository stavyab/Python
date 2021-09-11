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
from game_stats import Gamestats
from button import Button
from ship import Ship
from alien import Alien
import game_functions as gf
def run_game():
    #initialize game and create a screen object.
    pygame.init()
    gamesettings = Settings()
    screen = pygame.display.set_mode((gamesettings.screen_width,gamesettings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    #make the play button
    play_button = Button(gamesettings, screen, "Play")
    
  
    #make a ship
    ship = Ship(gamesettings ,screen)
    #make a group to store bullets
    bullets = Group()
    aliens = Group()
    #make an alien
    alien = Alien(gamesettings, screen)
    #create the fleet of aliens
    gf.create_fleet(gamesettings, screen, ship, aliens)
    #create an instance to store game statistics
    stats = Gamestats(gamesettings)
    
    #start main loop for game
    while True:
        gf.check_events(gamesettings, screen, stats, play_button, ship, aliens, bullets)
        
        if stats.game_active:
            ship.update()
            bullets.update()
            gf.update_aliens(gamesettings, stats, screen, ship, aliens, bullets)
            gf.update_bullets(gamesettings, screen, ship, aliens, bullets)
        
        
        #get rid of excess bullets
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        print(len(bullets))
        gf.update_screen(gamesettings, screen, stats, ship, aliens, bullets, play_button)     
                
        
        
run_game()