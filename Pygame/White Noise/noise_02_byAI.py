#VIBE CODING


# pip install pygame noise
import pygame as pg
from noise import pnoise2
import random

W, H   = 800, 600           # janela
TW, TH = 2, 2                # tamanho do tile (px)
GRID_W, GRID_H = W//TW, H//TH

# parâmetros de ruído (fBM)
OCTAVES      = 5
PERSISTENCE  = 0.5
LACUNARITY   = 2.0

def fbm(x, y, scale, seed):
    """Fractal Brownian Motion com pnoise2 normalizado para [0,1]."""
    n = pnoise2((x+seed)*scale, (y+seed)*scale,
                octaves=OCTAVES, persistence=PERSISTENCE,
                lacunarity=LACUNARITY, repeatx=1_000_000, repeaty=1_000_000, base=0)
    # pnoise2 retorna ~[-1,1]; normaliza para [0,1]
    return 0.5 * (n + 1.0)

def gen_map(surf, scale, seed, offset=(0.0, 0.0)):
    """Gera o mapa para uma Surface, aplicando thresholds de bioma."""
    ox, oy = offset
    pxarray = pg.PixelArray(surf)
    for gy in range(GRID_H):
        for gx in range(GRID_W):
            # amostragem contínua; offset para pan
            h = fbm(gx + ox, gy + oy, scale, seed)

            # opcional: ruído secundário para “umidade” → variação de cor
            m = fbm(gx + 10000 + ox, gy + 10000 + oy, scale*0.8, seed+1234)

            # thresholds de altura → biomas
            if h < 0.35:
                color = (0, 40 + int(100*h), 180)             # água
            elif h < 0.40:
                color = (194, 178, 128)                        # areia
            elif h < 0.60:
                # mistura de verdes conforme “umidade”
                g = 120 + int(80*m)
                color = (40, g, 40)                            # relva
            elif h < 0.75:
                color = (34, 96, 34)                           # floresta
            elif h < 0.88:
                color = (110, 110, 110)                        # rocha
            else:
                color = (240, 240, 240)                        # neve

            pxarray[gx, gy] = surf.map_rgb(color)
    del pxarray  # desbloqueia a Surface

def main():
    pg.init()
    screen = pg.display.set_mode((W, H))
    pg.display.set_caption("Map generation with noise (pygame)")
    clock = pg.time.Clock()

    # Surface do mapa na resolução de tiles; depois “scale” para janela
    map_surf = pg.Surface((GRID_W, GRID_H))
    scale    = 0.015          # menor → features maiores; maior → noise mais “apertado”
    seed     = random.randint(0, 10_000)
    offset   = [0.0, 0.0]     # pan contínuo (setas)
    dirty    = True

    running = True
    while running:
        dt = clock.tick(60) / 1000.0

        for e in pg.event.get():
            if e.type == pg.QUIT:
                running = False
            elif e.type == pg.KEYDOWN:
                if e.key == pg.K_r:       # nova seed
                    seed = random.randint(0, 10_000)
                    dirty = True
                elif e.key == pg.K_q:     # escala ↓
                    scale = max(0.003, scale * 0.8)
                    dirty = True
                elif e.key == pg.K_e:     # escala ↑
                    scale = min(0.06, scale * 1.25)
                    dirty = True

        # pan com setas (offset em unidades de grid)
        keys = pg.key.get_pressed()
        speed = 100.0 * dt
        if keys[pg.K_LEFT]:  offset[0] -= speed
        if keys[pg.K_RIGHT]: offset[0] += speed
        if keys[pg.K_UP]:    offset[1] -= speed
        if keys[pg.K_DOWN]:  offset[1] += speed
        if any((keys[pg.K_LEFT], keys[pg.K_RIGHT], keys[pg.K_UP], keys[pg.K_DOWN])):
            dirty = True

        if dirty:
            gen_map(map_surf, scale, seed, offset)
            dirty = False

        # desenha: upscale do mapa “de tiles” para a janela
        pg.transform.scale(map_surf, (W, H), screen)

        # HUD mínimo
        pg.draw.rect(screen, (0,0,0), (0,0,340,22))
        font = pg.font.SysFont(None, 18)
        hud = font.render(f"seed={seed}  scale={scale:.4f}  arrows=pan  R=resear  Q/E=zoom", True, (255,255,255))
        screen.blit(hud, (6, 4))

        pg.display.flip()

    pg.quit()

if __name__ == "__main__":
    main()
