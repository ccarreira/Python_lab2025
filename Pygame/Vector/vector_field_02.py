import pygame

pygame.init()

WIDTH = 600
HEIGHT = 400

# ** PYGAME INIT **************************
clock = pygame.time.Clock()

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("VECTOR FIELD")

# ** UTIL **************************

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

# ** INIT **************************
spacing = 80
magnitude = 150

# ** MAIN ********************
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    delta_ms = clock.tick(60)
    delta_s  = delta_ms / 1000.0
    #x += vel * delta_s

    mouseX, mouseY = pygame.mouse.get_pos()
    mouse_pos = pygame.math.Vector2(mouseX, mouseY)

    pygame.draw.rect(window, BLACK, (0, 0, WIDTH, HEIGHT), width=0)
    for grid_x in range(spacing // 2, WIDTH, spacing):
        for grid_y in range(spacing // 2, HEIGHT, spacing):

            grid_pos = pygame.math.Vector2(grid_x, grid_y)
            
            #destino - origem
            direction = pygame.math.Vector2(mouse_pos - grid_pos)
            distance_to_mouse = direction.magnitude()
            if distance_to_mouse != 0: direction = pygame.math.Vector2.normalize(direction)
            
            #end_pos = origem + direção_normalizada * magnitude
            end_pos = pygame.math.Vector2(grid_pos + (direction * magnitude))
            
            pygame.draw.line(window, WHITE, grid_pos, end_pos, width=1)
            #STAR EFFECT
            if distance_to_mouse == 0 or distance_to_mouse >= magnitude:
                continue
            pygame.draw.line(window, RED, mouse_pos, end_pos, width=4)


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