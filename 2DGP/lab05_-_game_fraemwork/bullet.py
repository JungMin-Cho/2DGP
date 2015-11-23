__author__ = 'cho'

import random

from math import *
from pico2d import *

class Bullet:

    image = None

    PATTERN_1, PATTERN_2, PATTERN_3, PATTERN_4 = 0, 1, 2, 3

    def __init__(self):
        if Bullet.image == None:
            Bullet.image = load_image('Items.png')
        self.angle = 0
        self.x = 400#random.randint(50,750)
        self.y = 550#random.randint(50,550)
        self.r = 1
        self.count = 0
        self.fall_speed = 0.5
        self.state = 0

    def draw(self):
        self.image.clip_draw(415, 410, 30, 30 , self.x , self.y)
        #self.image.clip_draw(415, 410, 30, 30 ,self.x , self.y)
        self.draw_bb()

    def initbullet(self, angle, state, x, y):
        if state == Bullet.PATTERN_1:
            self.x = x#random.randint(50,750)
            self.y = y#random.randint(50,550)
            self.r = 1
            self.state = state
            self.angle = angle
        elif state == Bullet.PATTERN_2:
            self.x = x#random.randint(50,750)
            self.y = y#random.randint(50,550)
            self.r = 1
            self.state = state
        elif state == Bullet.PATTERN_3:
            self.x = x
            self.y = y
            self.r = 1
            self.state = state
            self.angle = angle
        elif state == Bullet.PATTERN_4:
            self.x = x
            self.y = y
            self.r = 1
            self.state = state
            self.angle = angle
            pass


    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 15, self.y - 15, self.x + 15, self.y + 15

    def update(self, frame_time):
        if self.state == Bullet.PATTERN_1:
            self.r += frame_time * self.fall_speed
            self.x += sin(self.angle)*self.r
            self.y += cos(self.angle)*self.r
        elif self.state == Bullet.PATTERN_2:
            self.r += frame_time * self.fall_speed
            self.y -= self.r
        elif self.state == Bullet.PATTERN_3:
            self.r += frame_time * self.fall_speed
            self.x += sin(self.angle)*self.r
            self.y += cos(self.angle)*self.r
        elif self.state == Bullet.PATTERN_4:
            self.r += frame_time * self.fall_speed
            self.x += sin(self.angle)*self.r
            self.y += cos(self.angle)*self.r
        #print("hihihi")
    pass