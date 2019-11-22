from pico2d import*

PIXEL_PER_METER = (10.0 / 1.0)
RUN_SPEED_KMPH = 0.1
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

class Right_White_Dragon:
    image = None
    def __init__(self, y = 650, dir = 0.15):
        self.y = y
        self.x = 320
        self.dir = dir
        if Right_White_Dragon.image == None:
            Right_White_Dragon.image = load_image('Right_White_Dragon.png')


    def get_bb(self):
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.y -= RUN_SPEED_PPS