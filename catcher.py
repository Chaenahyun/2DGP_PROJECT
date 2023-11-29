from pico2d import *

ground_width, ground_height = 800, 450
open_canvas(ground_width, ground_height)
ground = load_image('resource/ground_full.png')

catching_catcher = load_image('resource/catching_catcher.png')
idle_catcher = load_image('resource/idle_catcher.png')

#시작 여부
running = True
start_catching = False
start_catcher_idle = False

#초기 위치
catcher_x = 398# 초기 x 좌표
catcher_y = 40  # 초기 y 좌표

#프레임
catcher_frame = 0
catcher_idle_frame = 0

#프레임 수
catcher_frame_count = 8
catcher_idle_frame_count = 8

#딜레이
catching_delay = 0.1
catcher_idle_delay = 0.2

# 핸들 이벤트
def handle_events():
    global running, start_catching
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_SPACE and not start_catching:
                start_catching = True

def draw():
    clear_canvas()
    ground.draw(ground_width // 2, ground_height // 2)

    if start_catching:
        catching_catcher.draw(catcher_x, catcher_y, 30, 30)

    if not start_catching:
        idle_catcher.draw(catcher_x, catcher_y, 30, 30)

    update_canvas()

def update():
    global start_catching, catching_delay, catcher_idle_delay, catcher_frame, catcher_idle_frame

    if start_catching:
        catcher_frame = (catcher_frame + 1) % catcher_frame_count
        delay(catching_delay)

        # 만약 캐칭이 완료되면 다시 idle 상태로 전환
        if catcher_frame == catcher_frame_count - 1:
            start_catching = False

    # 캐칭하지 않을 때는 idle 애니메이션 재생
    if not start_catching:
        catcher_idle_frame = (catcher_idle_frame + 1) % catcher_idle_frame_count
        delay(catcher_idle_delay)

while running:
    handle_events()
    draw()
    update()

close_canvas()
