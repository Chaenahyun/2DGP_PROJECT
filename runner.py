from pico2d import *

ground_width, ground_height = 800, 450
open_canvas(ground_width, ground_height)
ground = load_image('ground_full.png')
# 주자
running_runner_to_left = load_image('running_runner_left.png')
running_runner_to_right = load_image('running_runner_right.png')
idle_runner = load_image('idle_runner_left.png')
# 베이스
first_base = load_image('base.png')
second_base = load_image('base.png')
third_base = load_image('base.png')
home_base = load_image('home_base.png')

running = True

# 주자 초기 위치
runner_x = 420
runner_y = 30

# 마우스 좌표
move_arrow_x, move_arrow_y = runner_x, runner_y

# 현재 베이스의 인덱스
current_base_index = 0
# 베이스 위치
base_positions = [
    (495, 72),  # 1루 베이스
    (398, 122),  # 2루 베이스
    (300, 72),  # 3루 베이스
    (398, 23)  # 홈 베이스
]

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
running_delay = 0.1
running_idle_delay = 0.5


# 핸들 이벤트
# 마우스 좌클릭한 위치에 주자 이동
def handle_events():
    global running, runner_x, runner_y, move_arrow_x, move_arrow_y, start_running, current_base_index

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        # 숫자 키 입력 처리
        elif event.type == SDL_KEYDOWN and SDLK_1 <= event.key <= SDLK_4:
            base_index = event.key - SDLK_1
            move_to_base(base_index)


def move_to_base(base_index):
    global move_arrow_x, move_arrow_y, start_running, current_base_index

    move_arrow_x, move_arrow_y = base_positions[base_index]
    current_base_index = base_index
    start_running = True


# 애니메이션 재생
def draw():
    global runner_frame, runner_idle_frame, start_running, runner_x, runner_y

    clear_canvas()

    ground.draw(ground_width // 2, ground_height // 2)
    # 베이스를 그림
    for base_index, (base_x, base_y) in enumerate(base_positions):
        if base_index == 0:
            first_base.draw(base_x, base_y, 15, 15)
        elif base_index == 1:
            second_base.draw(base_x, base_y, 15, 15)
        elif base_index == 2:
            third_base.draw(base_x, base_y, 15, 15)
        elif base_index == 3:
            home_base.draw(base_x, base_y, 15, 15)

    # 주자 애니메이션을 그림
    if start_running:
        if current_base_index in [1, 2]:
            # 1루와 3루에서는 왼쪽으로 이동하는 애니메이션을 재생
            running_runner_to_left.clip_draw(runner_frame * 45, 0, 45, 45,
                                             runner_x, runner_y, 30, 30)
        elif current_base_index in [0, 3]:
            # 홈과 2루에서는 오른쪽으로 이동하는 애니메이션을 재생
            running_runner_to_right.clip_draw(runner_frame * 45, 0, 45, 45,
                                              runner_x, runner_y, 30, 30)

        # 주자의 좌표 업데이트
        if runner_x < move_arrow_x:
            runner_x += 5
        elif runner_x > move_arrow_x:
            runner_x -= 5

        if runner_y < move_arrow_y:
            runner_y += 5
        elif runner_y > move_arrow_y:
            runner_y -= 5
    # idle
    if not start_running:
        idle_runner.clip_draw(runner_idle_frame * 45, 0, 45, 45,
                              runner_x, runner_y, 30, 30)

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
