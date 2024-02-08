"""
Conventions:

    naming convention: camelCase

    alias conventions: pygame --> pg
"""

from numpy import true_divide
import pygame as pg, os, sys, sqlite3
from entry import Entry

class Source:

    def __init__(self):
        self.dir=os.path.dirname(os.path.abspath(__file__))
        self.imgDir=os.path.join(self.dir,"images")
        self.screen=pg.display.set_mode((360,640), flags=pg.RESIZABLE | pg.SCALED, vsync=1)
        self.width,self.height=self.screen.get_size()
        pg.display.set_caption("Asphalos")
        self.items={file:pg.image.load(os.path.join(self.imgDir,file)).convert_alpha() for file in os.listdir(self.imgDir)}
        self.colorBG=(255,255,224,255)
        self.tree={"acceuil":True,"inscryption":False,"home":False}
        self.rect={}
        self.font=pg.font.SysFont("Arial",20,True)
        self.passwordFont=pg.font.Font(os.path.join(self.dir,"PasswordFont.ttf"),32)
        self.entry={}

    def initScroll(self):
        self.scrollRect=pg.Rect((self.width/20,self.screen.get_height()-self.width/20-self.height*0.75),(self.width-self.width/10,self.height*0.75))
        self.scroll=pg.Surface((self.scrollRect.width,640))
        self.h=0
        self.scroll.blit(self.font.render("nom",True,(0,0,1)),((self.scrollRect.width-self.font.render("nom",True,(0,0,1)).get_width())/2,20))
        self.scroll.blit(self.font.render("prenom",True,(0,0,1)),((self.scrollRect.width-self.font.render("prenom",True,(0,0,1)).get_width())/2,100))
        self.scroll.blit(self.font.render("adresse mail",True,(0,0,1)),((self.scrollRect.width-self.font.render("adresse mail",True,(0,0,1)).get_width())/2,180))
        self.scroll.blit(self.font.render("téléphon",True,(0,0,1)),((self.scrollRect.width-self.font.render("téléphone",True,(0,0,1)).get_width())/2,260))
        self.scroll.blit(self.font.render("mot de passe",True,(0,0,1)),((self.scrollRect.width-self.font.render("mot de passe",True,(0,0,1)).get_width())/2,340))
        self.scroll.blit(self.font.render("confirmation mot de passe",True,(0,0,1)),((self.scrollRect.width-self.font.render("confirmation mot de passe",True,(0,0,1)).get_width())/2,420))
        self.entry={
            "lastName":Entry(self.scroll,(20,40),self.scrollRect.top-self.h,self.scrollRect.left,(self.scrollRect.width-40,40),self.font,colorUnder=(0,0,1),underWidth=3,colorNonActiveBackground=self.colorBG,colorActiveBackground=(224,255,232,255)),
            "name":Entry(self.scroll,(20,120),self.scrollRect.top-self.h,self.scrollRect.left,(self.scrollRect.width-40,40),self.font,colorUnder=(0,0,1),underWidth=3,colorNonActiveBackground=self.colorBG,colorActiveBackground=(224,255,232,255)),
            "mail":Entry(self.scroll,(20,200),self.scrollRect.top-self.h,self.scrollRect.left,(self.scrollRect.width-40,40),self.font,colorUnder=(0,0,1),underWidth=3,colorNonActiveBackground=self.colorBG,colorActiveBackground=(224,255,232,255)),
            "phone":Entry(self.scroll,(20,280),self.scrollRect.top-self.h,self.scrollRect.left,(self.scrollRect.width-40,40),self.font,colorUnder=(0,0,1),underWidth=3,colorNonActiveBackground=self.colorBG,colorActiveBackground=(224,255,232,255)),
            "password":Entry(self.scroll,(20,360),self.scrollRect.top-self.h,self.scrollRect.left,(self.scrollRect.width-40,40),self.passwordFont,colorUnder=(0,0,1),underWidth=3,colorNonActiveBackground=self.colorBG,colorActiveBackground=(224,255,232,255)),
            "confPassword":Entry(self.scroll,(20,440),self.scrollRect.top-self.h,self.scrollRect.left,(self.scrollRect.width-40,40),self.passwordFont,colorUnder=(0,0,1),underWidth=3,colorNonActiveBackground=self.colorBG,colorActiveBackground=(224,255,232,255))
        }

    def show(self):
        self.screen.fill(self.colorBG)
        if self.tree["acceuil"]:
            self.screen.blit(pg.transform.scale(self.items["tree app.png"],(self.width,self.height)).subsurface((0,0,self.width,150)),(0,0))
            self.screen.blit(self.items["logoApp.png"],(75,67))
            self.screen.blit(pg.transform.scale(self.items["tree app.png"],(self.width,self.height)).subsurface((0,150,self.width,self.height-150)),(0,150))
            self.rect["connectButton.png"]=pg.Rect(((self.width-self.items["connectButton.png"].get_width())/2,self.height/2-(self.items["connectButton.png"].get_height())*1),self.items["connectButton.png"].get_size())
            self.screen.blit(self.items["connectButton.png"],self.rect["connectButton.png"])
            self.rect["inscryptionButton.png"]=pg.Rect(((self.width-self.items["inscryptionButton.png"].get_width())/2,self.height/2+(self.items["inscryptionButton.png"].get_height())*0.1),self.items["inscryptionButton.png"].get_size())
            self.screen.blit(self.items["inscryptionButton.png"],self.rect["inscryptionButton.png"])
        if self.tree["inscryption"]:
            self.rect["backArrow.png"]=pg.Rect((5,5),self.items["backArrow.png"].get_size())
            self.screen.blit(self.items["backArrow.png"],(5,5))
            self.screen.blit(self.items["AsphalosTitle.png"],((self.width-self.items["AsphalosTitle.png"].get_width())/2,10))
            for value in self.entry.values():value.draw(self.scrollRect.top+self.h,self.scrollRect.left)
            render=pg.Surface(self.scrollRect.size)
            render.blit(self.scroll,(0,self.h))
            render.set_colorkey((0,0,0))
            self.screen.blit(render,self.scrollRect.topleft)
        if self.tree["home"]:
            self.screen.blit(self.items["AsphalosTitle.png"],((self.width-self.items["AsphalosTitle.png"].get_width())/2,10))
            self.screen.blit(self.items["domesticButton.png"],((self.width-self.items["domesticButton.png"].get_width())/2,self.height/2-(self.items["domesticButton.png"].get_height())*1.15))
            self.screen.blit(self.items["securityButton.png"],((self.width-self.items["securityButton.png"].get_width())/2,self.height/2+(self.items["securityButton.png"].get_height())*0.15))

    def back(self):
        if self.tree["inscryption"] and not pg.mouse.get_pressed()[0]:
            if self.h>0:self.h-=10
            if self.h<self.scrollRect.height-self.scroll.get_height():self.h+=10

    def running(self):
        while True:
            self.show()
            self.back()
            lst=[ent.getActive() for ent in self.entry if type(ent)==Entry]
            if not True in lst:
                for event in pg.event.get():
                    if event.type==pg.QUIT or (event.type==pg.KEYDOWN and event.type==pg.K_ESCAPE):
                        pg.quit()
                        sys.exit()
                    if event.type==pg.MOUSEBUTTONDOWN:
                        if self.tree["inscryption"]:
                            if self.rect["backArrow.png"].collidepoint(event.pos):
                                for key in self.tree.keys():self.tree[key]=True if key=="acceuil" else False
                            if self.scrollRect.collidepoint(event.pos):
                                self.startPos=event.pos
                        if self.tree["acceuil"]:
                            if self.rect["inscryptionButton.png"].collidepoint(event.pos):
                                self.initScroll()
                                for key in self.tree.keys():self.tree[key]=True if key=="inscryption" else False
                    if event.type==pg.MOUSEMOTION:
                        if self.tree["inscryption"]:
                            if self.scrollRect.collidepoint(event.pos) and event.buttons[0]==1:
                                if not hasattr(self, "startPos"):self.startPos=event.pos
                                self.deltay=event.pos[1]-self.startPos[1]
                                self.startPos=event.pos
                                self.h+=self.deltay
                    if event.type==pg.MOUSEBUTTONUP:
                        if hasattr(self, "startPos"): del self.startPos
            pg.display.flip()
