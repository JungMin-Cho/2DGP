import random

import json
import os

from pico2d import *

import time
import game_framework
import title_state

from bullet import Bullet
from character import Character
from monster import Monster

name = "MainState"

character = None
grass = None
font = None

bullet = None
monster = None


class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

def enter():
    global character, grass, bullet, monster
    monster = Monster()
    bullet = Bullet()
    character = Character()
    grass = Grass()



def exit():
    global character, grass, bullet, monster
    del(monster)
    del(bullet)
    del(character)
    del(grass)


def pause():
    pass


def resume():
    pass


def handle_events(frame_time):

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_h):
                monster.state = Monster.PATTERN_1
                monster.initbullet()
                print("h")
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_j):
                monster.state = Monster.PATTERN_2
                monster.initbullet()
                print("h")
            else:
                character.handle_event(event)


def update(frame_time):
    character.update(frame_time)

    monster.update(frame_time)




def draw(frame_time):
    global test
    clear_canvas()
    grass.draw()
    monster.draw()
    character.draw()
    update_canvas()





