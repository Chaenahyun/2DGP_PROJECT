from pico2d import *
import math
import game_framework
import server

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 10.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
#RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
RUN_SPEED_PPS = 200


class Fielder:
    def __init__(self):
        self.idle_image = load_image('resource/idle_defender.png')
        self.running_left_image = load_image('resource/running_defender_to_left.png')
        self.running_right_image = load_image('resource/running_defender_to_right.png')
        # self.throwing1 = load_image('resource/catching_and_throwing_defender.png')
        # self.throwing2 = load_image('resource/catching_ground_ball_and_throwing_defender.png')
        # self.throwing3 = load_image('resource/jump_catching_and_throwing_defender.png')
        self.x = 0
        self.y = 0
        self.frame = 0
        self.dir_x = 0
        self.dir_y = 0
        self.character_width = 60
        self.character_height = 60
        self.is_idle = True
        self.idle_frame = 0

    def handle_events(self):
        events = get_events()
        for event in events:
            if event.type == SDL_QUIT:
                self.running = False
            elif event.type == SDL_KEYDOWN:
                if event.key == SDLK_RIGHT:
                    self.dir_x += 1
                    self.is_idle = False
                elif event.key == SDLK_LEFT:
                    self.dir_x -= 1
                    self.is_idle = False
                elif event.key == SDLK_UP:
                    self.dir_y += 1
                    self.is_idle = False
                elif event.key == SDLK_DOWN:
                    self.dir_y -= 1
                    self.is_idle = False
                elif event.key == SDLK_ESCAPE:
                    self.running = False
            elif event.type == SDL_KEYUP:
                if event.key == SDLK_RIGHT:
                    self.dir_x -= 1
                elif event.key == SDLK_LEFT:
                    self.dir_x += 1
                elif event.key == SDLK_UP:
                    self.dir_y -= 1
                elif event.key == SDLK_DOWN:
                    self.dir_y += 1

    def move_towards_ball(self, ball):
        if ball is None:
            return  # ball 객체가 None이면 아무 작업도 하지 않음

        # 공의 위치로 이동하는 로직을 작성
        target_x, target_y = ball.x, ball.y
        self.dir = math.atan2(target_y - self.y, target_x - self.x)
        self.speed = RUN_SPEED_PPS
        self.x += self.speed * math.cos(self.dir) * game_framework.frame_time
        self.y += self.speed * math.sin(self.dir) * game_framework.frame_time



    def draw(self):
        if self.is_idle:
            self.idle_image.clip_draw(self.frame * 45, 0, 45, 45,
                                      self.x, self.y, 30, 30)
        elif self.dir_x < 0:
            self.running_right_image.clip_draw(self.frame * 45, 0, 45, 45,
                                      self.x, self.y, 30, 30)
        else:
            self.running_left_image.clip_draw(self.frame * 45, 0, 45, 45,
                                      self.x, self.y, 30, 30)

    def update(self):
        self.move_towards_ball(server.hit)
        #print('공을 향해 이동!')

        # x 방향 이동
        if self.dir_x > 0:
            if self.x + self.dir_x * 5 + self.character_width // 2 <= 800:
                self.x += self.dir_x * 5
            self.frame = (self.frame + 1) % 8
        elif self.dir_x < 0:
            if self.x + self.dir_x * 5 - self.character_width // 2 >= 0:
                self.x += self.dir_x * 5
            self.frame = (self.frame + 1) % 8

        # y 방향 이동
        if self.dir_y > 0:
            if self.y + self.dir_y * 5 + self.character_height // 2 <= 450:
                self.y += self.dir_y * 5
            self.frame = (self.frame + 1) % 8

        elif self.dir_y < 0:
            if self.y + self.dir_y * 5 - self.character_height // 2 >= 0:
                self.y += self.dir_y * 5
            self.frame = (self.frame + 1) % 8

        # 이동하지 않을 때 체크 (dir_x와 dir_y가 모두 0인 경우)
        if self.dir_x == 0 and self.dir_y == 0:
            self.is_idle = True
            self.idle_frame = (self.idle_frame + 1) % 8
        else:
            self.is_idle = False
