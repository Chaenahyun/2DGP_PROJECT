#키보드 방향키 이동
from pico2d import *

ground_width, ground_height =800, 450
open_canvas(ground_width, ground_height)
ground = load_image('ground_full.png')

idle_fielder = load_image('idle_defender.png')
running_fielder_to_left = load_image('running_defender_to_left.png')
running_fielder_to_right = load_image('running_defender_to_right.png')
catching_and_throwing_fielder = load_image('catching_and_throwing_defender.png')
catching_ground_ball_and_throwing_fielder = load_image('catching_ground_ball_and_throwing_defender.png')
jump_catching_and_throwing_fielder = load_image('jump_catching_and_throwing_defender.png')


running = True
x = 400  # 초기 x 좌표
y = 160  # 초기 y 좌표
frame = 0  # 변수 초기화

dir_x = 0
dir_y = 0

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 450

character_width = 60
character_height = 60


def handle_events():
    global running, dir_x, dir_y, fielder, is_idle, idle_frame  # 전역 변수
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_x += 1  # 오른쪽
                #character = character_right  # 오
                is_idle = False
            elif event.key == SDLK_LEFT:
                dir_x -= 1  # 왼쪽
                #character = character_left  # 왼
                is_idle = False
            elif event.key == SDLK_UP:
                dir_y += 1  # 위
                #character = character_up  # 위
                is_idle = False
            elif event.key == SDLK_DOWN:
                dir_y -= 1  # 아래
                #character = character_down  # 아래
                is_idle = False
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_x -= 1  # 이동 방향 반전
            elif event.key == SDLK_LEFT:
                dir_x += 1
            elif event.key == SDLK_UP:
                dir_y -= 1
            elif event.key == SDLK_DOWN:
                dir_y += 1


while running:
    clear_canvas()
    ground.draw(ground_width//2, ground_height//2)

    idle_fielder.clip_draw(frame * 20, 0, 20, 20, x, y, 30, 30)
    running_fielder_to_left.clip_draw(frame * 20, 0, 20, 20, x, y, 30, 30)
    running_fielder_to_right(frame * 20, 0, 20, 20, x, y, 30, 30)
    catching_and_throwing_fielder.clip_draw(frame * 20, 0, 20, 20, x, y, 30, 30)
    catching_ground_ball_and_throwing_fielder.clip_draw(frame * 20, 0, 20, 20, x, y, 30, 30)
    jump_catching_and_throwing_fielder.clip_draw(frame * 20, 0, 20, 20, x, y, 30, 30)
    update_canvas()
    handle_events()


    # x 방향
    if dir_x > 0:  # 오른쪽 이동
        if x + dir_x * 5 + character_width // 2 <= SCREEN_WIDTH:
            x += dir_x * 5
    elif dir_x < 0:  # 왼쪽 이동
        if x + dir_x * 5 - character_width // 2 >= 0:
            x += dir_x * 5

    # y 방향
    if dir_y > 0:  # 위로 이동
        if y + dir_y * 5 + character_height // 2 <= SCREEN_HEIGHT:
            y += dir_y * 5
    elif dir_y < 0:  # 아래로 이동
        if y + dir_y * 5 - character_height // 2 >= 0:
            y += dir_y * 5

    frame = (frame + 1) % 8
    delay(0.2)

    if not running:
        break

close_canvas()
