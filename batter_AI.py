from pico2d import *
import game_framework
import random

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class Batter_AI:
    def __init__(self):
        # 타자 sprite
        self.hitter_left_handed = load_image('resource/hitter_left_handed.png')
        self.hitter_right_handed = load_image('resource/hitter_right_handed.png')
        # 타자 idle sprite
        self.idle_hitter_left_handed = load_image('resource/idle_hitter_left_handed.png')
        self.idle_hitter_right_handed = load_image('resource/idle_hitter_right_handed.png')

        self.running = True

        # 우타자 초기 위치
        self.hitter_right_handed_x = 250  # 초기 x 좌표
        self.hitter_right_handed_y = 130  # 초기 y 좌표

        self.hitter_frame = 0
        self.hitter_idle_frame = 0

        self.hitter_frame_count = 8
        self.hitter_idle_frame_count = 8

        self.start_hitting = False

    def handle_events(self):
        pass

    def draw(self):
        if self.start_hitting:
            self.hitter_right_handed.clip_draw(self.hitter_frame * 80, 0, 80, 80,
                self.hitter_right_handed_x, self.hitter_right_handed_y, 385, 250)
        else:
            self.idle_hitter_right_handed.clip_draw(self.hitter_idle_frame * 50, 0, 50, 50,
                        self.hitter_right_handed_x, self.hitter_right_handed_y, 250, 250)

    def update(self):
        self.hitter_idle_frame = (self.hitter_idle_frame + 1) % self.hitter_idle_frame_count

        # 일정한 확률로 start_hitting을 재생
        if not self.start_hitting and random.random() <= 0.01:
            self.start_hitting = True

        if self.start_hitting:
            self.hitter_frame = (self.hitter_frame + 1) % self.hitter_frame_count

            if self.hitter_frame == 0:
                self.start_hitting = False