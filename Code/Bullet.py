from pico2d import*
import game_world
import game_world
import game_framework
import RIght_White_Dragon
import MainState
import Sunny

PIXEL_PER_METER = (10.0 / 1.0)
RUN_SPEED_KMPH = 0.5
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

class Bullet:
    def __init__(self):
        Sunny = MainState.get_sunny()
        self.image = load_image('Bullet.png')
        self.x = Sunny.x
        self.y = 70
        self.shooting = False
        game_world.add_object(self, 1)

    def __del__(self):
        del self.image

    def get_bb(self):
        return self.x-10, self.y-10, self.x+10, self.y+20

    def update(self):
        #self.y = 70
        self.y += RUN_SPEED_PPS
        if self.y > 600:
            game_world.remove_object(self)


    def draw(self):
        self.image.draw(self.x, self.y)

    def draw_bb(self):
        if self.shooting == True:
            draw_rectangle(*self.get_bb())



