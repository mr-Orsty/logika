python
import pygame as pg
import random

pg.init()

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

bg = pg.image.load("background.png")
ship_img = pg.image.load("shipImage.png")
pg.display.set_icon(pg.image.load("shipIcon.png"))

score = 0
time_limit = 5
spawn_time = pg.time.get_ticks() + time_limit * 1000
ship_timer_duration = 1000
ship_timer = None

scr = pg.display.set_mode((800, 600))
pg.display.set_caption("Galaxy Invaders")

pg.mouse.set_visible(False)

ship_box_size = 38
ship_rect = ship_img.get_rect(topleft=(random.randint(0, 800 - ship_box_size), random.randint(0, 600 - ship_box_size)))

f1 = pg.font.Font(None, 60)
f2 = pg.font.Font(None, 36)

click_mode = True
run = True
clock = pg.time.Clock()

def reset_ship():
    global ship_rect, ship_timer
    ship_rect.topleft = random.randint(0, 800 - ship_box_size), random.randint(0, 600 - ship_box_size)
    ship_timer = pg.time.get_ticks() + ship_timer_duration

reset_ship()

while run:
    current_time = pg.time.get_ticks()
    time_left = max(0, (spawn_time - current_time) // 1000)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
            pg.quit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_c:
                click_mode = not click_mode
            if (event.key == pg.K_x or event.key == pg.K_z) and click_mode and red_square_rect.colliderect(ship_rect):
                if time_left > 0:
                    score += 1
                    print("Score: " + str(score))
                    reset_ship()

    (mouse_x, mouse_y) = pg.mouse.get_pos()
    red_square_rect = pg.Rect(mouse_x - 16, mouse_y - 16, 32, 32)

    if time_left == 0:
        square_color = RED
        if run:
            final_text = f1.render("Final Score: " + str(score), 1, (255, 255, 255))
            scr.blit(final_text, ((800 - final_text.get_width()) // 2, 250))
            pg.display.flip()
            pg.time.wait(4000)
            run = False
            continue
    else:
        square_color = RED if not red_square_rect.colliderect(ship_rect) or not click_mode else GREEN

    if ship_timer and current_time > ship_timer:
        reset_ship()

    if red_square_rect.colliderect(ship_rect):
        if click_mode:
            square_color = GREEN
        else:
            score += 1
            print("Score: " + str(score))
            reset_ship()

    scr.blit(bg, (0, 0))
    text1 = f1.render("Score: " + str(score), 1, (255, 255, 255))
    scr.blit(text1, (10, 10))
    timer_text = f2.render(f"{max(0, ship_timer - current_time) / 1000:.1f}", True, (255, 255, 255))
    scr.blit(timer_text, (ship_rect.x + ship_rect.width // 2 - timer_text.get_width() // 2, ship_rect.y - 20))
    text2 = f1.render("Time Left: " + str(time_left) if time_left > 0 else "Time's Up!", 1, (255, 255, 255))
    scr.blit(text2, (800 - text2.get_width() - 10, 10))
    pg.draw.rect(scr, square_color, red_square_rect)
    scr.blit(ship_img, ship_rect.topleft)
    pg.display.flip()

    clock.tick(144)

final_text = f1.render("Final Score: " + str(score), 1, (255, 255, 255))
scr.blit(final_text, ((800 - final_text.get_width()) // 2, 250))
pg.display.flip()

pg.time.wait(4000)
pg.quit()