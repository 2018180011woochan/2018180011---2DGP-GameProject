import random
import json
import os

from pico2d import *

import game_framework

from BackGround1 import BackGround1
from Sunny import Sunny

name = "MainState"

sunny = None
background1 = None



def enter():
    global Sunny, BackGround1
    Sunny = Sunny()
    BackGround1 = BackGround1()

def exit():
    global Sunny, BackGround1
    del sunny
    del BackGround1

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
    Sunny.update

def draw():
    clear_canvas()
    BackGround1.draw()
    Sunny.draw()
    update_canvas()