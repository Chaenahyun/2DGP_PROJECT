#pitcher_AI.py
from pico2d import *
import random
from fast_ball_AI import Fast_ball_AI, target_positions_strike as fast_strike_targets
from breaking_ball_AI import Breaking_ball_AI, target_positions_strike as breaking_strike_targets

class Pitcher_AI:
    def __init__(self):
        self.idle_image = load_image('resource/idle_pitcher.png')
        self.pitching_image = load_image('resource/pitching_pitcher.png')

        self.pitcher_x, self.pitcher_y = 400, 200

        self.pitcher_frame = 0
        self.pitcher_idle_frame = 0

        self.pitcher_idle_frame_count = 8
        self.pitcher_frame_count = 8

        self.start_pitching = False
        self.selected_ball = None

        if not hasattr(self, 'pitching_sound'):
            self.pitching_sound = load_wav('resource_music/pitching.WAV')
            self.pitching_sound.set_volume(100)

    def throw_random_ball(self):
        ball_type = random.choice(["fast", "breaking"])
        if ball_type == "fast":
            self.selected_ball = Fast_ball_AI()
            target_index = random.randint(0, len(fast_strike_targets) - 1)
            self.selected_ball.set_target_position(fast_strike_targets[target_index])
            self.start_pitching = True
            self.pitching_sound.play()
        elif ball_type == "breaking":
            self.selected_ball = Breaking_ball_AI(400, 200, 10, 0.0)
            target_index = random.randint(0, len(breaking_strike_targets) - 1)
            self.selected_ball.set_target_position(target_index)
            self.start_pitching = True
            self.pitching_sound.play()
        else:
            self.selected_ball = None
            self.start_pitching = True
            self.pitching_sound.play()

    def handle_event(self, event):
        if event.type == SDL_KEYDOWN and event.key == SDLK_SPACE and not self.start_pitching:
            self.start_pitching = True
            self.pitcher_frame = 0
            self.throw_random_ball()

    def draw(self):
        if self.start_pitching:
            self.pitching_image.clip_draw(self.pitcher_frame * 45, 0, 45, 45,
                                          self.pitcher_x, self.pitcher_y, 100, 100)
            if self.selected_ball:
                self.selected_ball.draw()
        else:
            self.idle_image.clip_draw(self.pitcher_idle_frame * 45, 0, 45, 45,
                                       self.pitcher_x, self.pitcher_y, 100, 100)

    def update(self):
        if self.start_pitching:
            self.pitcher_frame = (self.pitcher_frame + 1) % self.pitcher_frame_count

            if self.pitcher_frame == 0:
                self.start_pitching = False
                if self.selected_ball:
                    self.selected_ball = None

        if self.selected_ball:
            self.selected_ball.update()

        if not self.start_pitching:
            self.pitcher_idle_frame = (self.pitcher_idle_frame + 1) % self.pitcher_idle_frame_count
