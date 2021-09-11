# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 19:59:05 2020

@author: stavy
"""

import pygame
import sys
from pygame.sprite import Sprite
sys.path.append("C:/Users/stavy/Documents/Python/alien invasion")


class Ship(Sprite):
    def __init__(self, gamesettings,screen):
        """Initialize the ship and set its starting position."""
        super(Ship, self).__init__()
        self.screen = screen
        self.gamesettings = gamesettings
        # Load the ship image and get its rect.
        
        self.image = pygame.image.load(r"C:\Users\stavy\Documents\Python\alien invasion\wanchu.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # Start each new ship at the bottom center of the screen.
        
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
       #store a decimal value for the ships center
        self.center = float(self.rect.centerx)
       #movement flag  
        self.moving_right = False
        self.moving_left = False

    def update(self):
        #update ships position
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.gamesettings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= self.gamesettings.ship_speed_factor
    
    def center_ship(self):
        self.center = self.screen_rect.centerx
    
    
    def blitme(self):
        self.screen.blit(self.image,self.rect)