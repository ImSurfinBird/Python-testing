import subprocess
import sys


def install(package):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    except:
        print("Module doesn't exist")


install('pygame')

import pygame as pg


class Suffer:
    def duplicate_object(self, object_name):
        self.active[self.key] = self.objects[object_name].copy()
        self.key += 1

    def move(self, path, object_data):
        self.remove_object(object_data)
        if (object_data['x'], object_data['y']) in path.keys():
            object_data['direction'] = path[(object_data['x'], object_data['y'])]
        if object_data['direction'] == 'UP':
            object_data['y'] -= object_data['speed']
        if object_data['direction'] == 'DOWN':
            object_data['y'] += object_data['speed']
        if object_data['direction'] == 'LEFT':
            object_data['x'] -= object_data['speed']
        if object_data['direction'] == 'RIGHT':
            object_data['x'] += object_data['speed']
        self.create_object(object_data)
        return object_data

    def remove_object(self, object_data):
        pg.draw.rect(self.win, self.bg, (object_data['x'], object_data['y'], object_data['width'], object_data['height']))

    def create_object(self, object_data):
        pg.draw.rect(self.win, object_data['color'],
                     (object_data['x'], object_data['y'], object_data['width'], object_data['height']))

    def init_objects(self):
        object1 = {
            'name': "object1",
            'width': 50,
            'height': 50,
            'color': (255, 0, 0),
            'x': 50,
            'y': 50,
            'displayed': True,
            'drag': False,
            'moving': False,
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
        self.objects = {
            object1['name']: object1,
            enemy['name']: enemy,
        }
        for x in self.objects:
            if self.objects[x].get('displayed') != None:
                self.create_object(self.objects[x])
        pg.display.update()

    def drag_and_drop(self, object_data):
        if self.m[0] == 1 and self.p[0] in range(object_data['x'], object_data['x'] + object_data['width']) and self.p[1] in range(object_data['y'], object_data['y'] + object_data['height']):
            object_data['drag'] = True
        if self.m[0] == 0 and object_data['drag']:
            object_data['drag'] = False
            self.remove_object(object_data)
            object_data['x'] = self.p[0] - int(object_data['width'] / 2)
            object_data['y'] = self.p[1] - int(object_data['height'] / 2)
            self.create_object(object_data)
            pg.display.update()
        return object_data

    def __init__(self):
        #Initialize background variables:
        self.bg = (0, 0, 0)
        self.window_size = (1910, 1040)
        self.drags = {}
        run = True
        self.counter = -1
        self.key = 0
        self.active = {}
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

        self.init_objects()

        while run:
            pg.time.delay(100)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False

            self.m = pg.mouse.get_pressed()
            self.p = pg.mouse.get_pos()
            self.counter += 1

            if self.counter % 100 == 0:
                self.duplicate_object('enemy')

            for x in self.objects:
                if self.objects[x].get('drag') != None:
                    self.objects[x] = self.drag_and_drop(self.objects[x])
            for x in self.active:
                if self.active[x].get('direction') != None:
                    self.active[x] = self.move(path, self.active[x])

            pg.display.update()


Suffer()
