from pico2d import *

ground_width, ground_height = 800, 450
open_canvas(ground_width, ground_height)
ground = load_image('ground_hitting.png')

# 타자 sprite
hitter_left_handed = load_image('hitter_left_handed.png')
hitter_right_handed = load_image('hitter_right_handed.png')
# 타자 idle sprite
idle_hitter_left_handed = load_image('idle_hitter_left_handed.png')
idle_hitter_right_handed = load_image('idle_hitter_right_handed.png')

running = True

# 우타자 초기 위치
hitter_right_handed_x = 230  # 초기 x 좌표
hitter_right_handed_y = 150  # 초기 y 좌표

hitter_frame = 0
hitter_idle_frame = 8
hitter_frame_count = 8

hitting_delay = 0.1
hitter_idle_delay = 0.2

start_hitting = False
start_idle = False

def handle_events():
    global running, start_hitting
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        #마우스 좌클릭 시 스윙
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            start_hitting = True

def draw():
    clear_canvas()
    ground.draw(ground_width // 2, ground_height // 2)

    if start_hitting:
        hitter_right_handed.clip_draw(hitter_frame * 80, 0, 80, 80,
            hitter_right_handed_x, hitter_right_handed_y, 490, 300)

    if not start_hitting:
        idle_hitter_right_handed.clip_draw(hitter_idle_frame * 50, 0, 50, 50,
                    hitter_right_handed_x, hitter_right_handed_y, 300, 300)

    update_canvas()

def update():
    global hitter_frame, hitter_idle_frame, start_hitting, start_idle

    if start_hitting:
        hitter_frame = (hitter_frame + 1) % hitter_frame_count
        delay(hitting_delay)

        if hitter_frame == 0:
            start_hitting = False

    # 스윙하지 않을 때는 idle 애니메이션 재생
    if not start_hitting:
        hitter_idle_frame = (hitter_idle_frame + 1) % hitter_frame_count
        delay(hitter_idle_delay)

while running:
    handle_events()
    draw()
    update()

close_canvas()
