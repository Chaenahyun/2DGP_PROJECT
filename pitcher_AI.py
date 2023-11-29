from pico2d import *

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

    def handle_event(self, event):
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_SPACE and not self.start_pitching:
                self.start_pitching = True

    def update(self):
        if self.start_pitching:
            self.frame = (self.frame + 1) % self.pitching_frame_count
            #delay(self.pitching_delay)

            if self.frame == 0:
                self.start_pitching = False
        else:
            self.frame = (self.frame + 1) % self.idle_frame_count
            #delay(self.idle_delay)

    def draw(self):
        if self.start_pitching:
            self.pitching_image.clip_draw(self.frame * 45, 0, 45, 45, self.x, self.y, 100, 100)
        else:
            self.idle_image.clip_draw(self.frame * 45, 0, 45, 45, self.x, self.y, 100, 100)