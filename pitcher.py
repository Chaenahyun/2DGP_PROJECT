from pico2d import *
from fast_ball import Fast_Ball, target_positions_strike, target_positions_ball
from breaking_ball import Breaking_ball

class Pitcher:
    def __init__(self):
        self.idle_image = load_image('resource/idle_pitcher.png')
        self.pitching_image = load_image('resource/pitching_pitcher.png')

        self.x, self.y = 400, 200
        self.frame = 0
        self.idle_frame_count = 8
        self.pitching_frame_count = 8
        self.idle_delay = 0.3
        self.pitching_delay = 0.01

        self.start_pitching = False
        self.fast_ball = Fast_Ball()

    def handle_event(self, event):
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_SPACE and not self.start_pitching:
                self.start_pitching = True
            elif event.key in [SDLK_1, SDLK_2, SDLK_3, SDLK_4, SDLK_5, SDLK_6, SDLK_7, SDLK_8, SDLK_9,
                               SDLK_a, SDLK_b, SDLK_c, SDLK_d, SDLK_e, SDLK_f, SDLK_g, SDLK_h] and not self.start_pitching:
                self.start_pitching = True

    def update(self):
        if self.start_pitching:
            self.frame = (self.frame + 1) % self.pitching_frame_count

            if self.frame == 0:
                self.start_pitching = False
        else:
            self.frame = (self.frame + 1) % self.idle_frame_count

    def draw(self):
        if self.start_pitching:
            self.pitching_image.clip_draw(self.frame * 45, 0, 45, 45, self.x, self.y, 100, 100)
        else:
            self.idle_image.clip_draw(self.frame * 45, 0, 45, 45, self.x, self.y, 100, 100)

