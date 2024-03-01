import pygame as pg
from random import randrange
from threading import Thread
from time import sleep

pg.init()

RED = (255, 0, 0)
GREEN = (0, 255, 0)

score = 0

scr = pg.display.set_mode((800, 600))
pg.display.set_caption("idk")

pg.mouse.set_visible(False)

green_square_size = 32
green_square_x = randrange(0, 800 - green_square_size)
green_square_y = randrange(0, 600 - green_square_size)
green_square_rect = pg.Rect(green_square_x, green_square_y, green_square_size, green_square_size)

run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
            pg.quit()

    (mouse_x, mouse_y) = pg.mouse.get_pos()
    red_square_rect = pg.Rect(mouse_x - 16, mouse_y - 16, 32, 32)

    if red_square_rect.colliderect(green_square_rect):
        score += 1
        print(score)
        green_square_x = randrange(0, 800 - green_square_size)
        green_square_y = randrange(0, 600 - green_square_size)
        green_square_rect.topleft = (green_square_x, green_square_y)

    scr.fill((0, 0, 0))
    pg.draw.rect(scr, RED, red_square_rect)
    pg.draw.rect(scr, GREEN, green_square_rect)
    pg.display.flip()
