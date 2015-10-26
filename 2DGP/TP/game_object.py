__author__ = 'cho'
from pico2d import *

class Missile:
    def __init__(self):
        self.image = load_image('Items.png')
    def draw(self):
        self.image.clip_draw(415, 125, 445, 155, 400, 300)

class Monster:
    def __init__(self):
        self.image = load_image('Items.png')