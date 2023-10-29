import os
import pico2d

# 경로 설정
os.chdir(os.path.dirname(os.path.abspath(__file__)))
pico2d.open_canvas()

# 이미지 로드
background_image = pico2d.load_image('title.png')
start_button_image = pico2d.load_image('start_button.png')
quit_button_image = pico2d.load_image('quit_button.png')

# 화면에 이미지 출력
background_image.draw(400, 300)
quit_button_image.draw(400, 100)
start_button_image.draw(400, 200)

# 화면 업데이트
pico2d.update_canvas()

# 마우스 이벤트 처리
running = True
while running:
    events = pico2d.get_events()
    for event in events:
        if event.type == pico2d.SDL_MOUSEBUTTONDOWN:
            x, y = event.x, 600 - event.y
            if 300 < x < 500 and 50 < y < 150:  # quit_button 영역
                running = False

pico2d.close_canvas()
