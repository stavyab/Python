# -*- coding: utf-8 -*-
"""
Created on Tue May 26 12:34:25 2020

@author: stavy
"""

import pygame


pygame.mixer.init()

bullet_sound = pygame.mixer.Sound(r"C:/Users/stavy/Documents/Python/alien invasion/laser.wav")
alien_sound = pygame.mixer.Sound(r"C:/Users/stavy/Documents/Python/alien invasion/boom.wav")
ending_sound = pygame.mixer.Sound(r"C:\Users\stavy\Documents\Python\alien invasion/gamestarting.wav")
starting_sound = pygame.mixer.Sound(r"C:\Users\stavy\Documents\Python\alien invasion/gameend.wav")