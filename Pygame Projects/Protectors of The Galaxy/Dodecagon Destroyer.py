import pygame
import random
from pygame.locals import *

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 400, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Protectors of the Galaxy")

font = pygame.font.Font("/Users/Bennet/Documents/Python/Pygame Projects/Protectors of The Galaxy/PublicPixel-z84yD.ttf", 13)
bigger_font = pygame.font.Font("/Users/Bennet/Documents/Python/Pygame Projects/Protectors of The Galaxy/PublicPixel-z84yD.ttf", 23)
biggest_font = pygame.font.Font("/Users/Bennet/Documents/Python/Pygame Projects/Protectors of The Galaxy/PublicPixel-z84yD.ttf", 60)
huge_font = pygame.font.Font("/Users/Bennet/Documents/Python/Pygame Projects/Protectors of The Galaxy/PublicPixel-z84yD.ttf", 95)
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
grey = (211,211,211)

enemy_speed = 2

score = 0
player_health = 100
game_over = False

player_dimension = 50
enemy_dimension = 25

enemy_spawns = [40, 80, 120, 160, 200, 240, 280, 320, 360]

player_bullets = []
enemies = []

max_bullets = 6
max_enemies = 5

bullet_sfx = pygame.mixer.Sound("/Users/Bennet/Documents/Python/Pygame Projects/Protectors of The Galaxy/mixkit-sci-fi-positive-notification-266.wav")
hit_sfx = pygame.mixer.Sound("/Users/Bennet/Documents/Python/Pygame Projects/Protectors of The Galaxy/mixkit-arcade-mechanical-bling-210.wav")


player_rect = pygame.Rect(180, 550, player_dimension, player_dimension)

player = pygame.image.load("/Users/Bennet/Documents/Python/Pygame Projects/Protectors of The Galaxy/spaceship_red.png")
player = pygame.transform.scale(player, (player_dimension, player_dimension))
player = pygame.transform.rotate(player, 180)

def draw_game(player_health, score, enemy_speed):
    screen.fill(white)
    if score < 100:
        level_display = biggest_font.render("I", True, grey)
        screen.blit(level_display, (170, 260))
        max_enemies = 6
        max_bullets = 7
    if score >= 100:
        cover_display = pygame.Rect(175, 260, 400, 400)
        pygame.draw.rect(screen, white, cover_display)
        level_display = biggest_font.render("II", True, grey)
        screen.blit(level_display, (135, 260))
        max_enemies = 7
        max_bullets = 8
    if score >= 300:
        cover_display = pygame.Rect(135, 260, 400, 400)
        pygame.draw.rect(screen, white, cover_display)
        level_display = biggest_font.render("III", True, grey)
        screen.blit(level_display, (120, 260))
        max_enemies = 8
        max_bullets = 9
    if score >= 400:
        cover_display = pygame.Rect(120, 260, 500, 450)
        pygame.draw.rect(screen, white, cover_display)
        level_display = biggest_font.render("IV", True, grey)
        screen.blit(level_display, (145, 260))
        enemy_speed = 2.5
    if score >= 500:
        cover_display = pygame.Rect(145, 260, 500, 500)
        pygame.draw.rect(screen, white, cover_display)
        level_display = huge_font.render("∞", True, grey)
        screen.blit(level_display, (170, 260))
        max_enemies = 10
        max_bullets = 8
    screen.blit(player, (player_rect.x, player_rect.y))

    health_text = font.render(str(player_health), True, black)
    screen.blit(health_text, (170, 17))
    score_text = font.render(str("Score:" + str(score)), True, black)
    screen.blit(score_text, (15, 40) )

    cover_bar = pygame.Rect(15, 15, 150, 20)
    pygame.draw.rect(screen, red, cover_bar)
    health_bar = pygame.Rect(15, 15, player_health * 1.5, 20)
    pygame.draw.rect(screen, green, health_bar)


    for bullet in player_bullets:
        pygame.draw.rect(screen, black, bullet)
        bullet.y -= 3
        if bullet.y - 3 < 0:
            player_bullets.remove(bullet)
        
    for enemy_rect in enemies:   
        enemy = pygame.image.load("/Users/Bennet/Documents/Python/Pygame Projects/Protectors of The Galaxy/spaceship_yellow.png")
        enemy = pygame.transform.scale(enemy, (enemy_dimension, enemy_dimension))
        enemy = pygame.transform.rotate(enemy, 180)

        screen.blit(enemy, (enemy_rect.x, enemy_rect.y))
        enemy_rect.y += enemy_speed

    if game_over == True:
        screen.fill(black)
        game_over_text = "Game Over!"
        game_over_text_display = bigger_font.render(game_over_text, True, red)
        final_score = "Score: " + str(score)
        final_score_display = font.render(final_score, True, white)
        screen.blit(final_score_display, (139, 270))
        screen.blit(game_over_text_display, (90, 240))
    

def player_movement(keys_pressed, player_rect):
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_LEFT] and player_rect.x - 3 > 0:
        player_rect.x -= 5
    if keys_pressed[pygame.K_RIGHT] and player_rect.x + player_dimension + 3 < 400:
        player_rect.x += 5

    


run = True
while run:
    clock = pygame.time.Clock()
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if game_over == False:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and len(player_bullets) < max_bullets:
                    bullet = pygame.Rect(player_rect.x + player_dimension // 2 - 3.5, player_rect.y - 15, 7, 15)
                    player_bullets.append(bullet)
                    bullet_sfx.play()
                
    keys_pressed = pygame.key.get_pressed
    if game_over == False:
        for x in range(max_enemies - len(enemies)):
            enemy_rect = pygame.Rect((random.choice(enemy_spawns)), 15, enemy_dimension, enemy_dimension)
            enemies.append(enemy_rect)
        for enemy_rect in enemies:   
            for bullet in player_bullets:
                if bullet.colliderect(enemy_rect):
                    hit_sfx.play()
                    player_bullets.remove(bullet)
                    enemies.remove(enemy_rect)
                    score += 10
        for enemy_rect in enemies:
            if enemy_rect.y > 600 or enemy_rect.colliderect(player_rect):
                enemies.remove(enemy_rect) 
                if player_health != 0:
                    player_health -= 20
                hit_sfx.play()
    
    draw_game(player_health, score, enemy_speed)
    player_movement(keys_pressed, player_rect)
    if player_health == 0:
        game_over = True
        
    pygame.display.update()

pygame.quit()