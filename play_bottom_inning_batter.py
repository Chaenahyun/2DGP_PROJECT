#play_top_inning_batter.py
#공격 이닝(말)
#투수: AI / 타자: 플레이어
from pico2d import *
import game_framework
from ground_batting_and_pitching import Ground_batting_and_pitching
from pitcher_AI import Pitcher_AI
from batter import Batter
from fast_ball import Fast_ball, target_positions_strike, target_positions_ball
from breaking_ball import Breaking_ball

# 캔버스 열기
ground_width, ground_height = 800, 450
open_canvas(ground_width, ground_height)

# 시작 여부
running = True

# 객체 생성
pitcher_AI = Pitcher_AI()
batter = Batter()
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
            pitcher_AI.handle_event(event)
            batter.handle_events()

            if event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
                batter.start_batting = True


def update():
    ground_batting_and_pitching.update()
    pitcher_AI.update()
    batter.update()
    fast_ball.update()
    breaking_ball.update()


def draw():
    clear_canvas()
    ground_batting_and_pitching.draw()
    pitcher_AI.draw()
    batter.draw()
    fast_ball.draw()
    breaking_ball.draw()
    update_canvas()

while running:
    handle_events()
    update()
    draw()
    delay(0.1)

close_canvas()

