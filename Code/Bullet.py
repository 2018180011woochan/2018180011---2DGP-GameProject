from pico2d import*
import game_world
import game_world
import game_framework
import Right_White_Dragon
import MainState
import Sunny

PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 0.5
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

class Bullet:
    def __init__(self):
        Sunny = MainState.get_sunny()
        self.image = load_image('Bullet.png')
        self.x = Sunny.x
        self.y = 70
        self.shooting = False
        self.attack = 20
        game_world.add_object(self, 1)

    def __del__(self):
        del self.image

    def get_bb(self):
        return self.x-10, self.y-10, self.x+10, self.y+20



    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())


    def update(self):
        yello_dragon = MainState.get_yello_dragon()
        left_white_dragon = MainState.get_left_white_dragon()
        right_white_dragon = MainState.get_right_white_dragon()
        # self.y = 70
        self.y += RUN_SPEED_PPS
        if self.y > 600:
            game_world.remove_object(self)

        if collide(left_white_dragon, self):
            game_world.remove_object(self)
            left_white_dragon.hp -= 20
        if collide(right_white_dragon, self):
            game_world.remove_object(self)
            right_white_dragon.hp -= 20
#        if collide(yello_dragon, self):
 #           game_world.remove_object(self)
  #          yello_dragon.hp -= 20






