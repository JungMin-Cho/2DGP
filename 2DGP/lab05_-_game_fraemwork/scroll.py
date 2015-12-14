__author__ = 'cho'

from pico2d import*

class Scroll:
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    SCROLL_SPEED_KMPH = 20.0                    # Km / Hour
    SCROLL_SPEED_MPM = (SCROLL_SPEED_KMPH * 1000.0 / 60.0)
    SCROLL_SPEED_MPS = (SCROLL_SPEED_MPM / 60.0)
    SCROLL_SPEED_PPS = (SCROLL_SPEED_MPS * PIXEL_PER_METER)

    def __init__(self, w, h):
        self.image = load_image('sky.png') # 960x272
        self.speed = Scroll.SCROLL_SPEED_PPS
        self.left = 0
        self.screen_width = w
        self.screen_height = h

    def draw(self):
        x = int(self.left)
        w = min(self.image.w - x, self.screen_width)
        self.image.clip_draw_to_origin(x, 0, w, self.screen_height, 0, 0)
        self.image.clip_draw_to_origin(0, 0, self.screen_width - w, self.screen_height, w, 0)
        pass

    def update(self, frame_time):
        self.left = (self.left + frame_time * self.speed) % self.image.w
        pass
    pass