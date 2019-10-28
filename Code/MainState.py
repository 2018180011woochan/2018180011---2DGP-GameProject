import random
import json
import os

from pico2d import *

import game_framework

from BackGround1 import BackGround1
from Sunny import Sunny
from Enemy1 import Enemy1
from Enemy2 import Enemy2
from Bullet import Bullet


name = "MainState"

sunny = None
background1 = None
enemy1 = None
enemy2 = None
bullet = None


def enter():
    global Sunny, BackGround1, Enemy1, Enemy2, Bullet
    Sunny = Sunny()
    BackGround1 = BackGround1()
    Enemy1 = Enemy1()
    Enemy2 = Enemy2()
    Bullet = Bullet()

def exit():
    global Sunny, BackGround1, Enemy1, Enemy2, Bullet
    del sunny
    del BackGround1
    del Enemy1
    del Enemy2
    del Bullet

def pause():
    pass


def resume():
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            Sunny.handle_event(event)

def update():
    Sunny.update()
    Enemy1.update()
    Enemy2.update()
    Bullet.update()

def draw():
    clear_canvas()
    BackGround1.draw()
    Sunny.draw()
    Bullet.draw()
    Enemy1.draw()
    Enemy2.draw()
    update_canvas()