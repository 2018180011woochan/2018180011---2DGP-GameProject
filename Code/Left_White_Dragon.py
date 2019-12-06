from pico2d import*
import game_world

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

class Left_White_Dragon:
    image = None
    def __init__(self, y = 650, dir = 0.15):
        self.y = y
        self.x = 80
        self.dir = dir
        self.hp = 100
        if Left_White_Dragon.image == None:
            Left_White_Dragon.image = load_image('Left_White_Dragon.png')


    def get_bb(self):
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50

    def draw(self):
        self.image.draw(self.x, self.y)

        draw_rectangle(*self.get_bb())

    def update(self):
        self.y -= RUN_SPEED_PPS
        if self.hp <= 0:
            game_world.remove_object(self)