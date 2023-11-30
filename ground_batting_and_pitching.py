#ground_batting_and_pitching.py

from pico2d import *

class Ground_batting_and_pitching:
    def __init__(self):
        self.image = load_image('resource/ground_batting_and_pitching.png')

    def draw(self):
        self.image.draw(800 // 2, 450 // 2)

    def update(self):
        pass
