#play_top_inning_pitcher.py
from pico2d import *
from ground_hitting_and_pitching import Ground_hitting_and_pitching
from pitcher import Pitcher
from batter import Batter
#from fast_ball import Fast_Ball, target_positions_strike, target_positions_ball
#from breaking_ball import Breaking_ball

# 캔버스 열기
ground_width, ground_height = 800, 450
open_canvas(ground_width, ground_height)

# 시작 여부
running = True

# 객체 생성
pitcher = Pitcher()
batter = Batter()
ground_hitting_and_pitching = Ground_hitting_and_pitching()
#fast_ball = Fast_Ball()
#breaking_ball = Breaking_ball(380, 200, 5, 0.02)

# play_fielding_team.py의 handle_events 함수
def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        else:
            pitcher.handle_event(event)
            batter.handle_events()

            if event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
                batter.start_hitting = True

            # elif event.type == SDL_KEYDOWN:
            #     if event.key in [SDLK_1, SDLK_2, SDLK_3, SDLK_4, SDLK_5, SDLK_6, SDLK_7, SDLK_8, SDLK_9]:
            #         target_index = int(event.key - SDLK_1)
            #         # fast_ball 객체에 접근하여 set_target_position 호출
            #         fast_ball.set_target_position(target_positions_strike[target_index])
            #     elif event.key in [SDLK_a, SDLK_b, SDLK_c, SDLK_d, SDLK_e, SDLK_f, SDLK_g, SDLK_h]:
            #         target_index = int(event.key - SDLK_a)
            #         # fast_ball 객체에 접근하여 set_target_position 호출
            #         fast_ball.set_target_position(target_positions_ball[target_index])


def update():
    ground_hitting_and_pitching.update()
    pitcher.update()
    batter.update()
    # fast_ball.update()
    # breaking_ball.update()

def draw():
    clear_canvas()
    ground_hitting_and_pitching.draw()
    pitcher.draw()
    batter.draw()
    # fast_ball.draw()
    # breaking_ball.draw()
    update_canvas()

while running:
    handle_events()
    update()
    draw()
    delay(0.1)

close_canvas()
