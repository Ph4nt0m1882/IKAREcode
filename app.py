import pygame as pg,os,sys

class App:

    def __init__(self):
        self.screen=pg.display.set_mode(((360,680)))
        pg.display.set_caption("IKARE")
        self.width,self.height=self.screen.get_size()
        self.colorBG=(255,255,224,255)

    def show(self):
        self.scren.fill(self.colorBG)

    def running(self):
        while True:
            for event in pg.event.get():
                if event.type==pg.QUIT:
                    pg.quit()
                    sys.exit()
            pg.display.flip()