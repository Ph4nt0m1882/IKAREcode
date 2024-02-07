"""
Conventions:

    naming convention: camelCase

    alias conventions: pygame --> pg
"""

import pygame as pg, os, sys

class Source:

    def __init__(self):
        self.dir=os.path.dirname(os.path.abspath(__file__))
        self.imgDir=os.path.join(self.dir,"images")
        self.screen=pg.display.set_mode((360,640), flags=pg.SCALED)
        self.width,self.height=self.screen.get_size()
        pg.display.set_caption("Asphalos")
        self.items=[pg.image.load(os.path.join(self.imgDir,file)).convert_alpha() for file in os.listdir(self.imgDir)]
        self.colorBG=(255,255,224,255)
        self.tree={"acceuil":False,"home":True}

    def show(self):
        self.screen.fill(self.colorBG)
        if self.tree["home"]:
            self.screen.blit(self.items[0],((self.width-self.items[0].get_width())/2,10))
            self.screen.blit(self.items[1],((self.width-self.items[1].get_width())/2,self.height/2-(self.items[1].get_height())*1.1))
            self.screen.blit(self.items[3],((self.width-self.items[3].get_width())/2,self.height/2+(self.items[1].get_height())*0.1))

    def running(self):
        while True:
            self.show()
            for event in pg.event.get():
                if event.type==pg.QUIT or (event.type==pg.KEYDOWN and event.type==pg.K_ESCAPE):
                    pg.quit()
                    sys.exit()
            pg.display.flip()