from pico2d import *

ground_width, ground_height = 800, 450

open_canvas(ground_width, ground_height)
ground = load_image('ground_pitching.png')
strike_zoon = load_image('strike_zoon.png')
pitcher_left_handed = load_image('pitcher.png')
fast_ball = load_image('fast_ball.png')

running = True
x_pitcher, y_pitcher = 400, 200
x_ball, y_ball = 380, 160
pitcher_frame, ball_frame = 0, 0

start_pitching = False
pitching_fast_ball = False
draw_fast_ball = False



pitcher_frame_count = 8
ball_frame_count = 5

pitching_delay = 0.1

def draw():
    clear_canvas()
    ground.draw(ground_width // 2, ground_height // 2)
    pitcher_left_handed.clip_draw(pitcher_frame * 45, 0, 45, 45, x_pitcher, y_pitcher, 100, 100)
    if draw_fast_ball:
        fast_ball.clip_draw(ball_frame * 20, 0, 20, 40, x_ball, y_ball, 100, 100)
    update_canvas()


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


def update():
    global pitcher_frame, ball_frame, start_pitching, pitching_fast_ball, draw_fast_ball

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


running = True

while running:
    handle_events()
    draw()
    update()

close_canvas()