from pico2d import *
import math

class Runner:
    def __init__(self, x, y, speed, frame_count, idle_frame_count, running_delay, running_idle_delay):
        self.x, self.y = x, y
        self.move_arrow_x, self.move_arrow_y = x, y
        self.start_running = False
        self.current_base_index = 0
        self.runner_frame = 0
        self.runner_idle_frame = 0
        self.runner_frame_count = frame_count
        self.runner_idle_frame_count = idle_frame_count
        self.running_delay = running_delay
        self.running_idle_delay = running_idle_delay
        self.speed = speed

        # Load images
        self.running_runner_to_left = load_image('running_runner_left.png')
        self.running_runner_to_right = load_image('running_runner_right.png')
        self.idle_runner = load_image('idle_runner_left.png')

        self.first_base = load_image('base.png')
        self.second_base = load_image('base.png')
        self.third_base = load_image('base.png')
        self.home_base = load_image('home_base.png')

    def move_to_base(self, base_index):
        self.move_arrow_x, self.move_arrow_y = base_positions[base_index]
        self.current_base_index = base_index
        self.start_running = True

    def lerp(self, start, end, t):
        return (1 - t) * start + t * end

    def update(self):
        if self.start_running:
            self.runner_frame = (self.runner_frame + 1) % self.runner_frame_count
            delay(self.running_delay)

            t = (self.runner_frame % self.runner_frame_count) / float(self.runner_frame_count)
            curve_x = self.lerp(self.x, self.move_arrow_x, t)
            curve_y = self.lerp(self.y, self.move_arrow_y, t)

            self.x, self.y = curve_x, curve_y

            if self.runner_frame == self.runner_frame_count - 1:
                self.start_running = False

        if not self.start_running:
            self.runner_idle_frame = (self.runner_idle_frame + 1) % self.runner_idle_frame_count
            delay(self.running_idle_delay)

    def draw(self):
        clear_canvas()

        for base_index, (base_x, base_y) in enumerate(base_positions):
            if base_index == 0:
                self.first_base.draw(base_x, base_y, 15, 15)
            elif base_index == 1:
                self.second_base.draw(base_x, base_y, 15, 15)
            elif base_index == 2:
                self.third_base.draw(base_x, base_y, 15, 15)
            elif base_index == 3:
                self.home_base.draw(base_x, base_y, 15, 15)

        if self.start_running:
            if self.current_base_index in [1, 2]:
                self.running_runner_to_left.clip_draw(self.runner_frame * 45, 0, 45, 45,
                                                 self.x, self.y, 30, 30)
            elif self.current_base_index in [0, 3]:
                self.running_runner_to_right.clip_draw(self.runner_frame * 45, 0, 45, 45,
                                                  self.x, self.y, 30, 30)
        else:
            self.idle_runner.clip_draw(self.runner_idle_frame * 45, 0, 45, 45,
                                  self.x, self.y, 30, 30)


# 베이스 위치
base_positions = [
    (495, 72),  # 1루 베이스
    (398, 122),  # 2루 베이스
    (300, 72),  # 3루 베이스
    (398, 23)  # 홈 베이스
]

# Initialize the Runner object
#runner = Runner(420, 30, 5, 8, 8, 0.1, 0.5)
