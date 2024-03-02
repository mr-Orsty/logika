import pygame as pg
from random import randrange

pg.init()

RED = (255, 0, 0)
GREEN = (0, 255, 0)

bg = pg.image.load("background.jpg")
ship = pg.image.load("shipImage.png")
green_square_rect = ship.get_rect()

score = 0

scr = pg.display.set_mode((800, 600))
pg.display.set_caption("galaxy invaders")

pg.mouse.set_visible(False)

green_square_size = 32
green_square_x = randrange(0, 800 - green_square_size)
green_square_y = randrange(0, 600 - green_square_size)
green_square_rect = pg.Rect(green_square_x, green_square_y, green_square_size, green_square_size)

f1 = pg.font.Font(None, 60)

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
        print("Score: " + str(score))
        green_square_x = randrange(0, 800 - green_square_size)
        green_square_y = randrange(0, 600 - green_square_size)
        green_square_rect.topleft = (green_square_x, green_square_y)

    text1 = f1.render("Score: " + str(score), 1, (255, 255, 255))
    scr.blit(bg, (0, 0))
    scr.blit(text1, (10, 10))
    scr.blit(ship, green_square_rect)
    pg.draw.rect(scr, RED, red_square_rect)
    pg.draw.rect(scr, GREEN, green_square_rect)
    pg.display.flip()
