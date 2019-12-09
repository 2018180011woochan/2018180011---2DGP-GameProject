from pico2d import*
import game_world
import game_framework
import MainState
import EndingState
import Sunny
import time


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

class Yello_Dragon:
    image = None
    def __init__(self, x):
        if Yello_Dragon.image == None:
            Yello_Dragon.image = load_image('Yello_Dragon.png')
        self.x = 200
        self.y = 570
        self.dir = 0.15
        self.hp = 100
        self.isAlive = True




    def get_bb(self):
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        sunny = MainState.get_sunny()
        self.y -= RUN_SPEED_PPS

        if self.y < 0:
            yello_dragons = MainState.get_yello_dragons()
            yello_dragons.remove(self)
            game_world.remove_object(self)
            self.isAlive = False
        if self.hp <= 0:
            yello_dragons = MainState.get_yello_dragons()
            yello_dragons.remove(self)
            game_world.remove_object(self)
            sunny.kill_score += 100
            self.isAlive = False
        if collide(self, sunny):
            delay(1)
            game_framework.change_state(EndingState)

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