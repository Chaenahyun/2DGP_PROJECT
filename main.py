#main.py
from pico2d import open_canvas, close_canvas
import game_framework
import title_mode
import play_mode
open_canvas()
game_framework.run(title_mode)
close_canvas()



