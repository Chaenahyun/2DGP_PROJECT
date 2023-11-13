#마우스 클릭으로 이동
from pico2d import *

ground_width, ground_height = 800, 450
open_canvas(ground_width, ground_height)
ground = load_image('ground.png')
running_runner_left = load_image('running_runner_left.png')
running_runner_right = load_image('running_runner_right.png')
#runner = load_image('idle_runner_left.png')
#runner = load_image('idle_runner_right.png')

def handle_events():
    global running
    global character_x, character_y
    global move_arrow_x, move_arrow_y

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_MOUSEBUTTONDOWN:
            move_arrow_x, move_arrow_y = event.x, ground_height - 1 - event.y

running = True
frame = 0
x = 495  #초기 x좌표
y = 83  #초기 y좌표
move_arrow_x, move_arrow_y = x, y
#hide_cursor()

while running:
    clear_canvas()
    ground.draw(ground_width // 2, ground_height // 2)
    running_runner_left.clip_draw(frame * 45, 0, 45, 45, x, y, 30, 30)

    if x < move_arrow_x:
        x += 5
    elif x > move_arrow_x:
        x -= 5

    if y < move_arrow_y:
        y += 5
    elif y > move_arrow_y:
        y -= 5

    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    delay(0.1)

close_canvas()
