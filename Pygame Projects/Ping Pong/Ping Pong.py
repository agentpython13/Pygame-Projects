import pygame
from pygame.locals import *

pygame.init()

hit_sfx = pygame.mixer.Sound("/Users/Bennet/Desktop/Python/Pygame Projects/Ping Pong/clack-85854.mp3")

SCREEN_WIDTH, SCREEN_HEIGHT = 600, 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ping Pong")

font = pygame.font.Font("/Users/Bennet/Desktop/Python/Pygame Projects/Ping Pong/PublicPixel-z84yD.ttf", 25)
smaller_font = pygame.font.Font("/Users/Bennet/Desktop/Python/Pygame Projects/Ping Pong/PublicPixel-z84yD.ttf", 15)

winner = 0
game_over = False

player_width, player_height = 12, 70

score1, score2 = 0, 0

player1 = pygame.Rect(10, 165, 2, player_height)
player2 = pygame.Rect(590, 265, 2, player_height)
ball = pygame.Rect(200, 200, 8, 8)
half_line = pygame.Rect(SCREEN_WIDTH//2 - 1, 0, 2, SCREEN_HEIGHT)
top_border = pygame.Rect(0,0, SCREEN_WIDTH, 10)
bottom_border = pygame.Rect(0,399, SCREEN_WIDTH, 10)

balls = [ball]

ball_right = True
ball_left = False
ball_up = True
ball_down = False

white = (255,255,255)
black = (0,0,0)

def draw_game(bottom_border, top_border, ball_left, ball_right, ball_up, ball_down, ball, score1, score2):
    screen.fill(black)
    pygame.draw.rect(screen, white, bottom_border)
    pygame.draw.rect(screen, white, top_border)
    pygame.draw.rect(screen, white, player1)
    pygame.draw.rect(screen, white, player2)
    pygame.draw.rect(screen, white, half_line)
    pygame.draw.rect(screen, white, ball)

    score1_text = str(score1)
    score1_display = font.render(score1_text, True, white)
    screen.blit(score1_display, (265, 15))
    score2_text = str(score2)
    score2_display = font.render(score2_text, True, white)
    screen.blit(score2_display, (315, 15))

def player_movement(player1, player2, keys_pressed):
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_a] and player1.y - 3 > 0:
        player1.y -= 7
    if keys_pressed[pygame.K_d] and player1.y + 3 + player_height < 400:
        player1.y += 7
    if keys_pressed[pygame.K_LEFT] and player2.y - 3 > 0:
        player2.y -= 7
    if keys_pressed[pygame.K_RIGHT] and player2.y + 3 + player_height < 400:
        player2.y += 7

run = True
while run:
    clock = pygame.time.Clock()
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys_pressed = pygame.key.get_pressed()
    if game_over == False:
        if ball.colliderect(top_border) or player1.colliderect(ball):
            if ball.colliderect(top_border):
                hit_sfx.play()
                ball_down = True
                ball_up = False
            else:
                hit_sfx.play()
                if player2.y - (player_height//2) < 100:
                    ball_up = True
                    ball_down = False
                if player2.y - (player_height//2) > 100 and player2.y - (player_height//2) < 175:
                    ball_up = False
                    ball_down = True
                if player2.y - (player_height//2) > 175 and player2.y - (player_height//2) < 275 or player2.y - (player_height//2) > 345 :
                    ball_up = False
                    ball_down = True
                if player2.y - (player_height//2) > 275 and player2.y - (player_height//2) < 345:
                    ball_up = True
                    ball_down = False
                if ball_right == True:
                    ball_left = True
                    ball_right = False
                if ball_left == True:
                    ball_right = True
                    ball_left = False
        if ball.colliderect(player2):
            hit_sfx.play()
            if player2.y - (player_height//2) < 100:
                ball_up = True
                ball_down = False
            if player2.y - (player_height//2) > 100 and player2.y - (player_height//2) < 175:
                ball_up = False
                ball_down = True
            if player2.y - (player_height//2) > 175 and player2.y - (player_height//2) < 275 or player2.y - (player_height//2) > 345 :
                ball_up = False
                ball_down = True
            if player2.y - (player_height//2) > 275 and player2.y - (player_height//2) < 345:
                ball_up = True
                ball_down = False
            if ball_right == False:
                ball_right = True
                ball_left = False
            if ball_left == False:
                ball_left = True
                ball_right = False
        if ball.colliderect(bottom_border):
            hit_sfx.play()
            ball_down = False
            ball_up = True

        if ball_left == True:
            ball.x -= 6
        if ball_right == True:
            ball.x += 6
        if ball_up == True:
            ball.y -= 6
        if ball_down == True:
            ball.y += 6
        
        if ball.x > 600:
            ball_down = False
            ball_right = False
            ball_up = True
            ball_left = True
            ball.x = 300
            ball.y = 200
            score1 += 1
        if ball.x < 0:
            ball_down = False
            ball_right = True
            ball_up = True
            ball_left = False
            ball.x = 300
            ball.y = 200
            score2 += 1

        
        if score1 == 9 or score1 > 9:
            game_over = True
            winner = player1
        if score2 == 9 or score2 > 9:
            game_over = True
            winner = player2


    
    player_movement(player1, player2, keys_pressed)
    draw_game(top_border, bottom_border, ball_left, ball_right, ball_up, ball_down, ball, score1, score2)
    
    if game_over == True:
        screen.fill(black)
        if winner == player1:
            score_cover = pygame.Rect(202,165,210,50)
            pygame.draw.rect(screen, white, score_cover)
            score_text = "Player 1 Wins!"
            score_display = smaller_font.render(score_text, True, black)
            screen.blit(score_display, (205,180))
        if winner == player2:
            score_cover = pygame.Rect(202,165,210,50)
            pygame.draw.rect(screen, white, score_cover)
            score_text = "Player 2 Wins!"
            score_display = smaller_font.render(score_text, True, black)
            screen.blit(score_display, (205,180))

    pygame.display.update()

pygame.quit()