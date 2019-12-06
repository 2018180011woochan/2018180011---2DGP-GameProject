import random
import json
import os


from pico2d import *

import game_framework
import game_world
import Sunny
import Yello_Dragon
import Bullet
import Right_White_Dragon
import EndingState

from BackGround1 import BackGround1
from Sunny import Sunny
from Left_White_Dragon import Left_White_Dragon
from Right_White_Dragon import Right_White_Dragon
from Yello_Dragon import Yello_Dragon
from Bullet import Bullet
#from Yello_Dragon import *


name = "MainState"

sunny = None
background1 = None
left_white_dragon = None
right_white_dragon = None
yello_dragon = None

Bullets = []

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True

def enter():
    global Sunny, BackGround1, Left_White_Dragon, Right_White_Dragon, Yello_Dragon
    Sunny = Sunny()
    BackGround1 = BackGround1()
    Left_White_Dragon = Left_White_Dragon()
    Right_White_Dragon = Right_White_Dragon()
    Yello_Dragon = Yello_Dragon()
    game_world.add_object(BackGround1, 0)
    game_world.add_object(Sunny, 1)
    game_world.add_object(Left_White_Dragon, 2)
    game_world.add_object(Right_White_Dragon, 2)
    game_world.add_object(Yello_Dragon, 3)



def exit():
    global Sunny, BackGround1, Left_White_Dragon, Right_White_Dragon, Yello_Dragon
    del sunny
    del BackGround1
    del Left_White_Dragon
    del Right_White_Dragon
    del Yello_Dragon
    game_world.clear()


def get_yello_dragon():
    return Yello_Dragon

def get_right_white_dragon():
    return Right_White_Dragon

def get_left_white_dragon():
    return Left_White_Dragon

def get_bullet():
    return Bullet

def get_sunny():
    return Sunny

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
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_framework.change_state(EndingState)
        else:
            Sunny.handle_event(event)

def update():
    for game_object in game_world.all_objects():
        game_object.update()
    if Sunny.collide(Yello_Dragon):
        delay(1)
        game_framework.change_state(EndingState)
    if Sunny.collide(Left_White_Dragon):
        delay(1)
        game_framework.change_state(EndingState)
    if Sunny.collide(Right_White_Dragon):
        delay(1)
        game_framework.change_state(EndingState)


    #if collide(Bullet, Yello_Dragon):
    #   game_framework.quit()
    #for Bullet in Bullets:
    #    if collide(Sunny.bullets, Right_White_Dragon):
    #        game_framework.quit()




def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()