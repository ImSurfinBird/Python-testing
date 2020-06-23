import subprocess
import sys


def install(package):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    except:
        print("Module doesn't exist")


install('pygame')

import pygame as pg
from PyGame import ObjectFunctions as fun, ObjectHandling as obj


class Suffer:
    def __init__(self):
        #Initialize background variables:
        self.bg = (0, 0, 0)
        self.window_size = (1910, 1040)
        self.drags = {}
        run = True
        self.counter = -1
        self.key = 0
        self.active = {}
        self.objects = {}

        pg.init()
        self.win = pg.display.set_mode(self.window_size)
        pg.display.set_caption("moon2SUFFER")
        pg.draw.rect(self.win, self.bg, (0, 0, self.window_size[0], self.window_size[1]))
        pg.display.update()

        self.objects = obj.create_object(self.objects, "Test", (0, 0), "moon2SUFFER.png")
        self.objects['Test']['drag'] = False

        self.active['Test'] = obj.duplicate_object('Test', self.objects)
        obj.display_object(self.win, 'Test', self.active)

        pg.display.update()

        while run:
            pg.time.delay(100)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False

            self.m = pg.mouse.get_pressed()
            self.p = pg.mouse.get_pos()

            for x in self.active:
                if self.active[x].get('drag') != None:
                    self.active[x] = fun.drag_and_drop(self.m, self.p, self.active[x])

            obj.update_display(self.win, self.bg, self.window_size, self.active)


Suffer()
