#play_top_inning_fielder.py

from pico2d import *
from ground_full import Ground_full
from runner import Runner
from fielder import Fielder


# 캔버스 열기
ground_width, ground_height = 800, 450
open_canvas(ground_width, ground_height)

# 시작 여부
running = True

# 객체 생성
runner = Runner()
fielder = Fielder()
ground_full = Ground_full()


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False


def update():
    ground_full.update()
    runner.update()
    fielder.update()


def draw():
    clear_canvas()
    ground_full.draw()
    runner.draw()
    fielder.draw()
    update_canvas()

while running:
    handle_events()
    update()
    draw()
    delay(0.1)

close_canvas()
