import pygame as pg,os,sys

class App:

    def __init__(self):
        self.path=os.path.dirname(os.path.abspath(__file__))
        self.screen=pg.display.set_mode((360,680), flags=pg.SCALED)
        pg.display.set_caption("ASPHALOS")
        self.width,self.height=self.screen.get_size()
        self.colorBG=(255,255,224,255)
        self.items=[
            pg.image.load(os.path.join(self.path,"images/AsphalosTitle.png"))
        ]
        self.items[0]=pg.transform.scale(self.items[0],(self.items[0].get_width()*0.3,self.items[0].get_height()*0.3))
        self.pages={
            "start":True,
            "inscription":False,
            "connexion":False,
            "acceuil":False,
            "security":False,
            "domestique":False
        }

    def show(self):
        if self.pages["acceuil"]:
            self.screen.fill(self.colorBG)
            self.screen.blit(self.items[0],((self.width-self.items[0].get_width())//2,10))

    def running(self):
        while True:
            self.show()
            for event in pg.event.get():
                if event.type==pg.QUIT:
                    pg.quit()
                    sys.exit()
            pg.display.flip()