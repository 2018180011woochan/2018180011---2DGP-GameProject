from pico2d import *
import random
import json
import os
import game_framework

from BackGround1 import BackGround1
from Sunny import Sunny

name = "MainState"

sunny = None
background1 = None

def enter():
    global Sunny, BackGround1
    sunny = Sunny()
    background1 = BackGround1()

def exit():
    global sunny, background1
    del sunny
    del background1

def pause():
    pass


def resume():
    pass

def handle_event():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            sunny.handle_event(event)

def update():
    sunny.update

def draw():
    clear_canvas()
    background1.draw()
    sunny.draw()
    update_canvas()