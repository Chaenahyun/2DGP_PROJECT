from pico2d import *
import math

class Runner:
    def __init__(self, x, y, speed, frame_count, idle_frame_count, running_delay, running_idle_delay):
        self.x, self.y = 492, 72
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
        self.running_runner_to_left = load_image('resource/running_runner_left.png')
        self.running_runner_to_right = load_image('resource/running_runner_right.png')
        self.idle_runner = load_image('resource/idle_runner_left.png')


    def update(self):
        if self.start_running:
            self.runner_frame = (self.runner_frame + 1) % self.runner_frame_count
            delay(self.running_delay)

        if not self.start_running:
            self.runner_idle_frame = (self.runner_idle_frame + 1) % self.runner_idle_frame_count
            delay(self.running_idle_delay)

    def draw(self):
        clear_canvas()

        if self.start_running:
            self.idle_runner.clip_draw(self.runner_idle_frame * 45, 0, 45, 45,
                                  self.x, self.y, 30, 30)

