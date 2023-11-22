from pico2d import *

# 캔버스 열기
ground_width, ground_height = 800, 450
open_canvas(ground_width, ground_height)
# load image
ground = load_image('ground_fielder.png')
# pitcher
idle_pitcher = load_image('idle_pitcher.png')
pitching_pitcher = load_image('pitching_pitcher.png')

# 시작 여부
running = True
start_pitching = False
draw_fast_ball = False

# 초기 위치
pitcher_x, pitcher_y = 400, 200

# 프레임
pitcher_frame = 0
pitcher_idle_frame = 0

# 프레임 수
pitcher_frame_count = 8
pitcher_idle_frame_count = 8

# 딜레이
pitching_delay = 0.1
pitcher_idle_delay = 0.3

# 핸들 이벤트
def handle_events():
    global running, start_pitching
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

    if start_pitching:
        pitching_pitcher.clip_draw(pitcher_frame * 45, 0, 45, 45, pitcher_x, pitcher_y, 100, 100)

    update_canvas()

def update():
    global pitcher_frame, start_pitching, \
        draw_fast_ball, pitcher_idle_frame

    if start_pitching:
        pitcher_frame = (pitcher_frame + 1) % pitcher_frame_count

        delay(pitching_delay)

        # start_pitching 애니메이션이 마지막 프레임에 도달하면 재생을 멈춤
        if pitcher_frame == 0:
            start_pitching = False



while running:
    handle_events()
    draw()
    update()

close_canvas()