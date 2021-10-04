from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def character_move():
    global x, y
    global character_x, character_y
    global looking_at
    if x > character_x:
        character_x += 2
        looking_at = 1
    elif x < character_x:
        character_x -= 2
        looking_at = 0
    if y > character_y:
        character_y += 2
    elif y < character_y:
        character_y -= 2

def handle_events():
    global running
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, KPU_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass


open_canvas(KPU_WIDTH, KPU_HEIGHT)

# fill here
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
arrow = load_image('hand_arrow.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
character_x, character_y = x, y
looking_at = 1
frame = 0
hide_cursor()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * looking_at, 100, 100, character_x, character_y)
    arrow.draw(x, y)
    update_canvas()
    frame = (frame + 1) % 8

    handle_events()
    character_move()

close_canvas()
