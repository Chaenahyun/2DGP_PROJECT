#주자(마우스 클릭으로 이동)
from pico2d import *

ground_width, ground_height = 800, 450
open_canvas(ground_width, ground_height)

#이미지 로드
ground = load_image('ground_full.png')
running_runner_left = load_image('running_runner_left.png')
running_runner_right = load_image('running_runner_right.png')
runner = load_image('idle_runner_left.png')

running = True

#주자 초기 위치
runner_x = 495
runner_y = 100

#마우스 좌표
move_arrow_x, move_arrow_y = runner_x, runner_y

#프레임
runner_frame = 0
runner_idle_frame = 0

#프레임 수
runner_frame_count = 8
runner_idle_frame_count = 8

#시작 여부
start_running = False
start_idle = False

#마우스 좌클릭한 위치에 주자 이동
def handle_events():
    global running
    global runner_x, runner_y
    global move_arrow_x, move_arrow_y

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_MOUSEBUTTONDOWN:   #마우스 좌클릭으로 주자 이동
            move_arrow_x, move_arrow_y = event.x, ground_height - 1 - event.y



while running:
    clear_canvas()
    ground.draw(ground_width // 2, ground_height // 2)
    running_runner_left.clip_draw(runner_frame * 45, 0, 45, 45, runner_x, runner_y, 50, 50)

    if runner_x < move_arrow_x:
        runner_x += 5
    elif runner_x > move_arrow_x:
        runner_x -= 5

    if runner_y < move_arrow_y:
        runner_y += 5
    elif runner_y > move_arrow_y:
        runner_y -= 5

    update_canvas()
    handle_events()
    runner_frame = (runner_frame + 1) % runner_frame_count
    delay(0.1)

close_canvas()
