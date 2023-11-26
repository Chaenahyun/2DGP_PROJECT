#fast_ball.py
from pico2d import *

# 캔버스 열기
ground_width, ground_height = 800, 450
open_canvas(ground_width, ground_height)
# load image
ball = load_image('ball.png')

# 시작 여부
running = True
start_pitching = False
draw_fast_ball = False

# 초기 위치
initial_ball_x, initial_ball_y = (380, 200)

target_positions_strike = [
    (380, 150),  # 1
    (405, 150),  # 2
    (430, 150),  # 3
    (380, 125),  # 4
    (405, 125),  # 5
    (430, 125),  # 6
    (380, 90),   # 7
    (405, 90),   # 8
    (430, 90)   # 9
]

target_positions_ball = [
    (350, 180),  # a
    (405, 180),  # b
    (470, 180),  # c
    (350, 125),  # d
    (465, 125),  # e
    (350, 50),  # f
    (405, 50),   # g
    (470, 50)    # h
]

ball_x, ball_y = initial_ball_x, initial_ball_y
pitcher_x, pitcher_y = 400, 200

# 초기 속도
speed = 5

# 프레임
ball_frame = 0
ball_frame_count = 8

# 딜레이
ball_delay = 0.02

# 초기 크기
ball_size = 15

# 목표 위치
target_x, target_y = 0, 0

# 핸들 이벤트
def handle_events():
    global running, start_pitching, ball_x, ball_y, ball_size
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key in [SDLK_1, SDLK_2, SDLK_3, SDLK_4, SDLK_5, SDLK_6, SDLK_7, SDLK_8, SDLK_9]:
                target_index = int(event.key - SDLK_1)
                set_target_position(target_positions_strike[target_index])
            elif event.key in [SDLK_a, SDLK_b, SDLK_c, SDLK_d, SDLK_e, SDLK_f, SDLK_g, SDLK_h]:
                target_index = int(event.key - SDLK_a)
                set_target_position(target_positions_ball[target_index])

def set_target_position(target):
    global start_pitching, ball_x, ball_y, ball_size
    clear_canvas()
    if not start_pitching:
        start_pitching = True
        ball_x, ball_y = initial_ball_x, initial_ball_y
        ball_size = 15  # 초기 크기로 되돌림
        set_target(target)

def set_target(target):
    global target_x, target_y

    target_x, target_y = target

# 애니메이션 재생
def draw():
    global ball_frame, start_pitching, ball_delay, ball_frame_count, ball_x, ball_y, ball_size

    clear_canvas()
    if start_pitching:

        # 볼을 그릴 때 크기를 적용
        ball.draw(ball_x, ball_y, ball_size, ball_size)
        ball_size += 0.2
    update_canvas()

def update():
    global ball_frame, start_pitching, ball_delay, ball_frame_count, ball_x, ball_y, target_x, target_y, speed

    if start_pitching:
        ball_frame = (ball_frame + 1) % ball_frame_count

        # 현재 위치에서 목표 위치까지의 벡터 계산
        dir_x = target_x - ball_x
        dir_y = target_y - ball_y

        # 벡터의 길이 계산
        length = math.sqrt(dir_x ** 2 + dir_y ** 2)

        # 벡터의 길이가 0이 아닌 경우에만 정규화하여 속도 벡터 계산
        if length != 0:
            # 벡터를 정규화하여 속도 벡터 계산
            dir_x /= length
            dir_y /= length

            # 현재 위치에서 목표 위치로 이동
            ball_x += dir_x * speed
            ball_y += dir_y * speed

        delay(ball_delay)

        # 목표 위치에 도달하면 애니메이션 종료
        tolerance = 5
        if abs(ball_x - target_x) < tolerance and abs(ball_y - target_y) < tolerance:
            start_pitching = False

while running:
    handle_events()
    draw()
    update()

close_canvas()
