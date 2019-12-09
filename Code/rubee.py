from pico2d import*
import game_world
import game_framework
import MainState
import EndingState
import Sunny
import time
import Yello_Dragon


PIXEL_PER_METER = (10.0 / 1.0)
RUN_SPEED_KMPH = 0.1
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True

class Rubee:
    image = None
    def __init__(self):
        if Rubee.image == None:
            Rubee.image = load_image('rubee.png')
        yello_dragons = MainState.get_yello_dragons()
        self.x = 0
        self.y = 0





    def get_bb(self):
        return self.x - 5, self.y - 5, self.x + 5, self.y + 5

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        sunny = MainState.get_sunny()
        self.y -= RUN_SPEED_PPS

        if self.y < 0:
            rubee = MainState.get_rubee()
            game_world.remove_object(self)

        if collide(self, sunny):
            #sunny = MainState.get_sunny()
            sunny.kill_score += 1

    #def remake_yellodragon(self):
     #   self.yellodragons += [Yello_Dragon()]

    def collide(self, a):
        left_a, bottom_a, right_a, top_a = a.get_bb()
        left_b, bottom_b, right_b, top_b = self.get_bb()

        if left_a > right_b: return False
        if right_a < left_b: return False
        if top_a < bottom_b: return False
        if bottom_a > top_b: return False
        return True