from pico2d import *

class Batter:
    def __init__(self):

        self.batter_left_handed = load_image('resource/batter_left_handed.png')
        self.batter_right_handed = load_image('resource/batter_right_handed.png')

        self.idle_batter_left_handed = load_image('resource/idle_batter_left_handed.png')
        self.idle_batter_right_handed = load_image('resource/idle_batter_right_handed.png')

        self.batter_right_handed_x, self.batter_right_handed_y = 250, 130
        self.batter_left_handed_x, self.batter_left_handed_y = 550, 130

        self.batter_frame = 0
        self.batter_idle_frame = 0

        self.batter_frame_count = 8
        self.batter_idle_frame_count = 8

        self.running = True
        self.start_batting = False

        if not hasattr(self, 'batting_sound'):
            self.batting_sound = load_wav('resource_music/miss.WAV')
            self.batting_sound.set_volume(100)


    def handle_events(self):
        events = get_events()
        for event in events:
            if event.type == SDL_QUIT:
                self.start_batting = False
            elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
                self.start_batting = True

    def draw(self):
        if self.start_batting:
            self.batter_right_handed.clip_draw(self.batter_frame * 80, 0, 80, 80,
                self.batter_right_handed_x, self.batter_right_handed_y, 385, 250)
        else:
            self.idle_batter_right_handed.clip_draw(self.batter_idle_frame * 50, 0, 50, 50,
                        self.batter_right_handed_x, self.batter_right_handed_y, 250, 250)

    def update(self):
        if self.start_batting:
            self.batter_frame = (self.batter_frame + 1) % self.batter_frame_count

            if self.batter_frame == 0:
                self.start_batting = False

        if not self.start_batting:
            self.batter_idle_frame = (self.batter_idle_frame + 1) % self.batter_idle_frame_count
