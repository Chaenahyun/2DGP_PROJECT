#play_mode.py

import random
import math
from pico2d import *
import game_framework
import game_world
import play_top_inning_pitcher
import play_top_inning_fielder
import play_bottom_inning_batter
import play_bottom_inning_runner
from pitcher import Pitcher
from pitcher_AI import Pitcher_AI
from batter import Batter
from batter_AI import Batter_AI
#from catcher import Catcher
from runner import Runner
from fielder import Fielder
from fast_ball import Fast_ball
from fast_ball_AI import Fast_ball_AI
from breaking_ball import Breaking_ball
from breaking_ball_AI import Breaking_ball_AI
#from fly_ball import Fly_ball
from hit import Hit
#from homerun import Homerun
#from foul_ball import Foul_ball
#from ground_ball import Ground_ball
from ground_full import Ground_full
from ground_batting_and_pitching import Ground_batting_and_pitching


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        # else:
        #     pitcher.handle_event(event)
        #     pitcher_AI.handle_event(event)
        #     batter.handle_event(event)
        #     batter_AI.handle_event(event)
        #     runner.handle_event(event)
        #     #catcher.handle_event(event)
        #     fielder.handle_event(event)




def init():
    global running, ground_batting_and_pitching, ground_full, pitcher, pitcher_AI, batter, batter_AI, runner, fielder, fast_ball

    running = True

    #map
    ground_batting_and_pitching = Ground_batting_and_pitching()
    game_world.add_object(ground_batting_and_pitching, 0)
    ground_full = Ground_full()
    game_world.add_object(ground_full, 0)

    #player
    batter = Batter() #타자
    game_world.add_object(batter, 2)
    game_world.add_collision_pair('fast_ball:batter', batter, None)

    batter_AI = Batter_AI()
    game_world.add_object(batter_AI, 2)
    game_world.add_collision_pair('fast_ball:batter_AI', batter_AI, None)

    # catcher = Catcher() #포수
    # game_world.add_object(catcher, 2)
    # game_world.add_collision_pair('', catcher, None)

    #runner = Runner() #주자
    #game_world.add_object(runner, 2)
    #game_world.add_collision_pair('', runner, None)

    #fielder = Fielder() # 수비수
    #game_world.add_object(fielder, 2)
    #game_world.add_collision_pair('', fielder, None)

    #공
    fast_ball = Fast_ball()
    game_world.add_object(fast_ball, 1)
    game_world.add_collision_pair('fast_ball:batter_AI', None, fast_ball)


def finish():
    game_world.clear()
    pass


def update():
    game_world.update()
    game_world.handle_collisions()

def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause():
    pass

def resume():
    pass

