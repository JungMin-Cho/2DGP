__author__ = 'cho'

import random
import time

from pico2d import *

class Character:
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    RUN_SPEED_KMPH = 80.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    print(RUN_SPEED_PPS)
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION

    FRAMES_PER_ACTION = 8
    IDLE_FRAMES_PER_ACTION = 4

    image = None
    hit_sound = None

    LEFT_RUN, RIGHT_RUN, LEFT_STAND, RIGHT_STAND = 0, 1, 2, 3
    LEFT_JUMP, RIGHT_JUMP, FALLING = 0, 1, 3

    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.life_time = 0.0
        self.total_frames = 0.0
        self.xdir = 0
        self.ydir = 0
        self.state = self.RIGHT_STAND
        self.jump = 3
        self.jump_count = 2
        self.current_time = 0

        if Character.image == None:
            Character.image = load_image('animation_sheet.png')
        if Character.hit_sound == None:
            pass
            #Character.hit_sound = load_music('pickup.wav')
            #Character.hit_sound.set_volume(32)

    def handle_event(self, event):
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_LEFT: self.xdir += -1
            elif event.key == SDLK_RIGHT: self.xdir += 1
            elif event.key == SDLK_x:
                if 0 < self.jump_count:
                    self.jump_count -= 1
                    if self.state == Character.RIGHT_STAND or self.state == Character.RIGHT_RUN:
                        self.jump = Character.RIGHT_JUMP
                        self.sate = Character.RIGHT_RUN
                        #self.current_time = 0
                    elif self.state == Character.LEFT_STAND or self.state == Character.LEFT_RUN:
                        self.jump = Character.LEFT_JUMP
                        self.state = Character.LEFT_RUN
                        #self.current_time = 0

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
        self.frame = int(self.total_frames) % 8

        self.x += (self.xdir * distance)
        if self.jump != 3:
            self.ydir = 1
            self.current_time += frame_time
            print("jump frame_time = %f, current_time = %f" % (frame_time,self.current_time))
            if self.current_time > 0.2:
                #self.gun[self.count].initbullet(self.angle, self.state, self.x, self.y)
                self.jump = Character.FALLING
                self.current_time = 0
        else:
            self.ydir = -1
        if self.y <= 75:
            self.y = 75
            self.jump_count = 2
        self.y += (self.ydir * distance)

        if self.xdir == -1: self.state = self.LEFT_RUN
        elif self.xdir == 1: self.state = self.RIGHT_RUN
        elif self.xdir == 0:
            if self.state == self.RIGHT_RUN: self.state = self.RIGHT_STAND
            elif self.state == self.LEFT_RUN: self.state = self.LEFT_STAND

        self.x = clamp(25, self.x, 775)
        self.y = clamp(75, self.y, 775)


    def draw(self):
        self.image.clip_draw(self.frame * 100, self.state * 100, 100, 100, self.x, self.y)
        self.draw_bb()

    def get_bb(self):
        return self.x - 25, self.y - 50, self.x + 25, self.y + 50

    def draw_bb(self):
        draw_rectangle(*self.get_bb())