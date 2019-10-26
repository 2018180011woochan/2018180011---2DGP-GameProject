from pico2d import*


class Sunny:

    def __init__(self):
        self.x, self.y = 400, 100
        self.dir = 1
        self.velocity = 0
        self.event_que = []
        self.image = load_image('Player_Sunny.png')

    def handle_event(self, event):
        if event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
            self.x += 10
        elif event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
            self.x -= 10
        if self.x > 570:
            self.x -= 10
        elif self.x < 230:
            self.x += 10

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)



