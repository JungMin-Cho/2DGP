__author__ = 'cho'

from pico2d import*

class Block:
    image = None
    def __init__(self):
        self.x = 0;
        self.y = 0;
        self.height = 0;
        self.width = 0;
        if Block.image == None:
            Block.image = load_image('grass.png')

    def init_block(self, x,y,w,h):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        pass

    def draw(self):
        self.image.draw(self.x,self.y,self.width*2,self.height*2)
        self.draw_bb()

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - self.width, self.y - self.height, self.x + self.width, self.y + self.height
    pass