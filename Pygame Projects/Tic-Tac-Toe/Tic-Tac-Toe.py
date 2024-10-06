import pygame
import pygame.locals

pygame.init()

white = (255,255,255)
black = (0,0,0)
green = (0,255,0)
red = (255,0,0)

clicked = False

pos = []
markers = []

player = 1 

line_width = 6

game_over = False
winner = 0

font = pygame.font.SysFont(None, 40)

screen_width = 300
screen_height = 300

screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill(white)
pygame.display.set_caption("Tic-Tac-Toe")

for x in range(3):
  row = [0] * 3
  markers.append(row)
  
def draw_grid():
  for x in range(1,3):
    pygame.draw.line(screen, black, (x * 100, 0), (x * 100, screen_height))
    pygame.draw.line(screen, black, (0, x * 100), (screen_width, x * 100))

def draw_markers():
  x_pos = 0
  for rows in markers:
    y_pos = 0
    for box in rows:
      if box == 1:
        pygame.draw.line(screen, red, (x_pos * 100 + 15, y_pos * 100 + 15), (x_pos * 100 + 85, y_pos * 100 + 85), line_width)
        pygame.draw.line(screen, red, (x_pos * 100 + 15, y_pos * 100 + 85), (x_pos * 100 + 85, y_pos * 100 + 15), line_width)
      if box == -1:
        pygame.draw.circle(screen, green, (x_pos * 100 + 50, y_pos * 100 + 50), 38, line_width)
      y_pos += 1
    x_pos += 1

def check_winner():
  global game_over
  global winner
  for x in markers:
    if sum(x) == 3:
      game_over = True
      winner = 'Player 1'
    if sum(x) == -3:
      game_over = True
      winner = 'Player 2'
  if markers[0][0] + markers[1][1] + markers[2][2] == 3 or markers[0][2] + markers[1][1] + markers[2][0] == 3:
    game_over = True
    winner = 'Player 1'
  if markers[0][0] + markers[1][1] + markers[2][2] == -3 or markers[0][2] + markers[1][1] + markers[2][0] == -3:
    game_over = True
    winner = 'Player 2' 
  if markers[0][0] + markers[1][0] + markers[2][0] == 3 or markers[0][1] + markers[1][1] + markers[2][1] == 3 or markers[0][2] + markers[1][2] + markers[2][2] == 3:
    game_over = True
    winner = "Player 1"
  if markers[0][0] + markers[1][0] + markers[2][0] == -3 or markers[0][1] + markers[1][1] + markers[2][1] == -3 or markers[0][2] + markers[1][2] + markers[2][2] == -3:
    game_over = True
    winner = "Player 2"

  total = 9
  for x in markers:
    for y in x:
      if y == 1 or y == -1:
        total -= 1
  if total == 0:
    game_over = True
    winner = "Nobody"
    
def display_winner():
  text = str(winner) + " Wins!"
  display = font.render(text, True, white)
  pygame.draw.rect(screen, black, (57, 125, 200, 50))
  screen.blit(display, (60, 140))


run = True
while run:

  draw_grid()
  draw_markers()
  
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
    if game_over == False:
      if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
        clicked = True
      if event.type == pygame.MOUSEBUTTONUP and clicked == True:
        clicked == False
        pos = pygame.mouse.get_pos()
        cell_x = pos[0]
        cell_y = pos[1]
        if markers[cell_x // 100][cell_y // 100] == 0:
          markers[cell_x // 100][cell_y // 100] = player
          player *= -1
          check_winner() 
      
  if game_over == True:
    display_winner()
      
  pygame.display.update()

pygame.quit()
