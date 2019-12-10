from pico2d import*
import game_world
import game_world
import game_framework
import Right_White_Dragon
import MainState
import Intro_state
import Sunny
import boss

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

class boss_bullet5:
    image = None
    def __init__(self, x):
        boss = MainState.get_boss()
        #self.x = boss.x
        #self.y = boss.y
        self.x = 200
        self.y = 500
        self.attack = 20
        #game_world.add_object(self, 1)
        if boss_bullet5.image == None:
            boss_bullet5.image = load_image('boss_bullet.png')

    def get_bb(self):
        return self.x-10, self.y-10, self.x+10, self.y+10



    def draw(self):
        self.image.draw(self.x, self.y)
        #draw_rectangle(*self.get_bb())


    def update(self):
        self.y -= RUN_SPEED_PPS
        self.x += 0.4

        if self.y < 0:
            boss_bullets5 = MainState.get_boss_bullets5()
            boss_bullets5.remove(self)
            game_world.remove_object(self)

        sunny = MainState.get_sunny()
        if collide(sunny, self):
            delay(1)
            game_framework.change_state(Intro_state)






