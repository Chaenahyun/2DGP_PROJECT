from pico2d import *

ground_width, ground_height =800, 450
open_canvas(ground_width, ground_height)
ground = load_image('ground_pitching.png')

pitcher = load_image('pitcher.png')
surprised_pitcher = load_image('surprised_pitcher.png')

running = True
x = 400  # 초기 x 좌표
y = 180  # 초기 y 좌표
frame = 0  # 변수 초기화
dir_x = 0
dir_y = 0

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 450

character_width = 60
character_height = 60


def handle_events():
    global running, dir_x, dir_y, pitcher, is_idle, idle_frame  # 전역 변수
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
    pitcher.clip_draw(frame * 45, 0, 45, 45, x, y, 50, 50)

    update_canvas()
    handle_events()

    frame = (frame + 1) % 8
    delay(0.2)

    if not running:
        break

close_canvas()
