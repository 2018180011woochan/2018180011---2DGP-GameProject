from pico2d import*
import game_world
import game_framework
import MainState

PIXEL_PER_METER = (10.0 / 1.0)
RUN_SPEED_KMPH = 0.1
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

class Yello_Dragon:
    image = None
    def __init__(self, x = 200, y = 650, dir = 0.15):
        if Yello_Dragon.image == None:
            Yello_Dragon.image = load_image('Yello_Dragon.png')
        self.x = x
        self.y = y
        self.dir = dir

    def get_bb(self):
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        if get_time() > 5:
            yello_dragon = MainState.get_yello_dragon()
        self.y -= RUN_SPEED_PPS

    def remake_yellodragon(self):
        yello_dragon = Yello_Dragon(self.x, self.y, self.dir)
        game_world.add_object(yello_dragon, 1)