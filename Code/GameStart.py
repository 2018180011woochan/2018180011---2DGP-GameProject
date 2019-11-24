import game_framework
import pico2d
import MainState
import Intro_state
import EndingState

pico2d.open_canvas(384, 512)
game_framework.run(Intro_state)
pico2d.close_canvas()


