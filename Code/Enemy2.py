from pico2d import*

class Enemy2:
    def __init__(self):
        self.image = load_image('Enemy2.png')

    def draw(self):
        self.image.draw(400, 500)