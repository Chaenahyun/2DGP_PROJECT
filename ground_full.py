from pico2d import load_image

class Ground:
    def __init__(self):
        self.image = load_image('ground_full.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(800 // 2, 450 // 2)