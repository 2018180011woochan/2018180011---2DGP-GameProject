from pico2d import*

class BackGround1:
    def __init__(self):
        self.image = load_image('Stage1_Background.png')
        self.bgm = load_music('main_bgm.mp3')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()

    def draw(self):
        self.image.draw(193, 256)

    def update(self):
        pass