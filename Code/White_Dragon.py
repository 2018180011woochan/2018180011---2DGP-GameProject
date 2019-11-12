from pico2d import*

class White_Dragon:
    image = None
    def __init__(self, y = 650, dir = 0.15):
        self.y = y
        self.dir = dir
        if White_Dragon.image == None:
            White_Dragon.image = load_image('White_Dragon.png')


    def draw(self):
        self.image.draw(80, self.y)
        self.image.draw(320, self.y)

    def update(self):
        self.y -= self.dir