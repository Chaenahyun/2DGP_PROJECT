#ground_full.py
from pico2d import *

class Ground_full:
    def __init__(self):
        self.image = load_image('resource/ground_full.png')

    def draw(self):
        self.image.draw(800 // 2, 450 // 2)

    def update(self):
        pass
