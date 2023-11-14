from pico2d import *

ground_width, ground_height =800, 450
open_canvas(ground_width, ground_height)
ground = load_image('ground_hitting.png')

hitter_left_handed = load_image('hitter_left_handed.png')
hitter_right_handed = load_image('hitter_right_handed.png')
idle_hitter_left_handed = load_image('idle_hitter_left_handed.png')

running = True
x = 600  # 초기 x 좌표
y = 120  # 초기 y 좌표
frame = 0  # 변수 초기화

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 450

character_width = 55
character_height = 55


def handle_events():
    global running, dir_x, dir_y, hitter_left_handed, is_idle, idle_frame  # 전역 변수
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False


while running:
    clear_canvas()
    ground.draw(ground_width//2, ground_height//2)
    #hitter_left_handed.clip_draw(frame * 80, 0, 80, 80, x, y, 250, 250)
    idle_hitter_left_handed.clip_draw(frame * 50, 0, 50, 50, x, y, 250, 250)

    update_canvas()
    handle_events()

    frame = (frame + 1) % 8
    delay(0.3)

    if not running:
        break

close_canvas()
