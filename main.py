"""
Use esc to exit, arrow keys to change smooth level

Your performance can make it look slightly different
"""

try: import curses
except ImportError: input("pip install windows-curses")
from time import sleep
from math import sin, cos

try: screen = curses.initscr()
except: print("You can't run it from ide!")
curses.curs_set(0)
curses.noecho()
screen.keypad(1) 
screen.nodelay(1)
screen.timeout(0)

def _wave(method, starting, smoother=1, height=10):
    numbers = []
    for i, y in zip(range(starting, starting+120), range(0, 120)):
        numbers.append((round(method(i/smoother))+height, y))
    return numbers

def cos_wave(*args, **kwargs): return _wave(cos, *args, **kwargs)
def sin_wave(*args, **kwargs): return _wave(sin, *args, **kwargs)


def visualize_list(screen, numbers, refresh=True):
    if refresh: screen.clear()
    for number in numbers:
        try: screen.addstr(*number, "█")
        except:
            print("You shrinked your command line to much!")
            return
    if refresh: screen.refresh()

def main(screen):
    i = 0
    smoother = 2
    while True:
        screen.clear()
        for h in range(1,7):
            if h % 2: nums = cos_wave(i, smoother, h*4)
            else: nums = sin_wave(i, smoother, h*4)
            visualize_list(screen, nums, False)
        key = screen.getch()
        if key == 27: break
        elif key == curses.KEY_RIGHT: smoother += 0.1
        elif key == curses.KEY_LEFT: smoother -= 0.1
        
        screen.refresh()
        sleep(0.01)
        i += 1

if __name__ == "__main__": curses.wrapper(main); curses.endwin()
