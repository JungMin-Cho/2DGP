__author__ = 'cho'

import random

from math import *
from pico2d import *

class Bullet:

    image = None
    hit_sound = None

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
        self.ex = 1
        self.hit = 0
        if Bullet.hit_sound == None:
            pass
            #Bullet.hit_sound = load_music('scream.wav')
            #Bullet.hit_sound.set_volume(32)

    def draw(self):
        if self.hit == 1:
            pass
        else:
            self.image.clip_draw(415, 410, 30, 30 , self.x , self.y)
            #self.image.clip_draw(415, 410, 30, 30 ,self.x , self.y)
            self.draw_bb()
    def hits(self, bullet):
        self.hit_sound.play()
        pass

    def initbullet(self, angle, state, x, y):
        self.hit = 0
        self.ex = 1
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
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

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
        if self.x < 0 or 800 < self.x or self.y < 0 or 600 < self.y:
            self.ex = 0
        #print("hihihi")
    pass