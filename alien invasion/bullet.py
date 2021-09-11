# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 13:50:46 2020

@author: stavy
"""

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    
    def __init__(self,gamesettings, screen, ship):
        super(Bullet, self).__init__()
        self.screen = screen
        
        #create a bullet rect at (0,0) and then set correct position
        self.rect = pygame.Rect(0, 0, gamesettings.bullet_width, gamesettings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        
        #store the bullets position as a decimal value
        self.y = float(self.rect.y)
        
        self.color = gamesettings.bullet_color
        self.speed_factor = gamesettings.bullet_speed_factor
        
    def update(self):
        #update the decimal position of the bullet
        self.y -= self.speed_factor
        #update the rect porition
        self.rect.y = self.y
        
    def draw_bullet(self):
        #draw the bullet to the screen
        pygame.draw.rect(self.screen, self.color, self.rect)