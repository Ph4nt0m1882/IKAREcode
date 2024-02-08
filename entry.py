import pygame as pg, sys # importation nécessaire: une gestion des évènement est nécessaire et sys permet de quitter le programme depuis ici

class Entry:

    def __init__(self,
            surface: pg.Surface, # fenêtre de l'application
            position: tuple, # position de l'entrée dans la fenêtre
            high: int, # position de la surface en hauteur
            left: int, # position de la surface à gauche
            size: tuple, # taille de l'entrée texte
            font: pg.font.Font=None, # police de charactère
            txtColor: tuple=(0,0,0), # couleur de la police
            colorUnder: tuple=None, # couleur du cadre
            underWidth: int=1, # épaisseur du cadre
            colorNonActiveBackground: tuple=None, # couleur du fond de l'entrée si elle est inactive 
            colorActiveBackground: tuple=None # si elle est active
    ) -> None:
        self.surface=surface # création de la surface
        self.pos=position # généralisation de la position
        self.txt="\\" # définition du texte avec un curseur
        self.high=high
        self.left=left
        self.font=font if font is not None else pg.font.Font(None,32) # généralisation de la police
        self.size=size # généralisation de la taille
        self.rect=pg.Rect(self.pos,self.size) # création du rect pour sprite
        self.colorbg=[colorNonActiveBackground,colorActiveBackground] # généralisation des background
        self.colorUnder=colorUnder # généralisation du cadre
        self.underWidth=underWidth # généralisation de l'épaisseur
        self.txtColor=txtColor # généralisation de la couleur du texte
        self.active=False # si la fenêtre est active ou non
        if txtColor==(0,0,0):self.txtColor=(0,0,1) # si on laisse la couleur initiale en noir et qu'il n'y à pas de fond, je change légèrement la couleur pour éviter que le noir ce fasse aspirer par le set colorkey
        self.cursorPos=0 # position initiale du curseur qui est la référence pour disposer le texte sur l'entrée
        self.showCursor=True # permet de faire clignoter le curseur
        self.iteration=0 # sert à calculer le temps

    def getCursorPos(self,eventPos): # change la position du curseur quand on clique
        txt=self.getText()
        leftPos=self.cursorPos-self.font.render(self.txt.split("\\")[0],True,self.txtColor).get_width() # calcul la position du texte
        rightPos=leftPos+self.font.render(txt,True,self.txtColor).get_width()
        newPos=eventPos[0]-self.pos[0]
        def foundPosInTxt(txt,leftPos,rightPos,newPos):
            nbg=len(txt)//2
            nbd=len(txt)-nbg
            if nbg==0 and nbd==0:
                return "\\"
            elif nbg==0 or nbd==0:
                if newPos-leftPos>=rightPos-newPos:return f"{txt}\\"
                else:return f"\\{txt}"
            txtg,txtd=txt[:nbg],txt[nbg:]
            centerPos=leftPos+self.font.render(txtg,True,self.txtColor).get_width()
            if newPos<=centerPos:
                return foundPosInTxt(txtg,leftPos,centerPos,newPos)+txtd
            else:
                return txtg+foundPosInTxt(txtd,centerPos,rightPos,newPos)
        self.txt=foundPosInTxt(txt,leftPos,rightPos,newPos)
        self.cursorPos=leftPos+self.font.render(self.txt.split("\\")[0],True,self.txtColor).get_width()

    def draw(self,high,left):
        self.high=high
        self.left=left
        self.rect.top=self.high+self.pos[1]
        self.rect.left=self.left+self.pos[0]
        if self.active:
            self.iteration+=1
            if self.iteration%400==0:self.showCursor=not self.showCursor
        else: self.showCursor=False
        if pg.mouse.get_pressed()[0]:
            if self.rect.collidepoint(pg.mouse.get_pos()):
                self.active=True # on active si c'est sur l'entrée texte
                self.showCursor=True
                pg.key.start_text_input() # on active la saisie
            else:
                self.active=False # sinon on désactive
                pg.key.stop_text_input() # et on désactive la saisie
        if self.getActive():
            for event in pg.event.get(): # gestion des évènement vis à vie de l'entrée texte
                if event.type==pg.QUIT: # si on doit quitter
                    pg.quit # on quitte pygame
                    sys.exit() # on sort du programme
                if self.active:
                    if event.type==pg.MOUSEBUTTONDOWN or (event.type==pg.MOUSEMOTION and event.buttons[0]):
                        if self.rect.collidepoint(event.pos):self.getCursorPos(event.pos)
                if event.type==pg.KEYDOWN and self.active:
                    self.iteration=0
                    self.showCursor=True
                    if event.key==pg.K_BACKSPACE:
                        self.cursorPos-=self.font.render(self.txt.split("\\")[0],True,self.txtColor).get_width()
                        txt=self.txt.split("\\")
                        self.txt=f"{txt[0][:-1]}\\{txt[1]}"
                        self.cursorPos+=self.font.render(self.txt.split("\\")[0],True,self.txtColor).get_width()
                    elif event.key==pg.K_DELETE:
                        self.cursorPos-=self.font.render(self.txt.split("\\")[0],True,self.txtColor).get_width()
                        txt=self.txt.split("\\")
                        self.txt=f"{txt[0]}\\{txt[1][1:]}"
                        self.cursorPos+=self.font.render(self.txt.split("\\")[0],True,self.txtColor).get_width()
                    elif event.key==pg.K_LEFT:
                        self.cursorPos-=self.font.render(self.txt.split("\\")[0],True,self.txtColor).get_width()
                        txt=self.txt.split("\\")
                        self.txt=f"{txt[0][:-1]}\\{txt[0][-1:]}{txt[1]}"
                        self.cursorPos+=self.font.render(self.txt.split("\\")[0],True,self.txtColor).get_width()
                    elif event.key==pg.K_RIGHT:
                        self.cursorPos-=self.font.render(self.txt.split("\\")[0],True,self.txtColor).get_width()
                        txt=self.txt.split("\\")
                        self.txt=f"{txt[0]}{txt[1][:1]}\\{txt[1][1:]}"
                        self.cursorPos+=self.font.render(self.txt.split("\\")[0],True,self.txtColor).get_width()
                    elif event.key==pg.K_RETURN:
                        self.active=False # sinon on désactive
                        pg.key.stop_text_input() # et on désactive la saisie
                    else:
                        self.cursorPos-=self.font.render(self.txt.split("\\")[0],True,self.txtColor).get_width()
                        txt=self.txt.split("\\")
                        self.txt=f"{txt[0]}{event.unicode}\\{txt[1]}"
                        self.cursorPos+=self.font.render(self.txt.split("\\")[0],True,self.txtColor).get_width()
        self.construct() # on construit l'entrée texte
        self.surface.blit(self.entry,self.pos) # on la place

    def getActive(self):return self.active

    def getText(self):
        txt=self.txt.split("\\")[0]+self.txt.split("\\")[1] # recompose le texte
        return txt


    def construct(self):
        self.entry=pg.Surface(self.size)
        if self.colorbg[0] is not None: self.entry.fill(self.colorbg[0])
        else: self.entry.set_colorkey((0,0,0))
        if self.active:
            if self.colorbg[1] is not None: self.entry.fill(self.colorbg[1])
        if self.colorUnder is not None:pg.draw.rect(self.entry,self.colorUnder,(0,0,self.size[0],self.size[1]),self.underWidth)
        render=pg.Surface((self.size[0]-self.underWidth*2,self.size[1]-self.underWidth*2))
        render.set_colorkey((0,0,0))
        if self.cursorPos<0:self.cursorPos=0
        if self.cursorPos>render.get_width():self.cursorPos=render.get_width()
        if self.showCursor:pg.draw.line(render,self.txtColor,(self.cursorPos,3),(self.cursorPos,render.get_height()-3),3)
        txt=self.txt.split("\\")
        size=self.font.render(txt[0],True,self.txtColor).get_size()
        render.blit(
            self.font.render(self.getText(),True,self.txtColor),
            (self.cursorPos-size[0],(render.get_height()-size[1])/2)
        )
        self.entry.blit(render,(self.underWidth,self.underWidth))