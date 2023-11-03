from pico2d import *

class map:
    def __init__(self):
        self.image = load_image('map.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(1600, 900)



