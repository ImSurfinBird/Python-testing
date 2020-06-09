import subprocess
import sys


def install(package):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    except:
        print("Module doesn't exist")


install('pygame')

import pygame as pg
import ObjectHandling as obj
import ObjectFunctions as fun


object1 = {
        'name': "object1",
        'width': 50,
        'height': 50,
        'color': (255, 0, 0),
        'x': 50,
        'y': 50,
        'displayed': True,
        'drag': False,
        'type': "Rectangle",
}
enemy = {
        'name': "enemy",
        'width': 50,
        'height': 50,
        'color': (0, 255, 0),
        'x': 0,
        'y': 0,
        'speed': 5,
        'type': "Rectangle",
        'direction': 'RIGHT',
}
image = {
        'name': "image",
        'width': 50,
        'height': 50,
        'x': 50,
        'y': 50,
        #'image': pg.image.load('moon2SUFFER.png').convert_alpha(),
        'type': "Image",
}
objects = {
        object1['name']: object1,
        enemy['name']: enemy,
        image['name']: image,
}


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
        path = {
            (0, 0): 'RIGHT',
            (150, 0): 'DOWN',
            (150, 200): 'LEFT',
            (0, 200): 'UP',
        }

        pg.init()
        self.win = pg.display.set_mode(self.window_size)
        pg.display.set_caption("moon2SUFFER")
        pg.draw.rect(self.win, self.bg, (0, 0, self.window_size[0], self.window_size[1]))
        pg.display.update()

        self.objects = obj.create_object(self.objects, "Test", (0, 0), "moon2SUFFER.png")
        self.objects['Test']['drag'] = False
        self.objects['Test']['path'] = path
        self.objects['Test']['speed'] = 5
        self.objects['Test']['direction'] = 'RIGHT'

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
            self.counter += 1

            for x in self.active:
                if self.active[x].get('drag') != None:
                    self.active[x] = fun.drag_and_drop(self.m, self.p, self.active[x])
                if self.active[x].get('path') != None:
                    self.active[x] = fun.move_path(self.active[x])

            obj.update_display(self.win, self.bg, self.window_size, self.active)


Suffer()
