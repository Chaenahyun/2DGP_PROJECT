#ground_batting_and_pitching.py
from pico2d import *

# 캔버스 열기
ground_width, ground_height = 800, 450
open_canvas(ground_width, ground_height)

class Ground_batting_and_pitching:
    def __init__(self):
        self.image = load_image('resource/ground_batting_and_pitching.png')

    def draw(self):
        self.image.draw(800 // 2, 450 // 2)

    def update(self):
        pass
