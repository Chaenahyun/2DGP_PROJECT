# play_top_inning_fielder.py

from pico2d import *
from game_world import collide
from ground_full import Ground_full
from runner import Runner



# 캔버스 열기
ground_width, ground_height = 800, 450
open_canvas(ground_width, ground_height)

# 시작 여부
running = True

# 객체 생성
ground_full = Ground_full()
runner = Runner(x=200, y=200, speed=5, frame_count=8, idle_frame_count=8, running_delay=0.1, running_idle_delay=0.3)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False

def handle_collision():
    pass

def update():
    ground_full.update()
    runner.update()
    handle_collision()


def draw():
    clear_canvas()
    ground_full.draw()
    runner.draw()
    update_canvas()

while running:
    handle_events()
    update()
    handle_collision()
    draw()
    delay(0.1)

close_canvas()
