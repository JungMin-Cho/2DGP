__author__ = 'cho'

from pico2d import *

class Background:
    bgm = None
    def __init__(self):
        self.image = load_image('grass.png')
        #if Background.bgm == None:
        #    Background.bgm = load_music('backbgm.wav')
        #    Background.bgm.set_volume(64)
        #    Background.bgm.repeat_play()


    def draw(self):
        self.image.draw(400, 30)
        self.draw_bb()

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return 0, 0, 800, 50

    pass

