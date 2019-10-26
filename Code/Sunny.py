from pico2d import*

class Sunny:

    def __init__(self):
        self.x, self.y = 400, 100
        self.image = load_image('Player_Sunny.png')

    def handle_event(self, event):
        if (event.type == SDL_KEYUP , event.type == SDLK_RIGHT):
            self.x += 10
        elif (event.type == SDL_KEYUP & event.type == SDLK_LEFT):
            self.x -= 10

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)



