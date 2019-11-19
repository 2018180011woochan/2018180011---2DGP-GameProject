from pico2d import*
import game_world

PIXEL_PER_METER = (10.0 / 1.0)
RUN_SPEED_KMPH = 5.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

class Bullet:
    image = None
    def __init__(self, x = 200, y = 70, dir = 1):
        self.x = x
        self.y = y
        self.dir = dir
        if Bullet.image == None:
            Bullet.image = load_image('Bullet.png')

    def draw(self):
        self.image.draw(self.x, self.y)


    def update(self):
        self.y += RUN_SPEED_PPS

        if self.y > 600:
            game_world.remove_object(self)