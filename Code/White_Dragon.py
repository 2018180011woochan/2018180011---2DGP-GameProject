from pico2d import*

PIXEL_PER_METER = (10.0 / 1.0)
RUN_SPEED_KMPH = 0.1
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

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
        self.y -= RUN_SPEED_PPS