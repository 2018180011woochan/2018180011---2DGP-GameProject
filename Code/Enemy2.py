from pico2d import*

class Enemy2:
    def __init__(self):
        self.image = load_image('Enemy2.png')
        self.y = 650
        self.dir = 0.15


    def draw(self):
        self.image.draw(400, self.y)

    def update(self):
        self.y -= self.dir