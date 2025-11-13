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
    pg.display.set_caption("Simple Noise Map")
    clock = pg.time.Clock()

    scale = 0.02
    seed = random.randint(0, 10000)

    surface = pg.Surface((GRID_W, GRID_H))
    px = pg.PixelArray(surface)

    for y in range(GRID_H):
        for x in range(GRID_W):
            n = pnoise2((x + seed) * scale, (y + seed) * scale)
            n = int((n + 1) * 127.5)  # normalize [-1,1] → [0,255]
            px[x, y] = (n << 16) | (n << 8) | n  # grayscale
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
