import random
import json
import os


from pico2d import *

import game_framework
import game_world
import Sunny
import Yello_Dragon
import Bullet
import boss_bullet
import Right_White_Dragon
import EndingState
import time
import threading

from BackGround1 import BackGround1
from Sunny import Sunny
from Left_White_Dragon import Left_White_Dragon
from Right_White_Dragon import Right_White_Dragon
from Yello_Dragon import Yello_Dragon
from Bullet import Bullet
from boss import Boss
from rubee import Rubee
from boss_bullet import boss_bullet
#from Yello_Dragon import *


name = "MainState"

sunny = None
background1 = None
boss = None
rubee = None

boss_bullets = []
Bullets = []
yello_dragons = []
left_white_dragon = []
right_white_dragon = []
#rubees = []

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True

def enter():
    global Sunny, BackGround1, boss
    #global Yello_Dragon
    global rubee
    rubee = Rubee()
    Sunny = Sunny()
    BackGround1 = BackGround1()
    boss = Boss()
    #Left_White_Dragon = Left_White_Dragon()
    #Right_White_Dragon = Right_White_Dragon()
    #Yello_Dragon = Yello_Dragon()
    game_world.add_object(BackGround1, 0)
    game_world.add_object(Sunny, 1)

    #game_world.add_object(boss, 1)
    #game_world.add_object(Left_White_Dragon, 2)
    #game_world.add_object(Right_White_Dragon, 2)
    #game_world.add_object(Yello_Dragon, 3)

    #global rubees
    #rubees = [Rubee(i) for i in range(5)]
    #game_world.add_objects(rubees, 1)

    global yello_dragons
    yello_dragons = [Yello_Dragon(i) for i in range(5)]
    game_world.add_objects(yello_dragons, 1)

    global left_white_dragons
    left_white_dragons = [Left_White_Dragon(i) for i in range(5)]
    game_world.add_objects(left_white_dragons, 1)

    global right_white_dragons
    right_white_dragons = [Right_White_Dragon(i) for i in range(5)]
    game_world.add_objects(right_white_dragons, 1)

    #global boss_bullets
    #boss_bullets = [boss_bullet(i) for i in range(5)]
    #game_world.add_objects(boss_bullets, 1)



def exit():
    global Sunny, BackGround1, Left_White_Dragon, Right_White_Dragon, Yello_Dragon
    del sunny
    del BackGround1
    del Left_White_Dragon
    del Right_White_Dragon
    del Yello_Dragon
    game_world.clear()

def get_rubee():
    return rubee

def get_boss():
    return boss

def get_boss_bullets():
    return boss_bullets

def get_yello_dragons():
    return yello_dragons

def get_right_white_dragons():
    return right_white_dragons

def get_left_white_dragons():
    return left_white_dragons

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

    current_time = time.time()
    for game_object in game_world.all_objects():
        game_object.update()
    #if Sunny.collide(Yello_Dragon):
     #   delay(1)
      #  game_framework.change_state(EndingState)
    #if Sunny.collide(Left_White_Dragon):
     #   delay(1)
      #  game_framework.change_state(EndingState)
   # if Sunny.collide(Right_White_Dragon):
    #    delay(1)
     #   game_framework.change_state(EndingState)



    global yello_dragons
    sunny = get_sunny()
    if len(yello_dragons) <= 0 and sunny.kill_score < 18000:
        yello_dragons = [Yello_Dragon(i) for i in range(5)]
        game_world.add_objects(yello_dragons, 1)

    global left_white_dragons
    sunny = get_sunny()
    if len(left_white_dragons) <= 0 and sunny.kill_score < 18000:
        left_white_dragons = [Left_White_Dragon(i) for i in range(5)]
        game_world.add_objects(left_white_dragons, 1)

    global right_white_dragons
    sunny = get_sunny()
    if len(right_white_dragons) <= 0 and sunny.kill_score < 18000:
        right_white_dragons = [Right_White_Dragon(i) for i in range(5)]
        game_world.add_objects(right_white_dragons, 1)




    if sunny.kill_score > 18000:
        game_world.add_object(boss, 1)
        global boss_bullets
        if len(boss_bullets) <= 0:
            boss_bullets = [boss_bullet(i) for i in range(5)]
            game_world.add_objects(boss_bullets, 1)

    #if Yello_Dragon.isAlive == False:
    #    game_world.add_object(yello_dragon, 1)
    #threading.Timer(3, yello_dragon).game_world.add_object(yello_dragon, 1)


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