import pygame as pg
import random

pg.init()

RED = (255, 0, 0)
GREEN = (0, 255, 0)

bg = pg.image.load("background.png")
ship_img = pg.image.load("shipImage.png")
pg.display.set_icon(pg.image.load("shipIcon.png"))

score = 0
time_limit = 30
spawn_time = pg.time.get_ticks() + time_limit * 1000

scr = pg.display.set_mode((800, 600))
pg.display.set_caption("galaxy invaders")

pg.mouse.set_visible(False)

ship_box_size = 38
ship_rect = ship_img.get_rect()

f1 = pg.font.Font(None, 60)

run = True
clock = pg.time.Clock()
while run:
    current_time = pg.time.get_ticks()
    time_left = max(0, (spawn_time - current_time) // 1000)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
            pg.quit()

    (mouse_x, mouse_y) = pg.mouse.get_pos()
    red_square_rect = pg.Rect(mouse_x - 16, mouse_y - 16, 32, 32)

    if red_square_rect.colliderect(ship_rect):
        score += 1
        print("Score: " + str(score))
        ship_rect.topleft = random.randint(0, 800 - ship_rect.width), random.randint(0, 600 - ship_rect.height)

    if time_left == 0:
        run = False

    if current_time >= spawn_time:
        green_square_x = random.randint(0, 800 - ship_box_size)
        green_square_y = random.randint(0, 600 - ship_box_size)
        ship_rect.topleft = (green_square_x, green_square_y)
        spawn_time = current_time + time_limit * 1000

    text1 = f1.render("Score: " + str(score), 1, (255, 255, 255))
    if time_left > 0:
        text2 = f1.render("Time Left: " + str(time_left), 1, (255, 255, 255))
    else:
        text2 = f1.render("Time's Up!", 1, (255, 255, 255))
    scr.blit(bg, (0, 0))
    scr.blit(text1, (10, 10))
    scr.blit(text2, (800 - text2.get_width() - 10, 10))
    pg.draw.rect(scr, RED, red_square_rect)
    scr.blit(ship_img, ship_rect.topleft)
    pg.display.flip()

    clock.tick(144)

final_text = f1.render("Final Score: " + str(score), 1, (255, 255, 255))
scr.blit(final_text, ((800 - final_text.get_width()) // 2, 250))
pg.display.flip()

pg.time.wait(4000)
pg.quit()
