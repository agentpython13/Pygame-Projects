import pygame

pygame.init()

#creating game window and adding window caption
screen_width, screen_height = 900, 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Invaders")

#defining color variables 
red = (255,0,0)
white = (255,255,255)
black = (0,0,0)
green = (0,255,0)
yellow = (255,255,0)

#defining spaceship width and height
spaceship_dimensions = 45

#spaceship borders
border = pygame.Rect(screen_width // 2 - 5, 0, 10, screen_height)

#bullet lists
r_bullets = []
y_bullets = []

r_health = 100
y_health = 100

winner = 0

game_over = False

font = pygame.font.SysFont(None, 35)

bullet_sfx = pygame.mixer.Sound("/Users/Bennet/Desktop/Python/Pygame Projects/Space Invaders/mixkit-arcade-mechanical-bling-210.wav")
hit_sfx = pygame.mixer.Sound("/Users/Bennet/Desktop/Python/Pygame Projects/Space Invaders/mixkit-electronic-retro-block-hit-2185.wav")


y_text = ("Yellow Player Wins!")
y_display = font.render(y_text, True, black)
r_text = ("Red Player Wins!")
r_display = font.render(r_text, True, black)

#drawing spaceships, changing size and rotating"
yellow_spaceship = pygame.image.load("/Users/Bennet/Desktop/Python/Pygame Projects/Space Invaders/spaceship_yellow.png")
yellow_spaceship = pygame.transform.scale(yellow_spaceship, (spaceship_dimensions, spaceship_dimensions))
yellow_spaceship = pygame.transform.rotate(yellow_spaceship, 270)


red_spaceship = pygame.image.load("/Users/Bennet/Desktop/Python/Pygame Projects/Space Invaders/spaceship_red.png")
red_spaceship = pygame.transform.scale(red_spaceship, (spaceship_dimensions, spaceship_dimensions))
red_spaceship = pygame.transform.rotate(red_spaceship, 90)

#function coloring window, updating display and drawing spaceships
def draw_game(r_player, y_player):
  screen.fill(white)

  screen.blit(red_spaceship, (r_player.x, r_player.y))
  screen.blit(yellow_spaceship, (y_player.x, y_player.y))

  pygame.draw.rect(screen, black, border)
  for x in r_bullets:
    pygame.draw.rect(screen, black, x)
  for x in y_bullets:
    pygame.draw.rect(screen, black, x)
    
  for x in r_bullets:
    x.x += 6
    if x.x + 6 > 900:
      r_bullets.remove(x)
  for x in y_bullets:
    x.x -= 6
    if x.x + 6 < 0:
      y_bullets.remove(x)
      
  r_health_bar_ = pygame.Rect(50, 300, 150, 20)
  pygame.draw.rect(screen, red, r_health_bar_ )
  y_health_bar_ = pygame.Rect(661, 300, 150, 20)
  pygame.draw.rect(screen, red, y_health_bar_ )
  r_health_bar = pygame.Rect(50,300, r_health* 1.5, 20)
  pygame.draw.rect(screen, green, r_health_bar)
  y_health_bar = pygame.Rect(661,300, y_health * 1.5, 20)
  pygame.draw.rect(screen, green, y_health_bar)

  r_health_text = str(r_health)
  display = font.render(r_health_text, True, black)
  screen.blit(display, (210, 298))
  
  y_health_text = str(y_health)
  display = font.render(y_health_text, True, black)
  screen.blit(display, (820, 298))

  if game_over == True and winner == r_player:
    screen.fill(black)
    r_win_text = str("Player Red Wins!")
    display = font.render(r_win_text, True, black)
    border_cover = pygame.Rect(screen_width // 2 - 5, 0, 10, screen_height)
    pygame.draw.rect(screen, black, border_cover)
    display_cover = pygame.Rect(337, 165, 220, 35)
    pygame.draw.rect(screen, red, display_cover)
    screen.blit(display, (345, 170))
  if game_over == True and winner == y_player:
    screen.fill(black)
    y_win_text = str("Player Yellow Wins!")
    display = font.render(y_win_text, True, black)
    border_cover = pygame.Rect(screen_width // 2 - 5, 0, 10, screen_height)
    pygame.draw.rect(screen, black, border_cover)
    display_cover = pygame.Rect(327, 165, 243, 35)
    pygame.draw.rect(screen, yellow, display_cover)
    screen.blit(display, (335, 170))


  pygame.display.update()

#spaceship locations via rectangles
r_player = pygame.Rect(100, 150, spaceship_dimensions, spaceship_dimensions)
y_player = pygame.Rect(700, 150, spaceship_dimensions, spaceship_dimensions)

#red player movement controls
def r_movement(keys_pressed, r_player):
  keys_pressed = pygame.key.get_pressed()
  if keys_pressed[pygame.K_a] and r_player.x - 2 > 0:
    r_player.x -= 2
  if keys_pressed[pygame.K_d] and r_player.x + 2 < 400:
    r_player.x += 2
  if keys_pressed[pygame.K_w] and r_player.y - 2 > 0:
    r_player.y -= 2
  if keys_pressed[pygame.K_s] and r_player.y + 2 < screen_height - spaceship_dimensions:
    r_player.y += 2

#yellow player movement controls
def y_movement(keys_pressed, y_player):
  keys_pressed = pygame.key.get_pressed()
  if keys_pressed[pygame.K_LEFT] and y_player.x - 2 > 460:
    y_player.x -= 2
  if keys_pressed[pygame.K_RIGHT] and y_player.x + 2 < 860:
    y_player.x += 2
  if keys_pressed[pygame.K_UP] and y_player.y - 2 > 0:
    y_player.y -= 2
  if keys_pressed[pygame.K_DOWN] and y_player.y + 2 < screen_height - spaceship_dimensions:
    y_player.y += 2


#main game loop
run = True
while run:
    
  #handling game FPS
  clock = pygame.time.Clock()
  clock.tick(60)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
    if event.type == pygame.KEYDOWN and game_over == False:
      if event.key == pygame.K_g and len(r_bullets) < 8:
        bullet = pygame.Rect(r_player.x + spaceship_dimensions, r_player.y + (spaceship_dimensions // 2 - 3), 10, 5)
        bullet_sfx.play()
        r_bullets.append(bullet)
      if event.key == pygame.K_m and len(y_bullets) < 8:
        bullet = pygame.Rect(y_player.x - 5, y_player.y + (spaceship_dimensions // 2 - 2), 10, 5)
        bullet_sfx.play()
        y_bullets.append(bullet)
          
    #list of all keys being pressed
  keys_pressed = pygame.key.get_pressed()
    
  r_movement(keys_pressed, r_player)
  y_movement(keys_pressed, y_player)
      
  for x in y_bullets:
    if r_player.colliderect(x) and r_health != 0:
      r_health -= 20
      hit_sfx.play()
      print(r_health)
      y_bullets.remove(x)
  for x in r_bullets:
    if y_player.colliderect(x) and y_health != 0:
      y_health -= 20
      hit_sfx.play()
      r_bullets.remove(x)
  

  if y_health == 0:
    game_over = True
    winner = r_player
  if r_health == 0:
    game_over = True
    winner = y_player

  draw_game(r_player, y_player)

pygame.quit()