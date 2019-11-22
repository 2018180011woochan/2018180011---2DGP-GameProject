from pico2d import*
import game_world
import game_framework

PIXEL_PER_METER = (10.0 / 1.0)
RUN_SPEED_KMPH = 0.1
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

class Yello_Dragon:
    image = None
    def __init__(self):
        if Yello_Dragon.image == None:
            Yello_Dragon.image = load_image('Yello_Dragon.png')
        self.x = 200
        self.y = 650
        self.dir = 0.15

    def get_bb(self):
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.y -= RUN_SPEED_PPS