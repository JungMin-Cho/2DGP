__author__ = 'cho'

from pico2d import *
from bullet import Bullet
import random

import time

class Monster:

    PATTERN_1, PATTERN_2, PATTERN_3, PATTERN_4, MOVE_LEFT,MOVE_RIGHT, MONSTER_DOWN, MONSTER_UP = 0, 1, 2, 3, 4, 5, 6, 7

    def __init__(self):
        self.image = load_image('K.RoolMobile.png')
        self.x = 400
        self.y = 550
        self.gun = [Bullet() for i in range(110)]
        self.count = 0
        self.angle = 3.14#1.57
        self.increase = 0.1
        self.state = 0
        self.speed = 1
        self.xdir = 1
        self.ydir = 1
        self.current_time = 0
        self.bullet_ex_count = 0
        self.max = 109
        self.hp = 40

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

    def getbulletex(self):
        for guns in self.gun:
            if guns.ex == 0:
                self.bullet_ex_count += 1
        if self.state == 0:
            self.max = 109
        elif self.state == 1:
            self.max = 106
        elif self.state == 2:
            self.max = 100
        elif self.state == 3:
            self.max = 110
        #print(self.bullet_ex_count)

    def update(self, frame_time):
        #print(self.bullet_ex_count)
        self.bullet_ex_count = 0
        self.getbulletex()
        if self.state == Monster.MONSTER_DOWN:
            if 380 < self.x and self.x < 420:
                self.xdir = 0
                self.x = 400
            else:
                if self.x <420:
                    self.xdir = 1
                elif 420 < self.x:
                    self.xdir = -1

            if 220 < self.y and self.y < 270:
                self.ydir = 0
                self.y = 260
            else:
                self.ydir = -1


            if self.ydir == 0 and self.xdir == 0:
                self.current_time += frame_time
            self.x += self.xdir * self.speed
            self.y += self.ydir * self.speed
            #print(self.current_time)
            if 4 < self.current_time:
                self.state = Monster.MONSTER_UP
                self.current_time = 0
                #self.state += 1
                #print('count: ', self.count)
                #print(self.state)
                #print(self.bullet_ex_count)
                #for guns in self.gun:
                #    guns.initbullet(0, 0, 0, 0)
                ##self.initbullet(0,0,0,0)
                #self.count = 0
                #self.state += 1
                #if Monster.PATTERN_4 < self.state:
                #    self.state = Monster.PATTERN_1
            pass
        elif self.state == Monster.MONSTER_UP:
            #print("hihi")
            if 510 < self.y and self.y < 590:
                self.ydir = 0
                self.y = 550
                self.current_time += frame_time
            else:
                self.ydir = 1


            #if self.ydir == 0 and self.xdir == 0:

            #self.x += self.xdir * self.speed
            self.y += self.ydir * self.speed
            #print(self.current_time)
            if 1 < self.current_time:
                self.current_time = 0
                #self.state = Monster.MONSTER_UP
                self.state = random.randint(0, 3)
                print('count: ', self.count)
                print(self.state)
                print(self.bullet_ex_count)
                for guns in self.gun:
                    guns.initbullet(0, 0, 0, 0)
                ##self.initbullet(0,0,0,0)
                self.count = 0
                #self.state += 1
                if Monster.PATTERN_4 == self.state or Monster.PATTERN_2 == self.state:
                    self.xdir = 1
            pass

        elif self.bullet_ex_count < self.max:
            #print(self.bullet_ex_count)
        #if self.count < 100:
            if self.state == Monster.MOVE_RIGHT:
                pass
            elif self.state == Monster.PATTERN_1:
                self.current_time += frame_time
            #print("1 frame_time = %f, current_time = %f" % (frame_time,self.current_time))
                if self.current_time > 0.08:
                    self.gun[self.count].initbullet(self.angle, self.state, self.x, self.y)
                    if 4.71 < self.angle :
                        self.increase = -0.2
                    elif self.angle < 1.57:
                        self.increase = 0.2
                    self.angle += self.increase
                    self.current_time = 0
                    if 108 < self.count:
                        pass
                    else:
                        self.count += 1
                pass

            elif self.state == Monster.PATTERN_2:
            #current_time = time.clock()
                self.current_time += frame_time
            #print("2 frame_time = %f, current_time = %f" % (frame_time,self.current_time))
                if self.current_time > 0.2:
                    #print("time")
                    self.gun[self.count].initbullet(self.angle, self.state, self.x, self.y)
                    self.current_time = 0
                    if 108 < self.count:
                        pass
                    else:
                        self.count += 1
                self.x += self.xdir * self.speed
                if self.x - 40 < 0:
                    self.xdir = 1
                elif 800 < self.x + 40:
                    self.xdir = -1

            elif self.state == Monster.PATTERN_3:
                self.current_time += frame_time
            #print("3 frame_time = %f, current_time = %f" % (frame_time,self.current_time))
                if self.current_time > 0.2:
                    self.current_time = 0
                    if 80 < self.count:
                        pass
                    else:
                        for i in range(self.count, self.count + 20):
                            if 4.71 < self.angle :
                                self.increase = -0.157
                            elif self.angle < 1.57:
                                self.increase = 0.157
                            self.angle += self.increase
                            self.gun[i].initbullet(self.angle, self.state, self.x, self.y)
                        self.count += 20
            elif self.state == Monster.PATTERN_4:
                self.current_time += frame_time
            #print("3 frame_time = %f, current_time = %f" % (frame_time,self.current_time))
                if self.current_time > 0.2:
                    self.current_time = 0
                    if 100 < self.count:
                        pass
                    else:
                        for i in range(self.count, self.count + 10):
                            if 4.71 < self.angle :
                                self.increase = -0.314
                            elif self.angle < 1.57:
                                self.increase = 0.314
                            self.angle += self.increase
                            self.gun[i].initbullet(self.angle, self.state, self.x, self.y)
                        self.count += 10
                self.x += self.xdir * self.speed
                if self.x - 40 < 0:
                    self.xdir = 1
                elif 800 < self.x + 40:
                    self.xdir = -1
                pass
        else:
            self.state = Monster.MONSTER_DOWN
            #print('count: ', self.count)
            #print(self.state)
            #print(self.bullet_ex_count)
            #for guns in self.gun:
            #    guns.initbullet(0, 0, 0, 0)
            ##self.initbullet(0,0,0,0)
            #self.count = 0
            #self.state += 1
            #if Monster.PATTERN_4 < self.state:
            #    self.state = Monster.PATTERN_1
        ####
        for i in range(self.count):
            self.gun[i].update(frame_time)

        #for bullet in self.gun:
        #    bullet.update(frame_time)


    def draw(self):
        for i in range(self.count):
            self.gun[i].draw()
        self.image.clip_draw(300, 330, 80, 80, self.x , self.y)
        self.draw_bb()

    def initbullet(self):
        self.count = 0
        self.angle = 3.14
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
            elif self.state == Monster.PATTERN_3:
                for bullet in self.gun:
                    self.angle += 0.314
                    bullet.initbullet(self.angle, self.state, self.x, self.y)
            elif self.state == Monster.PATTERN_4:
                for bullet in self.gun:
                    self.angle += 0.314
                    bullet.initbullet(self.angle, self.state, self.x, self.y)



        print("init")
        #self.count = 0

    def get_bb(self):
        return self.x - 40, self.y - 40, self.x + 40, self.y + 40

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def init(self):
        pass