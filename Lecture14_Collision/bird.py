import game_framework
from pico2d import *
from ball import Ball

import game_world
import random

# Bird Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 130.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# 매의 속도가 약 390 km/hours 이라고 해서 그 1/3 속도로 정함

# Bird Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

# Bird States

class FlyState:

    def enter(bird, event):
        pass

    def exit(bird, event):
        pass

    def do(bird):
        bird.frame = (bird.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14

        if bird.x > 1600:
            bird.velocity = -1
        elif bird.x < 0:
            bird.velocity = 1

        bird.x += bird.velocity * RUN_SPEED_PPS * game_framework.frame_time

    def draw(bird):
        if bird.velocity == 1:
            bird.image_r.clip_draw(int(bird.frame) * 100, 0, 100, 100, bird.x, bird.y, 30, 30)  # 크기 10픽셀 당 30cm 90cm로 정함 (45cm로 해봤을때 너무 새가 작았음)
        else:
            bird.image_l.clip_draw(int(bird.frame) * 100, 0, 100, 100, bird.x, bird.y, 30, 30)

class Bird:
    image_r = None
    image_l = None
    def __init__(self):
        self.x, self.y = random.randint(0, 1600), random.randint(0, 600)
        if Bird.image_r == None:
            Bird.image_r = load_image('bird100x100x14.png')
        if Bird.image_l == None:
            Bird.image_l = load_image('bird100x100x14_left.png')
        self.velocity = random.randint(0, 2)
        if self.velocity == 0:
            self.velocity = -1
        self.frame = 0
        self.event_que = []
        self.cur_state = FlyState
        self.cur_state.enter(self, None)

    def update(self):
        self.cur_state.do(self)

    def draw(self):
        self.cur_state.draw(self)

