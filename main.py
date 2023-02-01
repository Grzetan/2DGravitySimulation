import pygame
import numpy as np
import math

pygame.init()
  
WHITE = (255,255,255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

W, H = 800, 800
GRID_SIZE = 100

canvas = pygame.display.set_mode((W, H))
  
pygame.display.set_caption("Gravity")
  
exit = False

START = -200
END = 200
grid = np.zeros((GRID_SIZE, GRID_SIZE, 2), dtype=np.int32)
offset_x = (W + abs(START) + END) / GRID_SIZE
offset_y = (H + abs(START) + END) / GRID_SIZE

gravity_points = [(200,200)]

gravity_force = 5000
falloff = 1

for x in range(GRID_SIZE):
    for y in range(GRID_SIZE):
        default_x = START + x * offset_x
        default_y = START + y * offset_y
        for p in gravity_points:
            dx = p[0] - default_x
            dy = p[1] - default_y
            d = math.sqrt(dx * dx + dy * dy)
            a = math.atan2(dy, dx)
            f = gravity_force / math.pow(d, falloff);
            if f > d:
                f = d
            default_x += math.cos(a) * f
            default_y += math.sin(a) * f    
    
        grid[x,y,0] = default_x
        grid[x,y,1] = default_y

while not exit:
    canvas.fill(WHITE)
  
    for x in range(1,GRID_SIZE):
        for y in range(1, GRID_SIZE):
            pygame.draw.line(canvas, BLACK, grid[x,y], grid[x-1, y])
            pygame.draw.line(canvas, BLACK, grid[x,y], grid[x, y-1])

    for p in gravity_points:
        pygame.draw.circle(canvas, RED, p, 4)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
  
    pygame.display.update()