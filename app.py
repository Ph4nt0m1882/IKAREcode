import pygame as pg,os,sys

class App:

    def __init__(self):
        self.screen=pg.display.set_mode(((360,680)))
        pg.display.set_caption("IKARE")

    def running(self):
        while True:
            for event in pg.event.get():
                if event.type==pg.QUIT:
                    pg.quit()
                    sys.exit()
            pg.display.flip()