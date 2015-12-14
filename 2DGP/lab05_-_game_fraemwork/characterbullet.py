__author__ = 'cho'
from pico2d import*

class CBullet:

    image = None
    hit_sound = None

    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    RUN_SPEED_KMPH = 90.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    print(RUN_SPEED_PPS)
    TIME_PER_ACTION = 0.2
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION

    FRAMES_PER_ACTION = 2
    IDLE_FRAMES_PER_ACTION = 2

    #PATTERN_1, PATTERN_2, PATTERN_3, PATTERN_4 = 0, 1, 2, 3

    def __init__(self):
        if CBullet.image == None:
            CBullet.image = load_image('Items.png')
        self.angle = 0
        self.x = 100#random.randint(50,750)
        self.y = 100#random.randint(50,550)
        self.r = 1
        self.composite = 0
        self.count = 0
        self.fall_speed = 0.5
        self.frame = 0
        self.total_frames = 0
        self.state = 0
        self.hit = 0
        self.xdir = 1
        self.ex = 0
        if CBullet.hit_sound == None:
            pass
            #Bullet.hit_sound = load_music('scream.wav')
            #Bullet.hit_sound.set_volume(32)

    def draw(self):
        if self.ex:
            if self.composite == 0:
                self.image.clip_draw(self.frame * 35 + 315, 410, 30, 30, self.x, self.y)
                pass
            elif self.composite == 1:
                #print("ddddddddddddddddd")
                self.image.clip_composite_draw(self.frame * 35 + 315, 410, 30, 30, 0,'h', self.x, self.y, 30, 30)
                pass
            self.draw_bb()
        #if self.hit == 1:
        #    pass
        #else:
        #    self.image.clip_draw(315, 410, 30, 30 , self.x , self.y)
        #    self.draw_bb()
    def hits(self, bullet):
        self.hit_sound.play()
        pass

    def initbullet(self, dir, x, y):
        if dir == 0:
            self.xdir = 1
        elif dir == 1:
            self.xdir = -1

        self.composite = dir
        self.x = x
        self.y = y
        self.ex = 1

        pass


    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 15, self.y - 15, self.x + 15, self.y + 15

    def update(self, frame_time):
        if self.ex:
            distance = CBullet.RUN_SPEED_PPS * frame_time
            self.total_frames += CBullet.FRAMES_PER_ACTION * CBullet.ACTION_PER_TIME * frame_time
            self.frame = int(self.total_frames) % 2
            self.x += (self.xdir * distance)
            if self.x < 0:
                self.ex = 0
            elif 800 < self.x:
                self.ex = 0
            pass
    pass