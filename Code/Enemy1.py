from pico2d import*

class Enemy1:
    def __init__(self):
        self.image = load_image('Enemy1.png')

    def draw(self):
        self.image.draw(270, 500)
        self.image.draw(530, 500)