__author__ = 'cho'

from pico2d import *

class Background:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return 0, 0, 800, 50

    pass