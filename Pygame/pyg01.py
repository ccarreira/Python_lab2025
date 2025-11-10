import pygame

pygame.init()

# ** PYGAME INIT **************************
clock = pygame.time.Clock()
window = pygame.display.set_mode((1500,400))

x = 0
vel = 100  # px/s

# ** MAIN ********************
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    delta_ms = clock.tick(60)
    delta_s  = delta_ms / 1000.0

    x += vel * delta_s

    # desenho
    window.fill((0,0,0))
    pygame.draw.rect(window, (255,0,255), (x,0,50,30))

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