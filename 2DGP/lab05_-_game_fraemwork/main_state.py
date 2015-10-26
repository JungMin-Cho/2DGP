import random

import json
import os

from pico2d import *
from math import *

import game_framework
import title_state


name = "MainState"

boy = None
grass = None
font = None

missile = None
monster = None

test = 0

num = 1

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)



class Boy:
    image = None
    hold_image = None
    LEFT_RUN, RIGHT_RUN, LEFT_STAND, RIGHT_STAND = 0, 1, 2, 3


    def handle_left_run(self):
        self.x -= 5
        self.run_frames += 1
        if self.x < 0:
            self.state = self.RIGHT_RUN
            self.x = 0
        if self.run_frames == 100:
            self.state = self.LEFT_STAND
            self.stand_frames = 0

    def handle_left_stand(self):
        self.stand_frames += 1
        if self.stand_frames == 50:
            self.state = self.LEFT_RUN
            self.run_frames = 0


    def handle_right_run(self):
        self.x += 5
        self.run_frames += 1
        if self.x > 800:
            self.state = self.LEFT_RUN
            self.x = 800
        if self.run_frames == 100:
            self.state = self.RIGHT_STAND
            self.stand_frames = 0


    def handle_right_stand(self):
        self.stand_frames += 1
        if self.stand_frames == 50:
            self.state = self.RIGHT_RUN
            self.run_frames = 0



    handle_state = {
        LEFT_RUN: handle_left_run,
        RIGHT_RUN: handle_right_run,
        LEFT_STAND: handle_left_stand,
        RIGHT_STAND: handle_right_stand
    }


    def update(self):
        self.frame = (self.frame + 1) % 8
        self.handle_state[self.state](self)



    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.run_frames = 0
        self.stand_frames = 0
        self.state = self.RIGHT_RUN
        if Boy.image == None:
            Boy.image = load_image('animation_sheet.png')
            Boy.hold_image = load_image('hold_state.png')

    def draw(self):
        self.image.clip_draw(self.frame * 100, self.state * 100, 100, 100, self.x, self.y)
    def draw2(self):
        if self.state == 0 or self.state == 1:
            self.hold_image.clip_draw(0,0,300,30, 300, 300)
        else:
            self.hold_image.clip_draw(0,50,300,70, 300, 300)


class Missile:
    image = None
    def __init__(self):
        if Missile.image == None:
            Missile.image = load_image('Items.png')
        self.angle = 0
        self.x = 400#random.randint(50,750)
        self.y = 550#random.randint(50,550)
        self.r = 1
        self.count = 0

    def draw(self):
        self.image.clip_draw(415, 410, 30, 30 , sin(self.angle)*self.r + self.x , cos(self.angle)*self.r + self.y)

    def init(self):
        self.x = 400#random.randint(50,750)
        self.y = 550#random.randint(50,550)
        self.r = 1
        self.count = 0

    def update(self):
        self.r += 10


class Monster:
    def __init__(self):
        self.image = load_image('K. Rool Mobile.png')
        self.x = 400
        self.y = 550
        self.gun = [Missile() for i in range(110)]
        self.count = 0
        self.angle = 1.57
        self.type = 1

    def draw(self):
        self.image.clip_draw(300, 330, 80, 80, self.x , self.y)

    def update(self):
        global num
        i = 0
        while i < num:
            i += 1
            self.gun[i].update()
            self.gun[i].draw()
        if i == 109:
            for re in self.gun:
                re.init()
            if 0 < self.gun[108].x and self.gun[108].x < 800:
                num = 0
            if 0 > self.gun[108].y:
                num = 0

    def init(self):
        i = 0
        while i < 109:
            i += 1
            self.gun[i].angle = self.angle
            if self.angle < 1.57:
                self.type = 1
            elif self.angle > 4.78:
                self.type = 0
            if self.type == 1:
                self.angle += 0.2
            elif self.type == 0:
                self.angle -= 0.2

def enter():
    global boy, grass, missile, monster
    monster = Monster()
    missile = Missile()
    boy = Boy()
    grass = Grass()



def exit():
    global boy, grass, missile, monster
    del(monster)
    del(missile)
    del(boy)
    del(grass)


def pause():
    pass


def resume():
    pass


def handle_events():

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            #LEFT_RUN, RIGHT_RUN, LEFT_STAND, RIGHT_STAND = 0, 1, 2, 3
            if boy.state == 0:
                boy.state = 1
            elif boy.state == 1:
                boy.state = 0
            elif boy.state == 2:
                boy.state = 0
                boy.run_frames = 0
            elif boy.state == 3:
                boy.state = 1
                boy.run_frames = 0
            monster.init()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_h:
            global test
            if test == 0:
                test = 1
            else:
                test = 0


def update():

    boy.update()


def draw():
    global test, num
    clear_canvas()
    grass.draw()
    boy.draw()
    monster.draw()
    monster.update()

    if test == 1:
        missile.draw()
        if num < 109:
            num += 1

    update_canvas()
    delay(0.04)





