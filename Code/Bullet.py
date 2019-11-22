from pico2d import*
import game_world
import game_world
import game_framework
import RIght_White_Dragon
import Sunny

PIXEL_PER_METER = (10.0 / 1.0)
RUN_SPEED_KMPH = 0.5
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

class Bullet:
    image = None
    def __init__(self, x = 200, y = 70, dir = 1):
        self.x = x
        self.y = y
        self.dir = dir
        self.shooting = False
        if Bullet.image == None:
            Bullet.image = load_image('Bullet.png')

    def get_bb(self):
        return self.x-10, self.y-10, self.x+10, self.y+20

    def draw(self):
        if self.shooting == True:
            self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        if self.shooting == False:
            self.x = 200
            self.y = 70
        if self.shooting == True:
            self.y += RUN_SPEED_PPS
            if self.y > 600:
                self.shooting = False
                self.x = 200
                self.y = 70

        #self.y += RUN_SPEED_PPS

        #if self.y > 600:
        #    game_world.remove_object(self)

