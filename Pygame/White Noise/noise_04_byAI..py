#VIBE CODING

# pip install pygame noise
import pygame as pg
from noise import pnoise2
import random

W, H = 800, 600
TILE = 4
GRID_W, GRID_H = W // TILE, H // TILE

def main():
    pg.init()
    screen = pg.display.set_mode((W, H))
    pg.display.set_caption("Binary Noise Map")
    clock = pg.time.Clock()

    scale = 0.012
    seed = random.randint(0, 10000)
    threshold = 0.0  # values above → white; below → black

    surface = pg.Surface((GRID_W, GRID_H))
    px = pg.PixelArray(surface)

    for y in range(GRID_H):
        for x in range(GRID_W):
            n = pnoise2((x + seed) * scale, (y + seed) * scale)
            color = 255 if n > threshold else 0
            px[x, y] = (color << 16) | (color << 8) | color
    del px

    running = True
    while running:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                running = False

        pg.transform.scale(surface, (W, H), screen)
        pg.display.flip()
        clock.tick(60)

    pg.quit()

if __name__ == "__main__":
    main()
