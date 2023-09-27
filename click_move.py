from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')

goal =[(1280,1024)]
def handle_events():
    global running
    global cursor_x, cursor_y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEBUTTONDOWN and  event.button == 1:
            goal.append((event.x,  TUK_HEIGHT - 1 - event.y))
        elif event.type == SDL_MOUSEMOTION:
            cursor_x, cursor_y = event.x, TUK_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass



running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
sx, sy = TUK_WIDTH // 2, TUK_HEIGHT // 2
p =0
cursor_x = 0
cursor_y = 0

frame = 0
hide_cursor()

while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    for i in range (0,len(goal)):
        hand.draw(goal[i][0], goal[i][1])
    if (len(goal)>0):
        if (goal[i][0] > x): character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        else :  character.clip_draw(frame * 100, 0, 100, 100, x, y)
        x = (1-p)*sx + p*goal[0][0]
        y = (1-p)*sy + p*goal[0][1]
        p += 0.5
        if (p>=1):
            p =0
            sx = goal[0][0]
            sy = goal[0][1]
            

    hand.draw(cursor_x,cursor_y)
    update_canvas()
    frame = (frame + 1) % 8

    handle_events()

close_canvas()