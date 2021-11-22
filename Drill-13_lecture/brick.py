import random

from pico2d import *

import game_framework
import game_world
import server
import collision


class Brick:
    def __init__(self):
        self.image = load_image('brick180x40.png')
        self.x, self.y = 100, 200
        self.speed = 200 # 200 pixel per second

        self.child_balls = [] # 발판에 속한 볼들의 리스트

    def update(self):
        self.x += game_framework.frame_time * self.speed
        if self.x > 1600:
            self.x = 1600
            self.speed = -self.speed
        if self.x < 0:
            self.x = 0
            self.speed = -self.speed

        for ball in server.balls.copy():
            if collision.collide(self, ball):
                self.attach_ball(ball)
                server.balls.remove(ball)


        for ball_ in self.child_balls.copy():
            for ball in server.balls.copy():
                if collision.collide(ball, ball_):
                    self.attach_ball(ball)
                    server.balls.remove(ball)

        # 자식 볼들의 개수를 확인한다.
        if len(self.child_balls) > 10:
            for ball in self.child_balls:
                ball.parent = None
                server.balls.append(ball)

                game_world.remove_object(self)
                # 부모 자식 관계를 끊는다
                # 볼들을 balls로 다시 보낸다
                # brick을 없앤다






    def draw(self):
        self.image.draw(self.x, self.y)


    def draw_bb(self):
        draw_rectangle(*self.get_bb())
        pass

    def get_bb(self):
        return self.x-90, self.y-20, self.x+90, self.y+20

    def attach_ball(self, ball):
        self.child_balls.append(ball)
        ball.set_parent(self) # 볼에 대해서 부모를 정한다
