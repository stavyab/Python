# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 17:24:57 2020

@author: stavy
"""

class Settings():
    #a class to store settings
    
    def __init__(self):
        #initialize the game's static settings
        #screen settings
        self.screen_width = 750
        self.screen_height = 400
        self.bg_color = (230,230,230)
        #ship settings
        self.ship_speed_factor = 10
        self.ship_limit = 3
        #aliensettings
        self.alien_speed_factor = 2.5
        self.fleet_drop_speed =5
        self.fleet_direction = 1
        #bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed =  3
        
        #how quickly the game speeds up
        self.speedup_scale = 1.25
        #how quickly the alien point value increases
        self.score_scale = 1.5
        self.initialize_dynamic_settings()
        
    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        
    def initialize_dynamic_settings(self):
        """initialize settings that change through the game"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.fleet_direction = 1
        #scoring
        self.alien_points = 50
   