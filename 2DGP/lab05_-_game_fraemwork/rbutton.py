__author__ = 'cho'

from pico2d import*

class Rbutton:

    def __init__(self):
        self.image = load_image('r.png') # 960x272

    def draw(self):
        self.image.clip_draw(0,0,413,355,400,300)
        pass

    def update(self, frame_time):
        pass
    pass