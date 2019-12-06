from pico2d import*
import game_framework
import game_world
from Bullet import Bullet
from Yello_Dragon import Yello_Dragon

Bullets = []

PIXEL_PER_METER = (10.0 / 1.0)
RUN_SPEED_KMPH = 100.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SPACE = range(5)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE
}


class IdleState:
    @staticmethod
    def enter(sunny, event):
        if event == RIGHT_DOWN:
            sunny.velocity += RUN_SPEED_PPS
            Bullet.shooting = True
            if sunny.x > 330:
                sunny.x = 330
        elif event == LEFT_DOWN:
            Bullet.shooting = True
            sunny.velocity -= RUN_SPEED_PPS
            if sunny.x < 0:
                sunny.x = 0
        elif event == RIGHT_UP:
            Bullet.shooting = True
            sunny.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            Bullet.shooting = True
            sunny.velocity += RUN_SPEED_PPS
        sunny.dir = clamp(-1, sunny.velocity, 1)

    @staticmethod
    def exit(sunny, event):
        pass

    @staticmethod
    def do(sunny):
        sunny.fly_distance = get_time() * 100
        sunny.x += sunny.velocity * game_framework.frame_time
        sunny.x = clamp(25, sunny.x, 800 - 25)
        sunny.bullet_remaketime += game_framework.frame_time * 10

        if int(sunny.bullet_remaketime) >= 3 - sunny.bullet_speed * 0.8:
            sunny.fire_bullet()
            sunny.bullet_remaketime = 0

        pass

    @staticmethod
    def draw(sunny):
        sunny.image.draw(sunny.x, sunny.y)
        sunny.font.draw(game_world.WIDTH * 0.7, game_world.HEIGHT - 50,
                      '%10.0f M' % (sunny.fly_distance - (sunny.fly_distance % 10)), (255, 255, 255))
        sunny.font.draw(game_world.WIDTH * -0.5, game_world.HEIGHT - 50,
                        '%10.0f' % (sunny.kill_score - (sunny.kill_score % 10)), (255, 255, 255))


class Sunny:

    def __init__(self):
        self.x, self.y = 200, 70
        self.dir = 1
        self.velocity = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)
        self.image = load_image('Player_Sunny.png')
        self.bullet_remaketime = 0
        self.bullets = []
        self.bullet_speed = 2
        self.fly_distance = 0
        self.kill_score = 0
        self.font = load_font('ENCR10B.TTF', 30)
        self.final_score = self.fly_distance + self.kill_score


    def update_state(self):
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state.enter(self, event)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state.enter(self, event)
        pass

    def get_bb(self):
        return self.x-20, self.y-20, self.x+20, self.y+20


    def draw(self):
        self.cur_state.draw(self)
        draw_rectangle(*self.get_bb())

    def fire_bullet(self):
        self.bullets += [Bullet()]


    def collide(self, a):
        left_a, bottom_a, right_a, top_a = a.get_bb()
        left_b, bottom_b, right_b, top_b = self.get_bb()
        if left_a > right_b: return False
        if right_a < left_b: return False
        if top_a < bottom_b: return False
        if bottom_a > top_b: return False
        return True




