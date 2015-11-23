__author__ = 'cho'

from pico2d import *
from bullet import Bullet

import time

class Monster:

    PATTERN_1, PATTERN_2, PATTERN_3, PATTERN_4, MOVE_LEFT,MOVE_RIGHT = 0, 1, 2, 3, 4, 5

    def __init__(self):
        self.image = load_image('K. Rool Mobile.png')
        self.x = 400
        self.y = 550
        self.gun = [Bullet() for i in range(110)]
        self.count = 0
        self.angle = 1.57
        self.increase = 0.1
        self.state = 0
        self.speed = 1
        self.xdir = 1
        self.ydir = 1
        self.current_time = 0

        for bullet in self.gun:
            if self.state == Monster.PATTERN_1:
                if 4.71 < self.angle :
                    self.increase = -0.1
                elif self.angle < 1.57:
                    self.increase = 0.1
                self.angle += self.increase
                bullet.initbullet(self.angle, self.state, self.x, self.y)
            elif self.state == Monster.PATTERN_2:
                for bullet in self.gun:
                    bullet.initbullet(self.angle, self.state, self.x, self.y)

        #self.count = 0

    def update(self, frame_time):
        if self.state == Monster.PATTERN_4:
            for i in range(self.count):
                self.gun[i].update(frame_time)
            if 109 < self.count:
                pass
            else:
                self.count += 1
        elif self.state == Monster.PATTERN_1:
            if 4.71 < self.angle :
                    self.increase = -0.1
            elif self.angle < 1.57:
                self.increase = 0.1
            self.angle += self.increase
            pass
        elif self.state == Monster.PATTERN_2:
            self.x += self.xdir * self.speed
            if self.x - 40 < 0:
                self.xdir = 1
            elif 800 < self.x + 40:
                self.xdir = -1
        #current_time = time.clock()
        self.current_time += frame_time
        print("frame_time = %f, current_time = %f" % (frame_time,self.current_time))
        if self.current_time > 0.5:
            print("time")
            self.gun[self.count].initbullet(self.angle, self.state, self.x, self.y)
            self.current_time = 0
            if 108 < self.count:
                pass
            else:
                self.count += 1
        for i in range(self.count):
            self.gun[i].update(frame_time)

        #for bullet in self.gun:
        #    bullet.update(frame_time)


    def draw(self):
        self.image.clip_draw(300, 330, 80, 80, self.x , self.y)
        self.draw_bb()
        for bullet in self.gun:
            bullet.draw()

    def initbullet(self):
        self.count = 0
        self.angle = 1.57
        self.increase = 0.1

        for bullet in self.gun:
            if self.state == Monster.PATTERN_1:
                if 4.71 < self.angle :
                    self.increase = -0.1
                elif self.angle < 1.57:
                    self.increase = 0.1
                self.angle += self.increase
                bullet.initbullet(self.angle, self.state, self.x, self.y)
            elif self.state == Monster.PATTERN_2:
                for bullet in self.gun:
                    bullet.initbullet(self.angle, self.state, self.x, self.y)
        print("init")
        #self.count = 0

    def get_bb(self):
        return self.x - 40, self.y - 40, self.x + 40, self.y + 40

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def init(self):
        pass