# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 17:10:36 2020

@author: stavy
"""

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    #a class to represent a single alien in the fleet
    
    def __init__(self, gamesettings, screen):
        #initialize alien and set starting position
        super(Alien, self).__init__()
        self.screen = screen
        self.gamesettings = gamesettings
        
        #load the alien and get its it rect
        self.image = pygame.image.load(r"C:\Users\stavy\Documents\Python\alien invasion\HEM.bmp")
        self.rect = self.image.get_rect()
        
        #start each new alien at the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        #store aliens exact positionr"C:\Users\stavy\Documents\Python\alien invasion\wanchu.bmp"
        self.x = float(self.rect.x)
        
    def blitme(self):
        #draw the alien at its current location
        self.screen.blit(self.image, self.rect)
    
    def check_edges(self):
        #return True if alien is at edge of screen
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
    

    def update(self):
        #move the alien to the right or left
        self.x += (self.gamesettings.alien_speed_factor * self.gamesettings.fleet_direction)
        self.rect.x = self.x