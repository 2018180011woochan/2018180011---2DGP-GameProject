from pico2d import*
import game_world
import game_world
import game_framework
import Right_White_Dragon
import MainState
import Sunny
import boss
import time

frame_time = 0.0

PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 0.5
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 150.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 100.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True

class boss_bullet:
    image = None
    def __init__(self, x):
        boss = MainState.get_boss()
        #self.x = boss.x
        #self.y = boss.y
        self.x = 200
        self.y = 500
        self.attack = 20
        #self.velocity -= RUN_SPEED_PPS
        #game_world.add_object(self, 1)
        if boss_bullet.image == None:
            boss_bullet.image = load_image('boss_bullet.png')

    def get_bb(self):
        return self.x-10, self.y-10, self.x+10, self.y+10



    def draw(self):
        self.image.draw(self.x, self.y)
        #draw_rectangle(*self.get_bb())


    def update(self):
        #self.velocity -= RUN_SPEED_PPS
        #self.y -= self.velocity * game_framework.frame_time
        self.y -= RUN_SPEED_PPS

        if self.y < 0:
            boss_bullets = MainState.get_boss_bullets()
            boss_bullets.remove(self)
            game_world.remove_object(self)

        sunny = MainState.get_sunny()
        if collide(sunny, self):
           game_framework.quit()






