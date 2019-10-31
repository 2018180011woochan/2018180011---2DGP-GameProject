import random
import json
import os


from pico2d import *

import game_framework
import game_world

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
    game_world.add_object(BackGround1, 0)
    game_world.add_object(Sunny, 1)
    game_world.add_object(Enemy1, 2)
    game_world.add_object(Enemy2, 3)
    game_world.add_object(Bullet, 4)

def exit():
    global Sunny, BackGround1, Enemy1, Enemy2, Bullet
    del sunny
    del BackGround1
    del Enemy1
    del Enemy2
    del Bullet
    game_world.clear()

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
    for game_object in game_world.all_objects():
        game_object.update()
    update_canvas()

def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()