import game_framework
import pico2d
from pico2d import*

open_canvas()

Sunny = load_image('Player_Sunny.png')
BackGround = load_image('Stage1_Background.png')

BackGround.draw_now(400, 300)
Sunny.draw_now(400, 100)

delay(100)

close_canvas()


