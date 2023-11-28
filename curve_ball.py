# curve_ball.py
from pico2d import *
import math


class Curve_Ball:
    def __init__(self, x, y, speed, delay, size=15):
        self.ball = load_image("ball.png")  # 이미지 파일의 경로를 정확하게 지정
        self.initial_x, self.initial_y = x, y
        self.x, self.y = x, y
        self.speed = speed
        self.size = size
        self.delay = delay
        self.frame = 0
        self.frame_count = 8
        self.t = 0.0
        self.points = []
        self.start_pitching = False
        self.curve_ball = self.ball  # 이미지를 할당

    def handle_events(self, ball_object=None):
        global running
        events = get_events()
        for event in events:
            if event.type == SDL_QUIT:
                running = False
            elif event.type == SDL_KEYDOWN:
                if event.key == SDLK_ESCAPE:
                    running = False
                elif event.key in [SDLK_1, SDLK_2, SDLK_3, SDLK_4, SDLK_5, SDLK_6, SDLK_7, SDLK_8, SDLK_9]:
                    target_index = int(event.key - SDLK_1)
                    ball_object.set_target_position(target_index)
                elif event.key in [SDLK_a, SDLK_b, SDLK_c, SDLK_d, SDLK_e, SDLK_f, SDLK_g, SDLK_h]:
                    target_index = int(event.key - SDLK_a)
                    ball_object.set_target_position(target_index, is_strike=False)

    def get_bezier_point(self, p0, p1, p2, p3, t):
        u = 1 - t
        tt = t * t
        uu = u * u
        uuu = uu * u
        ttt = tt * t

        p = uuu * p0
        p += 3 * uu * t * p1
        p += 3 * u * tt * p2
        p += ttt * p3

        return p

    def set_target(self, target):
        target_x, target_y = target
        self.points.clear()
        for t in range(0, 101):
            self.t = t / 100.0
            x = self.get_bezier_point(self.x, target_x, target_x, target_x, self.t)
            y = self.get_bezier_point(self.y, self.y, target_y, target_y, self.t)
            self.points.append((x, y))

    def set_target_position(self, index, is_strike=True):
        if not self.start_pitching:
            self.start_pitching = True
            self.x, self.y = self.initial_x, self.initial_y
            self.size = 15  # 초기 크기로 되돌림
            self.t = 0.0

            if is_strike:
                self.set_target(target_positions_strike[index])
            else:
                self.set_target(target_positions_ball[index])

    def draw(self):
        if self.start_pitching and self.t <= 1.0:
            self.curve_ball.draw(self.x, self.y, self.size, self.size)
            self.size += 0.1

    def update(self):
        if self.start_pitching and self.t <= 1.0:
            elapsed_time = get_time()

            if elapsed_time > self.delay:
                self.frame = (self.frame + 1) % self.frame_count
                index = int(self.t * 100)
                target_x, target_y = self.points[index]

                dir_x = target_x - self.x
                dir_y = target_y - self.y
                length = math.sqrt(dir_x ** 2 + dir_y ** 2)

                if length != 0:
                    dir_x /= length
                    dir_y /= length

                    self.x += dir_x * self.speed
                    self.y += dir_y * self.speed

                self.t += 0.01

                if self.t > 1.0:
                    self.start_pitching = False
                    self.size = 15  # 초기 크기로 되돌림

# 초기 위치
initial_ball_x, initial_ball_y = (380, 200)

# 목표 위치
target_positions_strike = [
    (380, 150), (405, 150), (430, 150),
    (380, 125), (405, 125), (430, 125),
    (380, 90), (405, 90), (430, 90)
]

target_positions_ball = [
    (350, 180), (405, 180), (470, 180),
    (350, 125), (465, 125), (350, 50),
    (405, 50), (470, 50)
]