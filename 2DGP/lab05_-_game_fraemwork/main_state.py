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
from background import Background
from block import Block
from characterbullet import CBullet
from scroll import Scroll
from rbutton import Rbutton


name = "MainState"

LEFT, RIGHT, TOP, BOTTOM, COLLIDE = 1,2,3,4,5

character = None
background = None
font = None

bullet = None
monster = None
current_time = 0
#block = [Block() for i in range(2)]
block = None
cbullet = None
scroll = None
r = None

def enter():
    global character, grass, bullet, monster, block, cbullet, scroll, r
    cbullet = [CBullet() for i in range(100)]
    block = [Block() for i in range(6)]
    block[0].init_block(30,220,50,15)
    block[1].init_block(200,120,50,15)
    block[2].init_block(400,220,50,15)
    block[3].init_block(600,120,50,15)
    block[4].init_block(750,220,50,15)
    #block[5].init_block(460,200,50,30)
    aa = 1
    #for blocks in block:
    #    blocks.init_block(300 * aa,200,30,100)
    #    aa += 1
    #cbullet = CBullet()
    monster = Monster()
    bullet = Bullet()
    character = Character()
    grass = Background()
    scroll = Scroll(1395, 866)
    r = Rbutton()
    # sound = load_music('backbgm.wav')
    # sound.set_volume(64)
    # sound.repeat_play()



def exit():
    global character, grass, bullet, monster, block, cbullet, scroll, r
    del(block)
    del(monster)
    del(bullet)
    del(character)
    del(grass)
    del(cbullet)
    del(scroll)
    del(r)



def pause():
    pass


def resume():
    pass

def collide(a, b):
    # fill here
    left_a, bottom_a, right_a, top_a =  a.get_bb()
    left_b, bottom_b, right_b, top_b =  b.get_bb()

    if left_a > right_b : return False
    if right_a < left_b : return False
    if top_a < bottom_b : return False
    if bottom_a > top_b : return False
    return True

def collide_check(a, b):
    # fill here
    left_a, bottom_a, right_a, top_a =  a.get_bb()
    left_b, bottom_b, right_b, top_b =  b.get_bb()

    if left_a > right_b : return RIGHT
    if right_a < left_b : return LEFT
    if top_a < bottom_b : return BOTTOM
    if bottom_a > top_b : return TOP
    return COLLIDE

def handle_events(frame_time):

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_r:
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
                print("j")
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_k):
                monster.state = Monster.PATTERN_3
                monster.initbullet()
                print("k")
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_l):
                monster.state = Monster.PATTERN_4
                monster.initbullet()
                print("l")
            elif (event.type,event.key) == (SDL_KEYDOWN, SDLK_z):
                if character.firecount < 100:
                    cbullet[character.firecount].initbullet(character.composite,character.x,character.y)
                    character.firecount += 1
                else:
                    character.firecount = 0
                #cbullet.ex = 1
            else:
                character.handle_event(event)


def update(frame_time):
    global  current_time
    current_time += frame_time
    scroll.update(frame_time)
    if current_time > 0.05:
        current_time = 0

    character.update(frame_time)

    if collide(character,grass):
        character.stopy = 1
    for blocks in block:
        temp = collide_check(character, blocks)
        if temp == COLLIDE:
            character.stopy = 1
            if blocks.x + blocks.width < character.x:
                character.x += 2
            elif character.x < blocks.x - blocks.width:
                character.x -= 2
            elif character.y < blocks.y - blocks.height:
                character.y = blocks.y - blocks.height - character.height - 2
            elif blocks.y + blocks.height < character.y:
                character.y = blocks.y + blocks.height + character.height + 2
    if monster.hp:
        monster.update(frame_time)
    for test in monster.gun:
        if collide(test, character):
            test.hit = 1
            character.alive = 0
    for cbullets in cbullet:
        cbullets.update(frame_time)
        if cbullets.ex and monster.hp:
            if collide(cbullets, monster):
                cbullets.ex = 0
                monster.hp -= 1


def draw(frame_time):
    global test
    clear_canvas()
    scroll.draw()
    grass.draw()
    if 0 < monster.hp:
        monster.draw()
    else:
        r.draw()
    if character.alive:
        character.draw()
        for cbullets in cbullet:
            cbullets.draw()
    else:
        r.draw()
    #for i in block:
    #    i.draw()
    for blocks in block:
        blocks.draw()
    update_canvas()





