import pygame
import numpy as np
import math

pygame.init()
  
WHITE = (255,255,255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

W, H = 800, 800
GRID_SIZE = 70

canvas = pygame.display.set_mode((W, H))
  
pygame.display.set_caption("Gravity")

im = pygame.image.load("./julia.png").convert_alpha()

exit = False

START = -200
END = 200
grid = np.zeros((GRID_SIZE, GRID_SIZE, 2), dtype=np.int32)
offset_x = (W + abs(START) + END) / GRID_SIZE
offset_y = (H + abs(START) + END) / GRID_SIZE

gravity_points = []

gravity_force = 4000

selected = None

show_points = True

def update():
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            default_x = START + x * offset_x
            default_y = START + y * offset_y
            for p in gravity_points:
                dx = p[0] - default_x
                dy = p[1] - default_y
                d = math.sqrt(dx * dx + dy * dy)
                a = math.atan2(dy, dx)
                f = gravity_force / d
                if f > d:
                    f = d
                default_x += math.cos(a) * f
                default_y += math.sin(a) * f    
        
            grid[x,y,0] = default_x
            grid[x,y,1] = default_y

update()

while not exit:
    canvas.fill(WHITE)
  
    for x in range(1,GRID_SIZE):
        for y in range(1, GRID_SIZE):
            pygame.draw.line(canvas, BLACK, grid[x,y], grid[x-1, y], 2)
            pygame.draw.line(canvas, BLACK, grid[x,y], grid[x, y-1], 2)

    canvas.blit(im, (100,100))

    if show_points:
        for p in gravity_points:
            pygame.draw.circle(canvas, RED, p, 7)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()

                for i, p in enumerate(gravity_points):
                    if math.sqrt((pos[0] - p[0])**2 + (pos[1] - p[1])**2) < 10:
                        selected = i
            elif pygame.mouse.get_pressed()[2]:
                gravity_points.append(pygame.mouse.get_pos())
                update()
        elif event.type == pygame.MOUSEMOTION:
            if selected is not None:
                pos = pygame.mouse.get_pos()
                gravity_points[selected] = pos
                update()
        elif event.type == pygame.MOUSEBUTTONUP:
            selected = None
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            show_points = not show_points
  
    pygame.display.update()