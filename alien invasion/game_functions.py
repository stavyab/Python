# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 13:55:02 2020

@author: stavy
"""

import sys
from time import sleep
import pygame
import sound as se
from bullet import Bullet
from alien import Alien

def check_events(gamesettings, screen, stats, sb, play_button, ship, aliens, bullets):
    #responds to keypresses and mouse events
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                check_keydown_events(event, gamesettings,screen ,ship, bullets)
            elif event.type == pygame.KEYUP:
                check_keyup_events(event, ship)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                check_play_button(gamesettings, screen, stats, sb, play_button, ship, aliens, 
                      bullets, mouse_x, mouse_y)
                
def check_play_button(gamesettings, screen, stats, sb, play_button, ship, aliens, 
                      bullets, mouse_x, mouse_y):
    """start a new game when the player clicks play"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        #wait 3 seconds
        #time.sleep(3)
        #play start sound
        se.ending_sound.play()
        #reset game setings
        gamesettings.initialize_dynamic_settings()
        #reset game statistics
        stats.reset_stats()
        stats.game_active = True
        #reset the scoreboard images
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()
        #hide the mouse cursor
        pygame.mouse.set_visible(False)
        
        #Empty the list of aliens and bullets
        aliens.empty()
        bullets.empty()
        
        #create a new fleet and center the ship
        create_fleet(gamesettings, screen, ship, aliens)
        ship.center_ship()
                        

def check_keydown_events(event ,gamesettings ,screen , ship ,bullets):
    #respond to keypresses
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        #create a new bullet and it to the bullet group
        fire_bullet(gamesettings, screen, ship, bullets)
    
        
def fire_bullet(gamesettings, screen, ship, bullets):
    #fire a bullet if limit is not reavhed       
    if len(bullets) < gamesettings.bullets_allowed:
        new_bullet = Bullet(gamesettings ,screen, ship)
        bullets.add(new_bullet)
        se.bullet_sound.play()
        
         
def update_bullets(gamesettings, screen, stats, sb, ship, aliens, bullets):
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(gamesettings, screen, stats, sb, ship, aliens, bullets)

def check_bullet_alien_collisions(gamesettings, screen, stats, sb, ship, aliens, bullets):
    #remove any aliens and bullets that have collided
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        stats.score += gamesettings.alien_points
        sb.prep_score()
        se.alien_sound.play()
    check_high_score(stats, sb)
    if len(aliens) == 0:
        bullets.empty
        gamesettings.increase_speed()
        
        stats.level += 1
        sb.prep_level()
        
        
        create_fleet(gamesettings, screen, ship, aliens)
        

def check_keyup_events(event, ship):
    #respond to keypresses
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False 
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def update_screen(gamesettings, screen, stats, sb, ship, aliens, bullets, play_button):
    screen.fill(gamesettings.bg_color)

    #redraw all bullets behind ship 
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    
    #draw the score information
    sb.show_score()

    #draw the play button if the game is inactive
    if not stats.game_active:
        play_button.draw_button()
    
    # make the most recently drawn screen visible.
    pygame.display.flip()   

    
    
def get_number_aliens_x(gamesettings, alien_width):
    available_space_x = gamesettings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(gamesettings, ship_height, alien_height):
    available_space_y = (gamesettings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows




def create_alien(gamesettings, screen, aliens, alien_number, row_number):
    alien = Alien(gamesettings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(gamesettings, screen, ship, aliens):
    alien = Alien(gamesettings, screen)
    number_aliens_x = get_number_aliens_x(gamesettings, alien.rect.width)
    number_rows = get_number_rows(gamesettings, ship.rect.height, alien.rect.height)
    
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(gamesettings, screen, aliens, alien_number, row_number)
    

def check_fleet_edges(gamesettings, aliens):
    #respond apropriately if any aliens have reached an edge
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(gamesettings, aliens)
            break
        
def change_fleet_direction(gamesettings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += gamesettings.fleet_drop_speed
    gamesettings.fleet_direction *= -1

def ship_hit(gamesettings, screen, stats, sb, ship, aliens, bullets):
    #decrement ships left
    if stats.ships_left > 0:
        stats.ships_left -= 1
        #update scoreboard
        sb.prep_ships()
        #empty the list of aliens and bullets
        aliens.empty()
        bullets.empty()
        #create a new fleet and center the ship
        create_fleet(gamesettings, screen, ship, aliens)
        ship.center_ship()
        #pause
        sleep(0.5)
        
    else:
        #play game end song
        se.starting_sound.play()
        stats.game_active = False
        pygame.mouse.set_visible(True)
    
def update_aliens(gamesettings, screen, stats, sb, ship, aliens, bullets):
    #Update the positions of all aliens in the fleet
    check_fleet_edges(gamesettings, aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(gamesettings, screen, stats, sb, ship, aliens, bullets)
    check_aliens_bottom(gamesettings, screen, stats, sb, ship, aliens, bullets)

def check_high_score(stats, sb):
    """check to seeif there is a new high score"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()

def check_aliens_bottom(gamesettings, screen, stats, sb, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            #treat this as the same as if the ship got hit
            ship_hit(gamesettings, screen, stats, sb, ship, aliens, bullets)
            break


