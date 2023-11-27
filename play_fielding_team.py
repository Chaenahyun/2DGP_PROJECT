#play_fielding_team.py
from pico2d import *
from ground_fielder import Ground_fielder
from pitcher import Pitcher
from batter import Batter


# 캔버스 열기
ground_width, ground_height = 800, 450
open_canvas(ground_width, ground_height)

# 시작 여부
running = True

# Pitcher와 Batter 객체 생성
pitcher = Pitcher()
batter = Batter()
ground_fielder = Ground_fielder()
#curve_ball = Curve_Ball()

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

def update():
    ground_fielder.update()
    pitcher.update()
    batter.update()
    #curve_ball.update()

def draw():
    clear_canvas()
    ground_fielder.draw()
    pitcher.draw()
    batter.draw()
    #curve_ball.draw()
    update_canvas()

while running:
    handle_events()
    update()
    draw()
    delay(0.1)

close_canvas()
