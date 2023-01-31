import pygame
import numpy as np

pygame.init()
  
WHITE = (255,255,255)
BLACK = (0, 0, 0)

W, H = 800, 800
GRID_SIZE = 70

canvas = pygame.display.set_mode((W, H))
  
pygame.display.set_caption("Gravity")
  
exit = False


grid = np.zeros((GRID_SIZE, GRID_SIZE, 2), dtype=np.int32)
offset_x = W / GRID_SIZE
offset_y = H / GRID_SIZE

for x in range(GRID_SIZE):
    for y in range(GRID_SIZE):
        grid[x,y,0] = x * offset_x
        grid[x,y,1] = y * offset_y

while not exit:
    canvas.fill(BLACK)
  
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            pygame.draw.circle(canvas, WHITE, grid[x,y], 1)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
  
    pygame.display.update()