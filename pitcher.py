from pico2d import *

ground_width, ground_height = 800, 450
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 450

open_canvas(ground_width, ground_height)

ground = load_image('ground_pitching.png')
hitter_left_handed = load_image('pitcher.png')
surprised_pitcher = load_image('surprised_pitcher.png')
fast_ball = load_image('fast_ball.png')

running = True
x, y = 400, 180
frame = 0  # 변수 초기화
start_pitching = False  #투구 애니메이션 재생 여부를 나타내는 변수


def draw():
    clear_canvas()
    ground.draw(ground_width // 2, ground_height// 2)
    hitter_left_handed.clip_draw(frame * 45, 0, 45, 45, x, y, 50, 50)
    fast_ball.clip_draw(frame * 20, 0, 20, 20, x, y, 100, 100)
    update_canvas()

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

def update():
    global frame, start_pitching
    if start_pitching:
        frame = (frame + 1) % 8
        delay(0.2)
        if frame == 0:  # 애니메이션이 마지막 프레임에 도달하면 재생을 멈춤
            start_pitching = False

running = True

while running:
    handle_events()
    draw()
    update()

close_canvas()
