from pico2d import *
import random

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.image = load_image('run_animation.png')
        self.frame = random.randint(0, 8)

    def update(self):
        self.x += 5
        self.frame = (self.frame+1) % 8

    def draw(self):
        self.image.clip_draw(100 * self.frame, 0, 100, 100, self.x, self.y)

class Ball:
    def __init__(self):
        if random.randint(0, 2) == 0:
            self.image = load_image('ball21x21.png')
        else:
            self.image = load_image('ball41x41.png')
        self.x = random.randint(0, 800)
        self.y = 599
        self.speed = random.randint(10, 30)
    def draw(self):
        self.image.draw(self.x, self.y)
    def fall(self):
        if (self.y > 65):
            self.y -= self.speed
        else:
            self.y = 65

def handle_events():
    global running
    global start
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

running = True
start = False

open_canvas()
grass = Grass()
team = [Boy() for i in range(1, 11+1)]
balls = [Ball() for i in range(1,20+1)]

while running:
    handle_events()

    # game_logic
    for boy in team:
        boy.update()

    for ball in balls:
        ball.fall()

    # game_drawing
    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()

    for ball in balls:
        ball.draw()

    update_canvas()

    delay(0.05)
