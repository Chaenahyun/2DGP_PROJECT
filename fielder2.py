#fielder.py
from pico2d import *

import random
import math
import game_framework
import game_world
from behavior_tree import BehaviorTree, Action, Sequence, Condition, Selector
import play_mode

import server

# Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 10.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 10.0

animation_names = ['Run', 'Idle', 'Catch', 'Throw']


class Fielder:
    images = None

    def load_images(self):
        if Fielder.images == None:
            Fielder.images = {}
            for name in animation_names:
                Fielder.images[name] = [load_image("") for i in range(1, 7)]
            Fielder.font = load_font('neodgm.TTF', 30)


    def __init__(self, name='Noname', x=0, y=0, size=1.0):
        self.name, self.x, self.y, self.size = name, x, y, size
        self.load_images()
        self.dir = 0.0      # radian 값으로 방향을 표시
        self.speed = 0.0
        self.frame = random.randint(0, 9)
        self.state = 'Idle'

        self.idle_image = load_image('resource/idle_defender.png')
        self.running_left_image = load_image('resource/running_defender_to_left.png')
        self.running_right_image = load_image('resource/running_defender_to_right.png')
        # self.throwing1 = load_image('resource/catching_and_throwing_defender.png')
        # self.throwing2 = load_image('resource/catching_ground_ball_and_throwing_defender.png')
        # self.throwing3 = load_image('resource/jump_catching_and_throwing_defender.png')
        self.x = 400
        self.y = 160
        self.frame = 0
        self.dir_x = 0
        self.dir_y = 0
        self.character_width = 60
        self.character_height = 60
        self.is_idle = True
        self.idle_frame = 0

        self.tx, self.ty = 0, 0
        self.build_behavior_tree()



    def __getstate__(self):
        state = {'name': self.name, 'x': self.x, 'y': self.y, 'size': self.size}
        return state

    def __setstate__(self, state):
        self.__init__()
        self.__dict__.update(state)


    def get_bb(self):
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50


    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        self.bt.run()


    def draw(self):
        sx, sy = self.x - server.background.window_left, self.y - server.background.window_bottom
        if math.cos(self.dir) < 0:
            Fielder.images[self.state][int(self.frame)].composite_draw(0, 'h', sx, sy, 100*self.size, 100*self.size)
        else:
            Fielder.images[self.state][int(self.frame)].draw(sx, sy, 100*self.size, 100*self.size)


    def handle_event(self, event):
        pass

    def handle_collision(self, group, other):
        pass

    def set_target_location(self, x=None, y=None):
        if not x or not y:
            raise ValueError('Location should be given')
        self.tx, self.ty = x, y
        return BehaviorTree.SUCCESS


    def distance_less_than(self, x1, y1, x2, y2, r):
        distance2 = (x1 - x2) ** 2 + (y1 - y2) ** 2
        return distance2 < (PIXEL_PER_METER * r) ** 2

    def move_slightly_to(self, tx, ty):
        self.dir = math.atan2(ty - self.y, tx - self.x)
        self.speed = RUN_SPEED_PPS
        self.x += self.speed * math.cos(self.dir) * game_framework.frame_time
        self.y += self.speed * math.sin(self.dir) * game_framework.frame_time

    def move_to(self, r=0.5):
        self.state = 'Run'
        self.move_slightly_to(self.tx, self.ty)
        if self.distance_less_than(self.tx, self.ty, self.x, self.y, r):
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.RUNNING



    def build_behavior_tree(self):
        a1 = Action('Set random location', self.move_to_ball)
        a2 = Action('Move to', self.move_to)
        root = SEQ_wander = Sequence('Idle', a1, a2)
        self.bt = BehaviorTree(root)
