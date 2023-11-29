from pico2d import *

class Batter:
    def __init__(self):
        # 타자 sprite
        self.hitter_left_handed = load_image('resource/hitter_left_handed.png')
        self.hitter_right_handed = load_image('resource/hitter_right_handed.png')
        # 타자 idle sprite
        self.idle_hitter_left_handed = load_image('resource/idle_hitter_left_handed.png')
        self.idle_hitter_right_handed = load_image('resource/idle_hitter_right_handed.png')

        self.running = True

        # 우타자 초기 위치
        self.hitter_right_handed_x = 250  # 초기 x 좌표
        self.hitter_right_handed_y = 130  # 초기 y 좌표

        self.hitter_frame = 0
        self.hitter_idle_frame = 0

        self.hitter_frame_count = 8
        self.hitter_idle_frame_count = 8

        self.hitting_delay = 0.01
        self.hitter_idle_delay = 0.3

        self.start_hitting = False

    def handle_events(self):
        events = get_events()
        for event in events:
            if event.type == SDL_QUIT:
                self.running = False
            # 마우스 좌클릭 시 스윙
            elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
                self.start_hitting = True

    def draw(self):
        if self.start_hitting:
            self.hitter_right_handed.clip_draw(self.hitter_frame * 80, 0, 80, 80,
                self.hitter_right_handed_x, self.hitter_right_handed_y, 385, 250)
        else:
            self.idle_hitter_right_handed.clip_draw(self.hitter_idle_frame * 50, 0, 50, 50,
                        self.hitter_right_handed_x, self.hitter_right_handed_y, 250, 250)

    def update(self):
        if self.start_hitting:
            self.hitter_frame = (self.hitter_frame + 1) % self.hitter_frame_count
            #delay(self.hitting_delay)

            if self.hitter_frame == 0:
                self.start_hitting = False

        # 스윙하지 않을 때는 idle 애니메이션 재생
        if not self.start_hitting:
            self.hitter_idle_frame = (self.hitter_idle_frame + 1) % self.hitter_idle_frame_count
            #delay(self.hitter_idle_delay)
