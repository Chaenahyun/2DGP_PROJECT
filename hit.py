# hit.py
from pico2d import *
import math
import random
import game_framework

class Hit:
    def __init__(self):
        self.ball = load_image('resource/ball.png')
        self.start_pitching = False
        self.ball_x, self.ball_y = 0, 0
        self.initial_ball_x, self.initial_ball_y = 400, 10
        self.speed = 5
        self.ball_frame = 0
        self.ball_frame_count = 8
        self.ball_size = 20
        self.target_x, self.target_y = 0, 0

    def handle_events(self):
        pass

    def move_ball_randomly(self):
        target_index = random.randint(0, len(target_positions_hit) - 1)
        self.set_target_position(target_positions_hit[target_index])
        self.start_pitching = True

    def set_target_position(self, target):
        if not self.start_pitching:
            self.start_pitching = True
            self.ball_x, self.ball_y = self.initial_ball_x, self.initial_ball_y
            self.ball_size = 15  # 초기 크기로 되돌림
            self.set_target(target)

    def set_target(self, target):
        self.target_x, self.target_y = target

    def update(self):
        if self.start_pitching:
            self.ball_frame = (self.ball_frame + 1) % self.ball_frame_count

            dir_x = self.target_x - self.ball_x
            dir_y = self.target_y - self.ball_y
            length = math.sqrt(dir_x ** 2 + dir_y ** 2)

            if length != 0:
                dir_x /= length
                dir_y /= length

                move_distance = self.speed
                self.ball_x += dir_x * move_distance
                self.ball_y += dir_y * move_distance

            self.ball_size += 0.8

            tolerance = 1

            if abs(self.ball_x - self.target_x) < tolerance and abs(self.ball_y - self.target_y) < tolerance:
                self.start_pitching = False
                self.ball_size = 15  # 초기 크기로 되돌림

    def draw(self):
        if self.start_pitching:
            self.ball.draw(self.ball_x, self.ball_y, self.ball_size, self.ball_size)

# 목표 위치
target_positions_hit = [
    (10, 400), (400, 400), (790, 400),
]
