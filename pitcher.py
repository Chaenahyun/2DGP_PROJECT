from pico2d import *
from fast_ball import Fast_ball, target_positions_strike, target_positions_ball
from breaking_ball import Breaking_ball

class Pitcher:
    def __init__(self):
        self.idle_image = load_image('resource/idle_pitcher.png')
        self.pitching_image = load_image('resource/pitching_pitcher.png')

        self.pitcher_x, self.pitcher_y = 400, 200

        self.pitcher_frame = 0
        self.pitcher_idle_frame = 0

        self.pitcher_idle_frame_count = 8
        self.pitcher_frame_count = 8

        self.start_pitching = False

        self.fast_ball = Fast_ball()
        self.breaking_ball = Breaking_ball

    def handle_event(self, event):
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_SPACE and not self.start_pitching:
                self.start_pitching = True
            elif event.key in [SDLK_1, SDLK_2, SDLK_3, SDLK_4, SDLK_5, SDLK_6, SDLK_7, SDLK_8, SDLK_9,
                               SDLK_a, SDLK_b, SDLK_c, SDLK_d, SDLK_e, SDLK_f, SDLK_g, SDLK_h] and not self.start_pitching:
                self.start_pitching = True

                if event.key in [SDLK_1, SDLK_2, SDLK_3, SDLK_4, SDLK_5, SDLK_6, SDLK_7, SDLK_8, SDLK_9]:
                    target_index = int(event.key - SDLK_1)
                    # fast_ball 객체에 접근하여 set_target_position 호출
                    self.fast_ball.set_target_position(target_positions_strike[target_index])
                elif event.key in [SDLK_a, SDLK_b, SDLK_c, SDLK_d, SDLK_e, SDLK_f, SDLK_g, SDLK_h]:
                    target_index = int(event.key - SDLK_a)
                    # fast_ball 객체에 접근하여 set_target_position 호출
                    self.fast_ball.set_target_position(target_positions_ball[target_index])


    def draw(self):
        if self.start_pitching:
            self.pitching_image.clip_draw(self.pitcher_frame * 45, 0, 45, 45,
                            self.pitcher_x, self.pitcher_y, 100, 100)
        else:
            self.idle_image.clip_draw(self.pitcher_frame * 45, 0, 45, 45,
                            self.pitcher_x, self.pitcher_y, 100, 100)

    def update(self):
        if self.start_pitching:
            self.pitcher_frame = (self.pitcher_frame + 1) % self.pitcher_frame_count

            if self.pitcher_frame == 0:
                self.start_pitching = False

        if not self.start_pitching:
            self.pitcher_idle_frame = (self.pitcher_idle_frame + 1) % self.pitcher_idle_frame_count

