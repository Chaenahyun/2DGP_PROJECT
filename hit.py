# hit.py
from pico2d import *
import random
import server

class Hit:
    def __init__(self):
        self.ball = load_image('resource/ball.png')
        self.hit = False
        self.ball_x, self.ball_y = 0, 0
        self.initial_ball_x, self.initial_ball_y = 400, 30
        self.speed = 10
        self.target_x, self.target_y = 0, 0



    def handle_events(self):
        pass

    def move_ball_randomly(self):
        target_index = random.randint(0, len(target_positions_hit) - 1)
        self.set_target_position(target_positions_hit[target_index])
        self.hit = True

    def set_target_position(self, target):
        if not self.hit:
            self.hit = True
            self.ball_x, self.ball_y = self.initial_ball_x, self.initial_ball_y
            self.set_target(target)

    def set_target(self, target):
        self.target_x, self.target_y = target

    def get_bb(self):
        return self.ball_x - 2, self.ball_y - 2, self.ball_x + 2, self.ball_y + 2

    # def handle_collision(self, group, other):
    #     if group == 'batter_AI:fast_ball':
    #         print(f'{group}과 충돌 감지!')
            #game_framework.push_mode(play_top_inning_fielder)

    def update(self):
        if self.hit:
            dir_x = self.target_x - self.ball_x
            dir_y = self.target_y - self.ball_y
            length = math.sqrt(dir_x ** 2 + dir_y ** 2)

            if length != 0:
                dir_x /= length
                dir_y /= length

                move_distance = self.speed
            self.ball_x += dir_x * move_distance
            self.ball_y += dir_y * move_distance

            tolerance = 30

            if abs(self.ball_x - self.target_x) < tolerance and abs(self.ball_y - self.target_y) < tolerance:
                self.hit = False



    def draw(self):
        if self.hit:
            self.ball.draw(self.ball_x, self.ball_y, 10, 10)



# 목표 위치
target_positions_hit = [
    (20, 250), (200, 300), (400, 300), (600,300), (700, 250), #장타
    (5, 310), (200, 400), (400, 400), (600, 400), (795, 310), #홈런
    (200, 150), (300, 150), (400, 200), (300, 150), (600, 150), #단타
    (200, 150), (300, 150), (400, 200), (300, 150), (600, 150), #단타
    (270, 100), (350, 140), (400, 160), (450, 140), (700, 250), #땅볼
    (270, 100), (350, 140), (400, 160), (450, 140), (700, 250), #땅볼
    (270, 100), (350, 140), (400, 160), (450, 140), (700, 250) #땅볼
]

# (20, 250), (200, 300), (400, 300), (600,300), (700, 250), #장타
# (5, 310), (200, 400), (400, 400), (600, 400), (795, 310), #홈런
# (200, 150), (300, 150), (400, 200), (300, 150), (600, 150), #단타
# (200, 150), (300, 150), (400, 200), (300, 150), (600, 150), #단타
# (270, 100), (350, 140), (400, 160), (450, 140), (700, 250) #땅볼
# (270, 100), (350, 140), (400, 160), (450, 140), (700, 250) #땅볼
# (270, 100), (350, 140), (400, 160), (450, 140), (700, 250) #땅볼