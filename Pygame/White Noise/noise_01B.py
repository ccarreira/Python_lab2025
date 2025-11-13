import pygame, random
import numpy as np

pygame.init()


# ** PYGAME INIT **************************

WIDTH, HEIGHT = 1260, 1200
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("White Noise")
clock = pygame.time.Clock()

surf = pygame.Surface((WIDTH, HEIGHT))


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

    #BW
    # random 0 or 255 for each pixel (H×W)
    bw = np.random.choice([0, 255], (WIDTH, HEIGHT, 1)).astype(np.uint8)
    # duplicate across R,G,B channels
    arr = np.repeat(bw, 3, axis=2)

    # write array into surface and draw
    pygame.surfarray.blit_array(surf, arr)

    window.blit(surf, (0, 0))

    pygame.display.flip()
    dt  = clock.tick(60) / 1000.0
        
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