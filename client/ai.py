#python imports
from random import choice


def decide(wm):
    is_white = bool(wm.my_color)
    return choice(wm.all_moves(is_white))
