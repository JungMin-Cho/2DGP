__author__ = 'cho'
import random
import json
import os

from pico2d import *

import game_framework
import title_state


name = "MainState"


boy = None
grass = None
font = None
test = 0


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



def enter():
    global boy, grass, missile
    boy = Boy()
    grass = Grass()
    missile = Missile()


def exit():
    global boy, grass, missile
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
                #boy.stand_frames = 0
            elif boy.state == 3:
                boy.state = 1
                boy.run_frames = 0
        elif event.type == SDL_KEYDOWN and event.key == SDLK_h:
            global test
            if test == 0:
                test = 1
            else:
                test = 0


def update():
    global test, hold_image
    if test == 1:
        pass
    else:
        boy.update()


def draw():
    global test, missile
    clear_canvas()
    grass.draw()
    boy.draw()
    if test == 1:
        boy.draw2()

    update_canvas()
    delay(0.04)





