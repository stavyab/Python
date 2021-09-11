# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 14:00:37 2020

@author: stavy
"""

class Gamestats():
    def __init__(self, gamesettings):
        self.gamesettings = gamesettings
        self.reset_stats()
        self.game_active = False
        #high score should never reset
        self.high_score = 0
        
    def reset_stats(self):
        self.ships_left = self.gamesettings.ship_limit
        self.score = 0
        self.level = 1
        