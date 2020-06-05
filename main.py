import pygame as pg


class Suffer:
    def movement_logic(self):
        m = pg.mouse.get_pressed()
        p = pg.mouse.get_pos()
        if m[0] == 1 and p[0] in range(self.x, self.x + self.width) and p[1] in range(self.y, self.y + self.height):
            while m[0] == 1:
                self.x, self.y = p
                m = pg.mouse.get_pressed()
        self.win.fill((0, 0, 0))
        pg.draw.rect(self.win, (255, 0, 0), (self.x, self.y, self.width, self.height))
        pg.display.update()

    def __init__(self):
        pg.init()
        self.win = pg.display.set_mode((500, 500))
        pg.display.set_caption("moon2SUFFER")
        self.x = 50
        self.y = 50
        self.width = 50
        self.height = 50
        self.vel = 5
        run = True
        while run:
            pg.time.delay(100)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
            self.movement_logic()


Suffer()
