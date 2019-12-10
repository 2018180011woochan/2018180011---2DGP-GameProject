from pico2d import*
import game_world
import game_framework
import MainState
import Sunny
import boss_bullet
import time
import EndingState

boss_bullet = []

PIXEL_PER_METER = (10.0 / 1.0)
RUN_SPEED_KMPH = 0.1
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 1500.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True


class Boss:
    image = None
    def __init__(self):
        if Boss.image == None:
            Boss.image = load_image('boss.png')
        self.x = 200
        self.y = 570
        self.dir = 0.15
        self.hp = 200000
        self.isAlive = True
        self.boss_bullet_remaketime = 0
        self.boss_bullets = []
        self.boss_bullet_speed = 2




    def get_bb(self):
        return self.x - 200, self.y - 180, self.x + 200, self.y + 180

    def draw(self):
        self.image.draw(self.x, self.y)
        #draw_rectangle(*self.get_bb())

    def update(self):
        sunny = MainState.get_sunny()

        self.y -= RUN_SPEED_PPS
        if self.y < 500:
            self.y += RUN_SPEED_PPS

        if self.hp <= 0:
            game_world.remove_object(self)

            sunny.kill_score += 1000
            game_framework.quit()

