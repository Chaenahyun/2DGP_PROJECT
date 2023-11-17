from pico2d import *

# 캔버스 열기
ground_width, ground_height = 800, 450
open_canvas(ground_width, ground_height)
# load image
ground = load_image('ground_pitching.png')
# strike zoon
strike_zoon = load_image('strike_zoon.png')
# pitcher
idle_pitcher = load_image('idle_pitcher.png')
pitching_pitcher = load_image('pitching_pitcher.png')
surprised_pitcher = load_image("surprised_pitcher.png")
# ball type
fast_ball = load_image('fast_ball.png')

# 시작 여부
running = True
start_pitching = False
start_pitcher_idle = False
pitching_fast_ball = False
draw_fast_ball = False

# 초기 위치
pitcher_x, pitcher_y = 400, 200
ball_x, ball_y = 380, 160

# 프레임
pitcher_frame = 0
pitcher_idle_frame = 0
surprised_pitcher_frame = 0
ball_frame = 0

# 프레임 수
pitcher_frame_count = 8
pitcher_idle_frame_count = 8
ball_frame_count = 5

# 딜레이
pitching_delay = 0.1
pitching_idle_delay = 0.3
ball_delay = 0.2

# 핸들 이벤트
def handle_events():
    global running, start_pitching, pitching_fast_ball
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_SPACE and not start_pitching:
                start_pitching = True

# 애니메이션 재생
def draw():
    clear_canvas()
    ground.draw(ground_width // 2, ground_height // 2)
    # 투수가 놀란 상태
    if pitching_fast_ball and draw_fast_ball:
        surprised_pitcher.clip_draw(surprised_pitcher_frame * 45, 0, 45, 45, pitcher_x, pitcher_y, 100, 100)
    # 그 외 상태에서는 투수가 던지는 애니메이션 재생
    else:
        pitching_pitcher.clip_draw(pitcher_frame * 45, 0, 45, 45, pitcher_x, pitcher_y, 100, 100)
    # 빠른 공 그리기
    if draw_fast_ball:
        fast_ball.clip_draw(ball_frame * 20, 0, 20, 40, ball_x, ball_y, 100, 100)
    update_canvas()

    # idle
    if not start_pitching:
        idle_pitcher.clip_draw(pitcher_idle_frame * 45, 0, 45, 45,
                               pitcher_x, pitcher_y, 100, 100)

    update_canvas()

def update():
    global pitcher_frame, ball_frame, start_pitching, pitching_fast_ball, \
        draw_fast_ball, pitcher_idle_frame, surprised_pitcher_frame, start_pitcher_idle

    if start_pitching:
        pitcher_frame = (pitcher_frame + 1) % pitcher_frame_count

        # start_pitching 애니메이션이 3번째 프레임에 도달하면 pitching_fast_ball 재생 시작
        if pitcher_frame == 3:
            pitching_fast_ball = True

        if pitching_fast_ball:
            draw_fast_ball = True
            ball_frame = (ball_frame + 1) % ball_frame_count
            if ball_frame == 0:
                pitching_fast_ball = False
                draw_fast_ball = False

        delay(pitching_delay)

        # start_pitching 애니메이션이 마지막 프레임에 도달하면 재생을 멈춤
        if pitcher_frame == 0:
            start_pitching = False

    # 공을 던지지 않을 때는 idle 애니메이션 재생
    if not start_pitching:
        pitcher_idle_frame = (pitcher_idle_frame + 1) % pitcher_idle_frame_count
        delay(pitching_idle_delay)


    # 투수가 놀란 애니메이션의 프레임 업데이트
    #surprised_pitcher_frame = (surprised_pitcher_frame + 1) % pitcher_frame_count

while running:
    handle_events()
    draw()
    update()

close_canvas()
