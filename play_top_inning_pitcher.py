#play_top_inning_pitcher.py
from pico2d import *
from ground_batting_and_pitching import Ground_batting_and_pitching
from pitcher import Pitcher
from batter_AI import Batter_AI
from fast_ball import Fast_ball, target_positions_strike, target_positions_ball
from breaking_ball import Breaking_ball

# 캔버스 열기
ground_width, ground_height = 800, 450
open_canvas(ground_width, ground_height)

# 시작 여부
running = True

# 객체 생성
pitcher = Pitcher()
batter_AI = Batter_AI()
ground_batting_and_pitching = Ground_batting_and_pitching()
fast_ball = Fast_ball()
breaking_ball = Breaking_ball(380, 200, 5, 0.02)


def handle_events():
    global running
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        else:
            pitcher.handle_event(event)
            batter_AI.handle_events()

            if event.type == SDL_KEYDOWN:
                if event.key in [SDLK_1, SDLK_2, SDLK_3, SDLK_4, SDLK_5, SDLK_6, SDLK_7, SDLK_8, SDLK_9]:
                    target_index = int(event.key - SDLK_1)
                    # fast_ball 객체에 접근하여 set_target_position 호출
                    fast_ball.set_target_position(target_positions_strike[target_index])
                    batter_AI.start_hitting = True

                elif event.key in [SDLK_a, SDLK_b, SDLK_c, SDLK_d, SDLK_e, SDLK_f, SDLK_g, SDLK_h]:
                    target_index = int(event.key - SDLK_a)
                    # fast_ball 객체에 접근하여 set_target_position 호출
                    fast_ball.set_target_position(target_positions_ball[target_index])
                    batter_AI.start_hitting = True


def update():
    ground_batting_and_pitching.update()
    pitcher.update()
    batter_AI.update()
    fast_ball.update()
    breaking_ball.update()

def draw():
    clear_canvas()
    ground_batting_and_pitching.draw()
    pitcher.draw()
    batter_AI.draw()
    fast_ball.draw()
    breaking_ball.draw()
    update_canvas()

while running:
    handle_events()
    update()
    draw()
    delay(0.1)

close_canvas()
