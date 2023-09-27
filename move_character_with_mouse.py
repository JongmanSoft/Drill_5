import random

from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass



running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
sx, sy = TUK_WIDTH // 2, TUK_HEIGHT // 2
rx ,ry = random.randint(200,700), random.randint(200,700)
p =0
frame = 0
hide_cursor()

while running:
    print(rx,ry)
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    hand.draw(rx,ry)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)

    update_canvas()
    frame = (frame + 1) % 8
    x = (1-p)*sx + p*rx
    y = (1 - p) * sy + p * ry
    p += 0.1
    if (p > 1.0):
        sx = x
        sy = y
        rx = random.randint(200,700)
        ry = random.randint(200, 700)
        p = 0
    handle_events()

close_canvas()




