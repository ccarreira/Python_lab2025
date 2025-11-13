import pygame, random
import numpy as np

pygame.init()

WIDTH = 260
HEIGHT = 200

# ** PYGAME INIT **************************
clock = pygame.time.Clock()

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("NOISE 01")

# ** UTIL **************************

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

# ** MAIN ********************
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            raise SystemExit

    dt  = clock.tick(60) / 1000.0
    #x += vel * delta_s

    #get Mouse Pos
    mouseX, mouseY = pygame.mouse.get_pos()
    mouse_pos = pygame.math.Vector2(mouseX, mouseY)
    
    # clear screen
    pygame.draw.rect(window, BLACK, (0, 0, WIDTH, HEIGHT), width=0)

    for grid_x in range(1, WIDTH, 1):
        for grid_y in range(1, HEIGHT, 1):
            #color = random.choice([(255,255,0), (255,255,0), (0,255,255)])
            #color = random.choice([RED, GREEN, BLUE, WHITE])
            #color = random.choice([BLACK, WHITE])
            color = random.randint(0, 255)
            pygame.draw.line(window, (color, color, color), (grid_x, grid_y), (grid_x, grid_y), width=1)
     
    pygame.display.update()




"""

#line
pygame.draw.line(surface, color, (x1, y1), (x2, y2), width=1)

#Múltiplas linhas
pygame.draw.lines(surface, color, closed, [(x,y), ...], width=1)

#Retângulo
pygame.draw.rect(surface, color, (x, y, w, h), width=0)
#width=0 desenha sólido.

#Círculo
pygame.draw.circle(surface, color, (cx, cy), radius, width=0)

#Elipse
pygame.draw.ellipse(surface, color, (x, y, w, h), width=0)

#Polígono
pygame.draw.polygon(surface, color, [(x,y), ...], width=0)

#Arco
pygame.draw.arc(surface, color, (x, y, w, h), start_angle, end_angle, width=1)
#Ângulos em radianos.

#Linha anti-aliased
pygame.draw.aaline(surface, color, (x1, y1), (x2, y2))

#Múltiplas anti-aliased
pygame.draw.aalines(surface, color, closed, [(x,y), ...])

"""