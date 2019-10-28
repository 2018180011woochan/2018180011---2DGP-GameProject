from pico2d import*
import random
from Sunny import Sunny

class Bullet:
    def __init__(self):
        self.x = 400
        self.y = 100
        self.dir = 1
        self.image = load_image('Bullet.png')

    def draw(self):
        self.image.draw(self.x, self.y)


    def update(self):
        self.y += self.dir