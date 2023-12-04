from pico2d import *

class Fielder:
    def __init__(self):
        self.idle_image = load_image('resource/idle_defender.png')
        self.running_left_image = load_image('resource/running_defender_to_left.png')
        self.running_right_image = load_image('resource/running_defender_to_right.png')
        self.running_right_image = load_image('resource/catching_and_throwing_defender.png')
        self.running_right_image = load_image('resource/catching_ground_ball_and_throwing_defender.png')
        self.running_right_image = load_image('resource/jump_catching_and_throwing_defender.png')
        self.x = 400
        self.y = 160
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

    def update(self):
        # x 방향 이동
        if self.dir_x > 0:
            if self.x + self.dir_x * 5 + self.character_width // 2 <= 800:
                self.x += self.dir_x * 5
        elif self.dir_x < 0:
            if self.x + self.dir_x * 5 - self.character_width // 2 >= 0:
                self.x += self.dir_x * 5

        # y 방향 이동
        if self.dir_y > 0:
            if self.y + self.dir_y * 5 + self.character_height // 2 <= 450:
                self.y += self.dir_y * 5
        elif self.dir_y < 0:
            if self.y + self.dir_y * 5 - self.character_height // 2 >= 0:
                self.y += self.dir_y * 5

        self.frame = (self.frame + 1) % 8
        self.idle_frame = (self.idle_frame + 1) % 8

    def draw(self):
        if self.is_idle:
            character_image = self.character_images[0]
            character_image.clip_draw(0, 0, 45, 45, self.x, self.y, 30, 30)
        else:
            character_image = self.character_images[self.frame % 6]
            character_image.clip_draw(0, 0, 45, 45, self.x, self.y, 30, 30)