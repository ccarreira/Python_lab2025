import pygame as pg
import numpy as np

pg.init()

WIDTH, HEIGHT = 800, 600
window = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("NOISE 01")
clock = pg.time.Clock()

# surface to receive array data (match window size)
surf = pg.Surface((WIDTH, HEIGHT))

running = True
while running:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            running = False

    # --- build one BW frame (0 or 255) ---
    # shape must be (WIDTH, HEIGHT, 3) for surfarray with pygame
    bw = np.random.choice([0, 255], (WIDTH, HEIGHT, 1)).astype(np.uint8)
    arr = np.repeat(bw, 3, axis=2)  # RGB channels

    # write array into surface and draw
    pg.surfarray.blit_array(surf, arr)
    window.blit(surf, (0, 0))

    pg.display.flip()           # flip once per frame
    clock.tick(60)              # cap FPS

pg.quit()
