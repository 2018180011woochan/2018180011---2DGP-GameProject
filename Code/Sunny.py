from pico2d import*
import game_framework
import game_world
from Bullet import Bullet

PIXEL_PER_METER = (10.0 / 1.0)
RUN_SPEED_KMPH = 2.0
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
            if sunny.x > 330:
                sunny.x = 330
        elif event == LEFT_DOWN:
            sunny.velocity -= RUN_SPEED_PPS
            if sunny.x < 0:
                sunny.x = 0
        elif event == RIGHT_UP:
            sunny.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            sunny.velocity += RUN_SPEED_PPS


    @staticmethod
    def exit(sunny, event):
        if event == SPACE:
            sunny.fire_bullet()
        pass

    @staticmethod
    def do(sunny):
        sunny.x += sunny.velocity
        sunny.x = clamp(25, sunny.x, 800 - 25)
        pass

    @staticmethod
    def draw(sunny):
        sunny.image.draw(sunny.x, sunny.y)


class Sunny:

    def __init__(self):
        self.x, self.y = 200, 70
        self.dir = 1
        self.velocity = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)
        self.image = load_image('Player_Sunny.png')

    def fire_bullet(self):
        bullet = Bullet(self.x, self.y, self.dir)
        game_world.add_object(bullet, 1)

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

    def draw(self):
        self.cur_state.draw(self)



