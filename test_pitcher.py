from pico2d import *

open_canvas()
tuk_ground = load_image('TUK_GROUND.png')

TUK_WIDTH, TUK_HEIGHT = 800, 600
open_canvas(TUK_WIDTH, TUK_HEIGHT)

character_up = load_image('pitcher_red.png')

running = True
x = 100
y = 250
frame = 0

dir_y = 0

character_height = 20

def handle_events():
    global running, dir_y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_UP:
                dir_y = 1  # 위
            elif event.key == SDLK_DOWN:
                dir_y = -1  # 아래
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_UP or event.key == SDLK_DOWN:
                dir_y = 0

while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

    if dir_y > 0:  # 위로 이동
        y += dir_y * 5
    elif dir_y < 0:  # 아래로 이동
        if y + dir_y * 5 - character_height // 2 >= 0:
            y += dir_y * 5

    character_up.clip_draw(frame * 20, 0, 20, 20, x, y, 40, 40)

    update_canvas()
    handle_events()

    frame = (frame + 1) % 8
    delay(0.5)

    if not running:
        break

close_canvas()