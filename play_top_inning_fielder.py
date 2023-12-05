# play_top_inning_fielder.py
from pico2d import *
import game_framework
import game_world
import server
from ground_full import Ground_full
from fielder import Fielder
from hit import Hit
from background import FixedBackground as Background

# 시작 여부
running = True
print("play_top_inning_fielder init called!")

# 객체 생성
ground_full = Ground_full()
fielder = Fielder()
hit = Hit()
hit.move_ball_randomly()
print("안타!")
fielder.move_towards_ball(server.hit)
print('공이다!!!!!!!!')

def init():
    global fielder, ground_full, hit
    fielder = Fielder()
    ground_full = Ground_full()
    hit = Hit()
    hit.move_ball_randomly()
    fielder.move_towards_ball(server.hit)
    #print('공이다!!!!!!!!')

    server.background = Background()
    game_world.add_object(server.background, 0)
    server.fielder = Fielder()
    game_world.add_object(server.fielder, 1)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False

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


def create_fielders():
    # 각 Fielder 객체의 초기 위치를 직접 지정
    fielder_positions = [
        (500, 90), #1B
        (440, 140), #2B
        (360, 140), #SS
        (300, 90), #3B

        (200, 250), #LF
        (400, 300), #CF
        (600, 250), #RF
    ]

    for i, (x, y) in enumerate(fielder_positions):
        # 각 Fielder 객체를 다르게 초기화하여 생성
        fielder = Fielder()
        fielder.x, fielder.y = x, y
        # game_world에 추가
        game_world.add_object(fielder, 1)

# 게임 초기화 시에 호출하여 Fielder 객체를 생성하고 배치
create_fielders()


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
