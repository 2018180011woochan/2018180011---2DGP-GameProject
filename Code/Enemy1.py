from pico2d import*

class Enemy1:
    def __init__(self):
        self.y = 650
        self.dir = 0.15
        self.image = load_image('Enemy1.png')

    def draw(self):
        self.image.draw(270, self.y)
        self.image.draw(530, self.y)

    def update(self):
        self.y -= self.dir