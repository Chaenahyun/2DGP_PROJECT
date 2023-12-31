#play_top_inning_pitcher.py
#수비 이닝(초)
#투수: 플레이어 / 타자: AI
from pico2d import *

import game_framework
from game_world import collide
from ground_batting_and_pitching import Ground_batting_and_pitching
from pitcher import Pitcher
from batter_AI import Batter_AI
from fast_ball import Fast_ball, target_positions_strike, target_positions_ball
from breaking_ball import Breaking_ball




# 시작 여부
running = True
pitcher = Pitcher()
batter_AI = Batter_AI()
ground_batting_and_pitching = Ground_batting_and_pitching()
fast_ball = Fast_ball()
breaking_ball = Breaking_ball(380, 200, 5, 0.02)

zoon = load_image('resource/zoon.png')
#title = load_image('resource/title.png')

bgm = load_music('resource_music/bg2.WAV')
bgm.set_volume(32)
bgm.repeat_play()

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

def handle_collision():
    global running
    # 현재는 함수의 매개변수로 self를 받지 않는데, self가 필요한 경우 self를 전달하도록 변경해야 합니다.
    if collide(batter_AI, fast_ball):
        batter_AI.handle_collision('batter_AI:fast_ball', fast_ball)


def update():
    ground_batting_and_pitching.update()
    pitcher.update()
    batter_AI.update()
    fast_ball.update()
    breaking_ball.update()
    handle_collision()


def draw():
    clear_canvas()
    ground_batting_and_pitching.draw()
    zoon.draw(70, 350, 200, 200)
    #title.draw(800//2, 450//2, 800, 450)

    x, y = 10, 430
    text = "원하는 위치를 키보드로 입력하세요!"

    # 폰트 초기화
    font = load_font('neodgm.TTF', 20)

    font.draw(x, y, text)

    pitcher.draw()
    batter_AI.draw()
    fast_ball.draw()
    breaking_ball.draw()

    update_canvas()

while running:
    handle_events()
    update()
    handle_collision()
    draw()
    delay(0.1)

close_canvas()
