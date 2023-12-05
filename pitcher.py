from pico2d import *
from fast_ball import Fast_ball, target_positions_strike as fast_strike_targets, target_positions_ball as fast_ball_targets
from breaking_ball import Breaking_ball, target_positions_strike as breaking_strike_targets, target_positions_ball as breaking_ball_targets
from batter_AI import Batter_AI
import random

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

        self.selected_ball = None  # 현재 선택된 공 객체를 저장하는 변수
        self.batter_AI = Batter_AI()  # Batter_AI 객체 생성
        self.hitting_probability = 0.01  # 1%의 확률로 설정

        if not hasattr(self, 'pitching_sound'):
            self.pitching_sound = load_wav('resource_music/pitching.WAV')
            self.pitching_sound.set_volume(100)


    def handle_event(self, event):
        if event.type == SDL_KEYDOWN:
            if event.key in [SDLK_1, SDLK_2, SDLK_3, SDLK_4, SDLK_5, SDLK_6, SDLK_7, SDLK_8, SDLK_9,
                               SDLK_a, SDLK_b, SDLK_c, SDLK_d, SDLK_e, SDLK_f, SDLK_g,
                               SDLK_h] and not self.start_pitching:
                self.start_pitching = True
                self.pitching_sound.play()

                if event.key in [SDLK_1, SDLK_2, SDLK_3, SDLK_4, SDLK_5, SDLK_6, SDLK_7, SDLK_8, SDLK_9]:
                    target_index = int(event.key - SDLK_1)
                    if 0 <= target_index < len(fast_strike_targets) and self.selected_ball:
                        self.selected_ball.set_target_position(fast_strike_targets[target_index])
                        self.start_pitching = True
                        self.pitching_sound.play()
                elif event.key in [SDLK_a, SDLK_b, SDLK_c, SDLK_d, SDLK_e, SDLK_f, SDLK_g, SDLK_h]:
                    target_index = int(event.key - SDLK_a)
                    if 0 <= target_index < len(breaking_strike_targets) and self.selected_ball:
                        self.selected_ball.set_target_position(breaking_strike_targets[target_index])
                        self.start_pitching = True
                        self.pitching_sound.play()

    def draw(self):
        if self.start_pitching:
            self.pitching_image.clip_draw(self.pitcher_frame * 45, 0, 45, 45,
                                          self.pitcher_x, self.pitcher_y, 100, 100)
            if self.selected_ball:
                self.selected_ball.draw()
                self.batter_AI.draw()  # 타자 애니메이션 추가
        else:
            self.idle_image.clip_draw(self.pitcher_idle_frame * 45, 0, 45, 45,
                                       self.pitcher_x, self.pitcher_y, 100, 100)

    def update(self):
        if self.start_pitching:
            self.pitcher_frame = (self.pitcher_frame + 1) % self.pitcher_frame_count
            print(f'start!')
            if self.pitcher_frame == 0:
                self.start_pitching = False
                self.selected_ball = None

                if random.random() < self.hitting_probability:
                    self.batter_AI.start_hitting = True

        else:
            self.pitcher_idle_frame = (self.pitcher_idle_frame + 1) % self.pitcher_idle_frame_count
