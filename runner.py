# 주자(마우스 클릭으로 이동)
from pico2d import *

ground_width, ground_height = 800, 450
open_canvas(ground_width, ground_height)

# 이미지 로드
ground = load_image('ground_full.png')
running_runner_to_left = load_image('running_runner_left.png')
running_runner_to_right = load_image('running_runner_right.png')
idle_runner = load_image('idle_runner_left.png')

running = True

# 주자 초기 위치
runner_x = 495
runner_y = 100

# 마우스 좌표
move_arrow_x, move_arrow_y = runner_x, runner_y

# 프레임
runner_frame = 0
runner_idle_frame = 0

# 프레임 수
runner_frame_count = 8
runner_idle_frame_count = 8

# 시작 여부
start_running = False
start_runner_idle = False

# 딜레이
running_delay = 0.15
running_idle_delay = 0.5


# 핸들 이벤트
# 마우스 좌클릭한 위치에 주자 이동
def handle_events():
    global running, runner_x, runner_y, move_arrow_x, move_arrow_y, start_running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        # 마우스 좌클릭으로 주자 이동
        elif event.type == SDL_MOUSEBUTTONDOWN:
            move_arrow_x, move_arrow_y = event.x, ground_height - 1 - event.y
            start_running = True


# 애니메이션 재생
def draw():
    global runner_frame, runner_idle_frame, start_running, runner_x, runner_y

    clear_canvas()
    ground.draw(ground_width // 2, ground_height // 2)

    if start_running:
        running_runner_to_left.clip_draw(runner_frame * 45, 0, 45, 45,
                                          runner_x, runner_y, 45, 45)
        if runner_x < move_arrow_x:
            runner_x += 5
        elif runner_x > move_arrow_x:
            runner_x -= 5

        if runner_y < move_arrow_y:
            runner_y += 5
        elif runner_y > move_arrow_y:
            runner_y -= 5

    # 달리지 않을 때는 idle 애니메이션 재생
    if not start_running:
        idle_runner.clip_draw(runner_idle_frame * 45, 0, 45, 45,
                              runner_x, runner_y, 45, 45)

    update_canvas()


def update():
    global runner_frame, runner_idle_frame, start_running

    # 달리기
    if start_running:
        runner_frame = (runner_frame + 1) % runner_frame_count
        delay(running_delay)

    # 달리지 않을 때는 idle 애니메이션 재생
    if not start_running:
        runner_idle_frame = (runner_idle_frame + 1) % runner_idle_frame_count
        delay(running_idle_delay)


while running:
    handle_events()
    draw()
    update()

close_canvas()
