from pico2d import*
import game_world

class Bullet:
    image = None
    def __init__(self, x = 200, y = 70, dir = 1):
        self.x = x
        self.y = y
        self.dir = dir
        if Bullet.image == None:
            Bullet.image = load_image('Bullet.png')

    def draw(self):
        self.image.draw(self.x, self.y)


    def update(self):
        self.y += self.dir

        if self.y > 600:
            game_world.remove_object(self)