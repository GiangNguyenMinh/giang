import pygame as py
import math
import random
from queue import PriorityQueue
py.init()
FPS = 60
height = 600
width = 800
clock = py.time.Clock()
clock.tick(10)
win = py.display.set_mode((width, height))
image = py.transform.rotate(py.transform.scale(py.image.load('car.png'), (50, 50)), 90)
image_down = py.transform.rotate(image, 270)
py.display.set_caption("test")
White = (255, 255, 255)


def draw():
    win.fill(White)

    # py.draw.rect(win, (239, 20, 138), rect1)
    # win.blit(image, (x, y))

    py.display.update()
def titi(t, x, y):
    i = 0
    while True:
        if i >= len(t):
            X = 100
            y = 100
        if (t[i] == 1):
            x += 10
            win.blit(image, (x, y))
        elif (t[i] == -1):
            y += 10
            win.blit(image_down, (x, y))
            i += 1
        draw()


def main():
    done = True
    x = 300
    y = 300

    t = [-1, -1, -1, -1, 1, -1 , 1, 1, 1, 1, -1, -1, -1, 1, 1, 1, 1]




    while done:
        draw()

        # rect1 = py.Rect(x, y, 50, 50)
        for event in py.event.get():
            if event.type == py.QUIT:
                done = False
            if event.type == py.KEYDOWN:
                if event.key == py.K_c:

                    i = 0
                    while i < len(t):
                        clock.tick(2)
                        win.fill(White)
                        if (t[i] == 1):
                            x += 10
                            win.blit(image, (x, y))
                        elif (t[i] == -1):
                            y += 10
                            win.blit(image_down, (x, y))
                        i += 1

                        py.display.update()








if __name__ == '__main__':
    main()






