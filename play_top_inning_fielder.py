# play_top_inning_fielder.py
from pico2d import *
import game_framework
import game_world
from ground_full import Ground_full
from fielder import Fielder
from hit import Hit

# 창 열기
ground_width, ground_height = 800, 450
open_canvas(ground_width, ground_height)

# 시작 여부
running = True

# 객체 생성
ground_full = Ground_full()
fielder = Fielder()
hit = Hit()

def init():
    print("play_top_inning_fielder init called!")
    global fielder, ground_full, hit
    fielder = Fielder()
    ground_full = Ground_full()
    hit = Hit()

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False

        elif event.key == SDLK_SPACE:
            hit.handle_events()
            print('스페이스바 눌림')

        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                fielder.dir_x += 1
                fielder.is_idle = False
            elif event.key == SDLK_LEFT:
                fielder.dir_x -= 1
                fielder.is_idle = False
            elif event.key == SDLK_UP:
                fielder.dir_y += 1
                fielder.is_idle = False
            elif event.key == SDLK_DOWN:
                fielder.dir_y -= 1
            elif event.key == SDLK_ESCAPE:
                fielder.running = False

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                fielder.dir_x -= 1
            elif event.key == SDLK_LEFT:
                fielder.dir_x += 1
            elif event.key == SDLK_UP:
                fielder.dir_y -= 1
            elif event.key == SDLK_DOWN:
                fielder.dir_y += 1





def update():
    ground_full.update()
    fielder.update()
    hit.update()
    game_world.update()

def draw():
    clear_canvas()
    ground_full.draw()
    fielder.draw()
    hit.draw()
    game_world.render()
    update_canvas()

# 게임 루프
while running:
    handle_events()
    update()
    draw()
    delay(0.1)

close_canvas()
