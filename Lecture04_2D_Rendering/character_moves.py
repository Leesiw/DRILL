from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

# fill here


character_x = 400
character_y = 90

character_direction = 0

Rect_or_Circle = True
angle = -90


while True:
    if Rect_or_Circle:
        if character_direction == 0 or character_direction == 4:
            character_x += 2
            if character_direction == 4 and character_x >= 400:
                Rect_or_Circle = False
                character_direction = 0
            elif character_x >= 780:
                character_direction = 1
        elif character_direction == 1:
            character_y += 2
            if character_y >=560:
                character_direction = 2
        elif character_direction == 2:
            character_x -= 2
            if character_x <= 20:
                character_direction = 3
        elif character_direction == 3:
            character_y -= 2
            if character_y <= 90:
                character_direction = 4
    else:
        character_x = 400 + 310 * math.cos(angle / 360 * 2 * math.pi)
        character_y = 400 + 310 * math.sin(angle / 360 * 2 * math.pi)
        angle += 1

        if angle >= 270:
            angle = -90
            Rect_or_Circle = True

    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(character_x, character_y)
    delay(0.01)

    
close_canvas()
