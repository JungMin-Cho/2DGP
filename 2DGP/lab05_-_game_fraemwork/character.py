__author__ = 'cho'

import random
import time

from pico2d import *

class Character:
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    RUN_SPEED_KMPH = 60.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    print(RUN_SPEED_PPS)
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION

    FRAMES_PER_ACTION = 4
    IDLE_FRAMES_PER_ACTION = 4

    image = None
    hit_sound = None

    LEFT_RUN, RIGHT_RUN, LEFT_STAND, RIGHT_STAND = 0, 1, 2, 3
    CHARACTER_FALL, CHARACTER_JUMP, CHARACTER_RUN, CHARACTER_STAND = 0,1,2,3
    LEFT_JUMP, RIGHT_JUMP, FALLING = 0, 1, 3

    def __init__(self):
        self.x, self.y = 400, 90
        self.frame = random.randint(0, 4)
        self.life_time = 0.0
        self.total_frames = 0.0
        self.xdir = 0
        self.ydir = 0
        self.state = self.RIGHT_STAND
        self.jump = 3
        self.jump_count = 1
        self.current_time = 0
        self.stopx = 0
        self.stopy = 0
        self.width = 20
        self.height = 20
        self.composite = 0
        self.firecount = 0
        self.alive = 1
        if Character.image == None:
            Character.image = load_image('boy.png')
        if Character.hit_sound == None:
            pass
            #Character.hit_sound = load_music('pickup.wav')
            #Character.hit_sound.set_volume(32)

    def handle_event(self, event):
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_LEFT:
                self.xdir += -1
                #self.state = Character.CHARACTER_RUN

            elif event.key == SDLK_RIGHT:
                self.xdir += 1
                #self.state = Character.CHARACTER_RUN
            elif event.key == SDLK_x:
                if 0 < self.jump_count:
                    self.jump_count -= 1
                    if self.state == Character.CHARACTER_RUN or self.state == Character.CHARACTER_STAND:
                        self.jump = Character.RIGHT_JUMP
                        self.state = Character.CHARACTER_JUMP
                    #if self.state == Character.RIGHT_STAND or self.state == Character.RIGHT_RUN:
                    #    self.jump = Character.RIGHT_JUMP
                    #    self.sate = Character.CHARACTER_JUMP
                        #self.current_time = 0
                    #elif self.state == Character.LEFT_STAND or self.state == Character.LEFT_RUN:
                    #    self.jump = Character.LEFT_JUMP
                    #    self.state = Character.CHARACTER_JUMP
                    #    #self.current_time = 0

            #elif event.key == SDLK_UP: self.ydir += 1
            #elif event.key == SDLK_DOWN: self.ydir -= 1

        if event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT: self.xdir += 1
            elif event.key == SDLK_RIGHT: self.xdir += -1
            #elif event.key == SDLK_UP: self.ydir -= 1
            #elif event.key == SDLK_DOWN: self.ydir += 1

    def hit(self, bullet):
        self.hit_sound.play()
        pass

    def update(self, frame_time):
        self.life_time += frame_time
        distance = Character.RUN_SPEED_PPS * frame_time
        self.total_frames += Character.FRAMES_PER_ACTION * Character.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 4
        #print("fff ",self.stopx)

        self.x += (self.xdir * distance)
        if self.jump != 3:
            self.ydir = 1
            self.current_time += frame_time
            if self.current_time > 0.2:
                self.jump = Character.FALLING
                self.state = Character.CHARACTER_FALL
                self.current_time = 0
        else:
            self.ydir = -1

        if self.stopy == 1:
            self.jump_count = 2
            self.state = Character.CHARACTER_STAND

        self.y += (self.ydir * distance)
        #print("sss %d : %d"%(self.jump_count, self.stopy))
        if self.state == Character.CHARACTER_FALL or Character.CHARACTER_JUMP:
            pass
        elif self.xdir == -1: self.state = Character.CHARACTER_RUN
        elif self.xdir == 1: self.state = Character.CHARACTER_RUN
        elif self.xdir == 0:
            self.state = self.CHARACTER_STAND
            #if self.state == self.RIGHT_RUN:
            #    self.state = self.RIGHT_STAND
            #    print("xdir == 0")
            #elif self.state == self.LEFT_RUN:
            #    self.state = self.LEFT_STAND
            #    print("xdir == 1")

        if self.xdir == -1:
            self.composite = 1
        elif self.xdir == 1:
            self.composite = 0

        if self.state == Character.CHARACTER_JUMP or self.state == Character.CHARACTER_FALL:
            #print("FALL")
            pass
        elif self.xdir == 0:
            #print("HERE")
            self.state = 3
        elif self.xdir != 0:#self.state == self.CHARACTER_RUN:# or self.state == self.RIGHT_RUN:
            #print("RUN")
            self.state = 2
        elif self.state == self.CHARACTER_STAND:# or self.state == self.LEFT_STAND:
            self.sate = 3

        self.x = clamp(25, self.x, 775)
        self.y = clamp(70, self.y, 575)
        self.stopx = 0
        self.stopy = 0



    def draw(self):
        #self.image.clip_draw(self.frame * 25, self.state * 25, 25, 25, self.x, self.y, self.width * 2, self.height * 2)
        #self.image.clip_draw(self.frame * 30, self.state * 30, 30, 30, self.x, self.y, self.width * 2, self.height * 2)
        if self.composite == 0:
            self.image.clip_draw(self.frame * 30, self.state * 30, 30, 30, self.x, self.y, self.width * 2, self.height * 2)
            pass
        elif self.composite == 1:
            #print("ddddddddddddddddd")
            self.image.clip_composite_draw(self.frame * 30, self.state * 30, 30, 30, 0,'h', self.x, self.y, self.width * 2, self.height * 2)
            pass
        self.draw_bb()

    def get_bb(self):
        return self.x - self.width, self.y - self.height, self.x + self.width, self.y + self.height

    def draw_bb(self):
        draw_rectangle(*self.get_bb())