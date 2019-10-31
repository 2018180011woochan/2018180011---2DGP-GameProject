from pico2d import*

class BackGround1:
    def __init__(self):
        self.image = load_image('Stage1_Background.png')

    def draw(self):
        self.image.draw(193, 256)

    def update(self):
        pass