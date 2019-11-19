from pico2d import*

PIXEL_PER_METER = (10.0 / 1.0)
RUN_SPEED_KMPH = 0.3
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

class Yello_Dragon:
    def __init__(self):
        self.image = load_image('Yello_Dragon.png')
        self.y = 650
        self.dir = 0.15


    def draw(self):
        self.image.draw(200, self.y)

    def update(self):
        self.y -= RUN_SPEED_PPS