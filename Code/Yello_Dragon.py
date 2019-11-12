from pico2d import*

class Yello_Dragon:
    def __init__(self):
        self.image = load_image('Yello_Dragon.png')
        self.y = 650
        self.dir = 0.15


    def draw(self):
        self.image.draw(200, self.y)

    def update(self):
        self.y -= self.dir