#batter_AI.py

from pico2d import *
import random

import game_framework


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

    def get_bb(self):
        #배트 바운딩 박스
        half_width = 5  # 바운딩 박스 가로 크기의 절반
        half_height = 5  # 바운딩 박스 세로 크기의 절반
        offset_x = 150
        return (self.hitter_right_handed_x - half_width+ offset_x, self.hitter_right_handed_y - half_height,
                self.hitter_right_handed_x + half_width+ offset_x, self.hitter_right_handed_y + half_height)


    def handle_collision(self, group, other):
        if group == 'batter_AI:fast_ball':
            print(f'{group}과 충돌 감지!')
            #game_framework.push_mode(play_top_inning_fielder)


    def draw(self):
        if self.start_hitting:
            self.hitter_right_handed.clip_draw(self.hitter_frame * 80, 0, 80, 80,
                self.hitter_right_handed_x, self.hitter_right_handed_y, 385, 250)
            draw_rectangle(*self.get_bb())

        else:
            self.idle_hitter_right_handed.clip_draw(self.hitter_idle_frame * 50, 0, 50, 50,
                        self.hitter_right_handed_x, self.hitter_right_handed_y, 250, 250)


    def update(self, start_pitching=None):
        self.hitter_idle_frame = (self.hitter_idle_frame + 1) % self.hitter_idle_frame_count

        # 일정한 확률로 start_hitting을 재생
        if start_pitching and not self.start_hitting and random.random() <= 0.1:
            self.start_hitting = True
            print(f'스윙!')

        if self.start_hitting:
            self.hitter_frame = (self.hitter_frame + 1) % self.hitter_frame_count
            #print(f'스윙!')

            if self.hitter_frame == 0:
                self.start_hitting = False