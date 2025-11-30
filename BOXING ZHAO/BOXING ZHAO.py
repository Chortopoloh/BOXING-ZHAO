import pygame as pg
import os
import json as js
import random as rd
import copy 
os.chdir(os.path.dirname(os.path.abspath(__file__)))
with open("STATS.json", "r") as f:
    fdt = js.load(f)
fdtcopy = copy.deepcopy(fdt)

pg.init()

clock = pg.time.Clock()

debugg = False
if debugg:
    fdt["Prib"]["health"] = 1000
info = pg.display.Info()
scw = info.current_w
sch = info.current_h
screen = pg.display.set_mode((scw,sch))
font = pg.font.Font("fonts/Gameplay.ttf",45)
click_cooldown = [0]  # <--- THIS IS A GODDAMN LIST. WHYYYYYYYYYYYYY ‽‽‽
MAJORL = False
victory = False

player_cooldowns = {
    "Attack": 0,
    "Attack 2": 2,
    "Special": 3,
    "Super": 5}

#-----------------------SSSSPRRRRIIIITEESSSS do i even begin to organise this------------
menu1 = pg.transform.scale(pg.image.load("sprites/testmenu.png").convert_alpha(), (scw, (sch/3)+30))
dgmenu = pg.transform.scale(pg.image.load("sprites/testmenu.png").convert_alpha(), (scw, (sch/3)-100))
but1i = pg.transform.scale(pg.image.load("sprites/but1.png").convert_alpha(), (420, 140))
but2i = pg.transform.scale(pg.image.load("sprites/but2.png").convert_alpha(), (420, 140))
but3i = pg.transform.scale(pg.image.load("sprites/but3.png").convert_alpha(), (420, 140))
but4i = pg.transform.scale(pg.image.load("sprites/but4.png").convert_alpha(), (420, 140))

but1ih = pg.transform.scale(pg.image.load("sprites/but1h.png").convert_alpha(), (420, 140))
but2ih = pg.transform.scale(pg.image.load("sprites/but2h.png").convert_alpha(), (420, 140))
but3ih = pg.transform.scale(pg.image.load("sprites/but3h.png").convert_alpha(), (420, 140))
but4ih = pg.transform.scale(pg.image.load("sprites/but4h.png").convert_alpha(), (420, 140))

tamqnc = pg.transform.scale(pg.image.load("sprites/tamqnc.png").convert_alpha(), (scw, sch))
soapdaddy = pg.transform.scale(pg.image.load("sprites/soapdaddy.png").convert_alpha(), (scw, sch))
boxinlab = pg.transform.scale(pg.image.load("sprites/boxinlab.png").convert_alpha(), (scw, sch))
battleground = pg.transform.scale(pg.image.load("sprites/battleground.png").convert_alpha(), (scw, sch))
VICTORYY = pg.transform.scale(pg.image.load("sprites/VICTORY.png").convert_alpha(), (scw, sch))
LLL = pg.transform.scale(pg.image.load("sprites/LLL.png").convert_alpha(), (scw, sch))

exit = pg.transform.scale(pg.image.load("sprites/exit.png").convert_alpha(), (60, 60))
exith = pg.transform.scale(pg.image.load("sprites/exith.png").convert_alpha(), (60, 60))

boxindg = pg.transform.scale(pg.image.load("sprites/boxindg.png").convert_alpha(),(1024, 1440))
boxindgh = pg.transform.scale(pg.image.load("sprites/boxindgh.png").convert_alpha(),(1024, 1440))
tamdg = pg.transform.scale(pg.image.load("sprites/tamdg.png").convert_alpha(),(1024, 1440))
aucoindg = pg.transform.scale(pg.image.load("sprites/aucoindg.png").convert_alpha(),(1024, 1440))
#-----------ANIMATIONS????------------------------
box = pg.image.load("sprites/box.png").convert_alpha()
box = pg.transform.scale(box, (box.get_width()*0.75 + 16, box.get_height()*0.75 + 16))
#----- PRIBBY -------
priba1 = pg.image.load("animations/PRIBA1.png").convert_alpha()
priba1 = pg.transform.scale(priba1, (priba1.get_width()*0.75, priba1.get_height()*0.75))
priba2 = pg.image.load("animations/PRIBA2.png").convert_alpha()
priba2 = pg.transform.scale(priba2, (priba2.get_width()*0.75, priba2.get_height()*0.75))
pribspec = pg.image.load("animations/PRIBSPEC.png").convert_alpha()
pribspec = pg.transform.scale(pribspec, (pribspec.get_width()*0.75, pribspec.get_height()*0.75))
pribult = pg.image.load("animations/PRIBULT.png").convert_alpha()
pribult = pg.transform.scale(pribult, (pribult.get_width()*0.75, pribult.get_height()*0.75))

pribi = pg.image.load("animations/PRIBI.png").convert_alpha()
pribi = pg.transform.scale(pribi, (pribi.get_width()*0.75, pribi.get_height()*0.75))
#------ BOXIN ------ 
boxa1 = pg.image.load("animations/BOXA1.png").convert_alpha()
boxa1 = pg.transform.scale(boxa1, (boxa1.get_width()*0.75, boxa1.get_height()*0.75))
boxa2 = pg.image.load("animations/BOXA2.png").convert_alpha()
boxa2 = pg.transform.scale(boxa2, (boxa2.get_width()*0.75, boxa2.get_height()*0.75))
boxspec = pg.image.load("animations/BOXSPEC.png").convert_alpha()
boxspec = pg.transform.scale(boxspec, (boxspec.get_width()*0.75, boxspec.get_height()*0.75))
boxult = pg.image.load("animations/BOXULT.png").convert_alpha()
boxult = pg.transform.scale(boxult, (boxult.get_width()*0.75, boxult.get_height()*0.75))

boxi = pg.image.load("animations/BOXI.png").convert_alpha()
boxi = pg.transform.scale(boxi, (boxi.get_width()*0.75, boxi.get_height()*0.75))
#------- TAM ---------
tama1 = pg.image.load("animations/TAMA1.png").convert_alpha()
tama1 = pg.transform.scale(tama1, (tama1.get_width()*0.75, tama1.get_height()*0.75))
tama2 = pg.image.load("animations/TAMA2.png").convert_alpha()
tama2 = pg.transform.scale(tama2, (tama2.get_width()*0.75, tama2.get_height()*0.75))
tamspec = pg.image.load("animations/TAMSPEC.png").convert_alpha()
tamspec = pg.transform.scale(tamspec, (tamspec.get_width()*0.75, tamspec.get_height()*0.75))
tamult = pg.image.load("animations/TAMULT.png").convert_alpha()
tamult = pg.transform.scale(tamult, (tamult.get_width()*0.75, tamult.get_height()*0.75))

tami = pg.image.load("animations/TAMI.png").convert_alpha()
tami = pg.transform.scale(tami, (tami.get_width()*0.75, tami.get_height()*0.75))
#------- AUCOIN ---------
auca1 = pg.image.load("animations/AUCOINA1.png").convert_alpha()
auca1 = pg.transform.scale(auca1, (auca1.get_width()*0.75, auca1.get_height()*0.75))
auca2 = pg.image.load("animations/AUCOINA2.png").convert_alpha()
auca2 = pg.transform.scale(auca2, (auca2.get_width()*0.75, auca2.get_height()*0.75))
aucspec = pg.image.load("animations/AUCOINSPEC.png").convert_alpha()
aucspec = pg.transform.scale(aucspec, (aucspec.get_width()*0.75, aucspec.get_height()*0.75))
aucult = pg.image.load("animations/AUCOINULT.png").convert_alpha()
aucult = pg.transform.scale(aucult, (aucult.get_width()*0.75, aucult.get_height()*0.75))

auci = pg.image.load("animations/AUCOINI.png").convert_alpha()
auci = pg.transform.scale(auci, (auci.get_width()*0.75, auci.get_height()*0.75))
#====

turnn = 1
player = "Prib"
enemies = ["Tam", "Aucoin", "Boxin"]
enemy_index = 0
enemy = enemies[enemy_index]

pr_special_boost = 0
pr_boost = False

reflect_next_dmg = False
PA1 = PA2 = PA3 = PA4 = TA1 = TA2=TA3=TA4=AA1=AA2=AA3=AA4=BA1=BA2=BA3=BA4 = False

def change_scene():
    global current_index, current_scene
    current_scene.done = False
    current_index = (current_index + 1) % len(scenes)
    current_scene = scenes[current_index]
    pg.display.flip()
    return

def ExIt():
    pg.quit()

        

# ------------------------- CLASSES -------------------------
class Animation:
    def __init__(self, sprite_sheet, frame_width, frame_height, num_frames, speed, loop=True, flip = True):
        self.sheet = sprite_sheet
        self.frame_width = frame_width
        self.frame_height = frame_height
        self.num_frames = num_frames
        self.speed = speed  # frames per update
        self.loop = loop
        self.freeze = False
        self.flip = flip
        self.frames = self._slice_frames()
        self.current_frame = 0
        self.counter = 0  # counts updates
    def _slice_frames(self):
        frames = []
        for i in range(self.num_frames):
            rect = pg.Rect(i*self.frame_width, 0, self.frame_width, self.frame_height)
            frame = self.sheet.subsurface(rect).copy()
            if self.flip == True:
                frame = pg.transform.flip(frame, True, False)

            frames.append(frame)
        return frames
    def reset(self):
        self.current_frame = 0
        self.counter = 0
        self.freeze = False
    def update(self):
        if self.freeze:
            return
        self.counter += 0.1
        if self.counter >= self.speed:
            self.counter = 0
            self.current_frame += 1
            if self.current_frame >= self.num_frames:
                if self.loop:
                    self.current_frame = 0
                else:
                    self.current_frame = 0
                    if not self.loop:
                        self.freeze = True  # stay on frist frame

    def draw(self, surface, pos):
        surface.blit(self.frames[self.current_frame], pos)
#===---===---AnImAtIoNs---===---===#
prib_a1 = Animation(priba1, priba1.get_height(), priba1.get_height(), 95, 0.1, loop = False,flip = False)
prib_a2 = Animation(priba2, priba2.get_height(), priba2.get_height(), 20, 0.4, loop = False,flip = False)
prib_spec = Animation(pribspec, pribspec.get_height(), pribspec.get_height(), 200, 0.15, loop = False,flip = False)
prib_ult = Animation(pribult, pribult.get_height(), pribult.get_height(), 77, 0.1, loop = False,flip = False)

box_a1 = Animation(boxa1, boxa1.get_height(), boxa1.get_height(), int((boxa1.get_width()/boxa1.get_height())), 0.25, loop = False, flip = True)
box_a2 = Animation(boxa2, boxa2.get_height(), boxa2.get_height(), int((boxa2.get_width()/boxa2.get_height())), 0.4, loop = False, flip = True)
box_spec = Animation(boxspec, boxspec.get_height(), boxspec.get_height(), 17, 0.3, loop = False, flip = True)
box_ult = Animation(boxult, boxult.get_height(), boxult.get_height(), int((boxult.get_width()/boxult.get_height())), 0.3, loop = False, flip = True)

tam_a1 = Animation(tama1, tama1.get_height(), tama1.get_height(), int((tama1.get_width()/tama1.get_height())), 0.25, loop = False, flip = True)
tam_a2 = Animation(tama2, tama2.get_height(), tama2.get_height(), int((tama2.get_width()/tama2.get_height())), 0.15, loop = False, flip = False)
tam_spec = Animation(tamspec, tamspec.get_height(), tamspec.get_height(), int((tamspec.get_width()/tamspec.get_height())), 0.2, loop = False, flip = True)
tam_ult = Animation(tamult, tamult.get_height(), tamult.get_height(), int((tamult.get_width()/tamult.get_height())), 0.3, loop = False, flip = True)

auc_a1 = Animation(auca1, auca1.get_height(), auca1.get_height(), int((auca1.get_width()/auca1.get_height())), 0.2, loop = False, flip = True)
auc_a2 = Animation(auca2, auca2.get_height(), auca2.get_height(), int((auca2.get_width()/auca2.get_height())), 0.3, loop = False, flip = True)
auc_spec = Animation(aucspec, aucspec.get_height(), aucspec.get_height(), int((aucspec.get_width()/aucspec.get_height())), 0.3, loop = False, flip = True)
auc_ult = Animation(aucult, aucult.get_height(), aucult.get_height(), int((aucult.get_width()/aucult.get_height())), 0.2, loop = False, flip = True)
class Text:
    def __init__(self, pos, text, font, color):
        self.font = font
        self.text = text
        self.color = color
        self.pos = pos
        self.visible = False
        self.text_render()
    def text_render(self):
        self.surface = self.font.render(self.text, True, self.color)
        self.rect = self.surface.get_rect(center = self.pos)
    def set_text(self, text=None, color = None):
        if text:
            self.text = text
        if color:
            self.color = color
        self.text_render()
    def show(self, hide):
        if hide == "s":
            self.visible = True
        if hide == "h":
            self.visible = False
    def draw(self, screen):
        if self.visible:
            screen.blit(self.surface, self.rect)






class Button:
    def __init__(self,x,y,normal_img,hover_img,func=None):
        self.normal_img = normal_img
        self.hover_img = hover_img
        self.image = self.normal_img
        self.rect = self.image.get_rect(center=(x, y))
        self.action = func
    def update(self, mouse_pos, mouse_pressed):
        global click_cooldown
        global turnn, PA1, PA2, PA3, PA4
        if self.rect.collidepoint(mouse_pos):
            self.image = self.hover_img
            if self.action == ExIt:
                if mouse_pressed[0]:
                    self.action()
                    click_cooldown[0] = 10
                    return True
            if turnn % 2 != 0 and self.action:
                if not (PA1 or PA2 or PA3 or PA4):
                    if mouse_pressed[0] and click_cooldown[0] == 0:
                        if self.action:
                            self.action()
                            click_cooldown[0] = 10
                            return True
        else:
            self.image = self.normal_img
    def draw(self, screen):
        if running:
            screen.blit(self.image, self.rect)

class Scene:
    def __init__(self, screen):
        self.screen = screen
        self.done = False
    def handle_event(self, event):
        pass
    def update(self):
        pass
    def draw(self):
        pass

menu1locx = 0
menu1locy = sch - (sch/3) - 30
but1locx = scw/2 + scw/4
but1locy = sch/2 + sch/4 
but2locx = but1locx
but2locy = but1locy + 150
but3locx = scw/2 - scw/4
but3locy = sch/2 + sch/4
but4locx = but3locx
but4locy = but3locy + 150

TamDialogue = []
TamDialogue.append(Text((scw/2, menu1locy + (sch/3)-110), "WELCOME TO BOXING ZHAO! (click mouse)", font,(255,255,20)))
TamDialogue.append(Text((scw/2, menu1locy + (sch/3)-110), "You're here for the title of 1A GOAT? Well then...", font,(255,255,20)))
TamDialogue.append(Text((scw/2, menu1locy + (sch/3)-110), "You shall fight the three deadly professors!", font,(255,255,20)))
TamDialogue.append(Text((scw/2, menu1locy + (sch/3)-110), "Each one more powerful. One after another, no respawns!!!", font,(255,255,20)))
TamDialogue.append(Text((scw/2, menu1locy + (sch/3)-110), "(we do allow calculators)", font,(255,255,20)))
TamDialogue.append(Text((scw/2, menu1locy + (sch/3)-110), "A few things to know:", font,(255,255,20)))
TamDialogue.append(Text((scw/2, menu1locy + (sch/3)-110), "Attacks have cooldowns. Bet you didn't know that.", font,(255,255,20)))
TamDialogue.append(Text((scw/2, menu1locy + (sch/3)-110), "Attack - 0, Attack 2 - 2, Special - 3, Super - 5", font,(255,255,20)))
TamDialogue.append(Text((scw/2, menu1locy + (sch/3)-110), "The first two attacks just deal some damage.", font,(255,255,20)))
TamDialogue.append(Text((scw/2, menu1locy + (sch/3)-110), "But Special is cool! It heals you and gives a dmg boost!", font,(255,255,20)))
TamDialogue.append(Text((scw/2, menu1locy + (sch/3)-110), "Your super attack... Trust me - use it when you're desperate.", font,(255,255,20)))
TamDialogue.append(Text((scw/2, menu1locy + (sch/3)-110), "Be careful of your cooldowns, plan ahead and stay balanced!", font,(255,255,20)))
TamDialogue.append(Text((scw/2, menu1locy + (sch/3)-110), "............", font,(255,255,20)))
TamDialogue.append(Text((scw/2, menu1locy + (sch/3)-110), "I happen to be the first one you'll face.", font,(255,255,20)))
TamDialogue.append(Text((scw/2, menu1locy + (sch/3)-110), "I'd wish you luck, but you're about to be linearly regressed...", font,(255,255,20)))
TamDialogue.append(Text((scw/2, menu1locy + (sch/3)-110), "...and HEAVILY pressured 😠", font,(255,255,20)))

class SceneOne(Scene):
    def __init__(self, screen):
        super().__init__(screen)
        self.dgindex = 0
    def draw(self):
        global TamDialogue
        self.screen.blit(tamqnc,(0,0))
        self.screen.blit(tamdg,(0,0))
        exith.draw(screen)
        self.screen.blit(dgmenu, (menu1locx, menu1locy+130))
        if self.dgindex < len(TamDialogue):
            TamDialogue[self.dgindex].show("s")
            TamDialogue[self.dgindex].draw(screen)
    def handle_event(self, event):
        global current_scene, current_index
        if event.type == pg.KEYDOWN and event.key == pg.K_s:
            self.done = True
        if event.type == pg.MOUSEBUTTONDOWN:
            self.dgindex +=1
            if self.dgindex == len(TamDialogue):
                current_index = 3
                current_scene = SceneBattle(screen)
                self.done = True
    def update(self):
        exith.update(mouse_pos, mouse_pressed)
        
AucoinDialogue = []
AucoinDialogue.append(Text((scw/2, menu1locy + (sch/3)-110), "You! How dare you defeat the great Michael Tam!", font,(255, 145, 248)))
AucoinDialogue.append(Text((scw/2, menu1locy + (sch/3)-110), "You're not worthy to be GOAT of 1A!", font,(255, 145, 248)))
AucoinDialogue.append(Text((scw/2, menu1locy + (sch/3)-110), "My soap levels are overwhelming.", font,(255, 145, 248)))
AucoinDialogue.append(Text((scw/2, menu1locy + (sch/3)-110), "YOU WILL BE LEFT SQUEAKY CLEAN", font,(255, 145, 248)))
class SceneTwo(Scene):
    def __init__(self, screen):
        super().__init__(screen)
        self.dgindex = 0
    def draw(self):
        self.screen.blit(soapdaddy,(0,0))
        self.screen.blit(aucoindg,(0,0))
        exith.draw(screen)
        self.screen.blit(dgmenu, (menu1locx, menu1locy+130))
        if self.dgindex < len(AucoinDialogue):
            AucoinDialogue[self.dgindex].show("s")
            AucoinDialogue[self.dgindex].draw(screen)
    def handle_event(self, event):
        global current_index, current_scene
        if event.type == pg.KEYDOWN and event.key == pg.K_s:
            self.done = True
        if event.type == pg.MOUSEBUTTONDOWN:
            self.dgindex +=1
            if self.dgindex == len(AucoinDialogue):
                current_index = 3
                current_scene = SceneBattle(screen)
                self.done = True
    def update(self):
        exith.update(mouse_pos, mouse_pressed)
BoxinDialogue = []
BoxinDialogue.append(Text((scw/2, menu1locy + (sch/3)-110), "Good Morning. I have expected you.", font,(255, 162, 156)))
BoxinDialogue.append(Text((scw/2, menu1locy + (sch/3)-110), "You have defeated Aucoin? A commendable achievement.", font,(255, 162, 156)))
BoxinDialogue.append(Text((scw/2, menu1locy + (sch/3)-110), "But but your path ends here, Prib.", font,(255, 162, 156)))
BoxinDialogue.append(Text((scw/2, menu1locy + (sch/3)-110), "Time to shift your equillibrium straight into Laurier!", font,(255, 162, 156)))

class SceneThree(Scene):
    def __init__(self, screen):
        super().__init__(screen)
        self.dgindex = 0
    def draw(self):
        self.screen.blit(boxinlab,(0,0))
        self.screen.blit(boxindg,(0,0))
        exith.draw(screen)
        self.screen.blit(dgmenu, (menu1locx, menu1locy+130))
        if self.dgindex < len(BoxinDialogue):
            BoxinDialogue[self.dgindex].show("s")
            BoxinDialogue[self.dgindex].draw(screen)
    def handle_event(self, event):
        global current_index, current_scene
        if event.type == pg.KEYDOWN and event.key == pg.K_s:
            self.done = True
        if event.type == pg.MOUSEBUTTONDOWN:
            self.dgindex +=1
            if self.dgindex == len(BoxinDialogue):
                current_index = 3
                current_scene = SceneBattle(screen)
                self.done = True

class SceneBattle(Scene):
    def draw(self):
        global PA1, PA2, PA3, PA4, BA1,BA2,BA3,BA4,TA1,TA2,TA3,TA4,AA1,AA2,AA3,AA4, turnn, reflect_next_dmg
        self.screen.blit(battleground, (0,0))
        self.screen.blit(box, (-16 + scw/5,-16 + sch/3))
        self.screen.blit(box, (16 -box.get_width() + scw - scw/5,-16 + sch/3))
        if PA2:
            prib_a2.draw(screen, (scw/5,sch/3))
            if prib_a2.freeze == True:
                PA2 = False
                turnn += 1
        elif PA1:
            prib_a1.draw(screen, (scw/5,sch/3))
            if prib_a1.freeze == True:
                PA1 = False
                turnn += 1
        elif PA3:
            prib_spec.draw(screen, (scw/5,sch/3))
            if prib_spec.freeze == True:
                PA3 = False
                turnn += 1
        elif PA4:
            prib_ult.draw(screen, (scw/5,sch/3))
            if prib_ult.freeze == True:
                PA4 = False
                turnn += 1
        elif TA4:
            tam_ult.draw(screen, (scw/5,sch/3))
            if tam_ult.freeze == True:
                TA4 = False
                fdt["Prib"]["health"] -= fdt[enemy]["attacks"]["Super"]["damage"]
                turnn += 1
        else:
            self.screen.blit(pribi, (scw/5,sch/3))
        if enemy == "Boxin":
            if BA1:
                box_a1.draw(screen, (scw - scw/5 - 288,sch/3))
                if box_a1.freeze == True:
                    BA1 = False
                    fdt["Prib"]["health"] -= fdt[enemy]["attacks"]["Attack"]["damage"]
                    turnn += 1
            elif BA2:
                box_a2.draw(screen, (scw - scw/5 - 288,sch/3))
                if box_a2.freeze == True:
                    BA2 = False
                    fdt["Prib"]["health"] -= fdt[enemy]["attacks"]["Attack 2"]["damage"]
                    turnn += 1
            elif BA3:
                box_spec.draw(screen, (scw - scw/5 - 288,sch/3))
                if box_spec.freeze == True:
                    BA3 = False

                    fdt[enemy]["health"] += fdt[enemy]["attacks"]["Special"]["heal"]
                    fdt["Prib"]["health"] -= fdt[enemy]["attacks"]["Special"]["damage"]

                    turnn += 1
            elif BA4:
                box_ult.draw(screen, (scw - scw/5 - 288,sch/3))
                if box_ult.freeze == True:
                    BA4 = False

                    reflect_next_dmg = True

                    turnn += 1
            else:
                self.screen.blit(boxi, (scw - scw/5 - 288,sch/3))
        if enemy == "Tam":
            if TA1:
                tam_a1.draw(screen, (scw - scw/5 - 288,sch/3))
                if tam_a1.freeze == True:
                    TA1 = False
                    fdt["Prib"]["health"] -= fdt[enemy]["attacks"]["Attack"]["damage"]
                    turnn += 1
            elif TA2:
                tam_a2.draw(screen, (scw - scw/5 - 288,sch/3))
                if tam_a2.freeze == True:
                    TA2 = False
                    fdt["Prib"]["health"] -= fdt[enemy]["attacks"]["Attack 2"]["damage"]
                    turnn += 1
            elif TA3:
                tam_spec.draw(screen, (scw - scw/5 - 288,sch/3))
                if tam_spec.freeze == True:
                    TA3 = False
                    fdt["Prib"]["health"] -= fdt[enemy]["attacks"]["Special"]["damage"]
                    turnn += 1
            # elif TA4:
            else:
                self.screen.blit(tami, (scw - scw/5 - 288,sch/3))
        if enemy == "Aucoin":
            if AA1:
                auc_a1.draw(screen, (scw - scw/5 - 288,sch/3))
                if auc_a1.freeze == True:
                    AA1 = False
                    fdt["Prib"]["health"] -= fdt[enemy]["attacks"]["Attack"]["damage"]
                    turnn += 1
            elif AA2:
                auc_a2.draw(screen, (scw - scw/5 - 288,sch/3))
                if auc_a2.freeze == True:
                    AA2 = False
                    fdt["Prib"]["health"] -= fdt[enemy]["attacks"]["Attack 2"]["damage"]
                    turnn += 1
            elif AA3:
                auc_spec.draw(screen, (scw - scw/5 - 288,sch/3))
                if auc_spec.freeze == True:
                    AA3 = False
                    fdt[enemy]["health"] += fdt[enemy]["attacks"]["Special"]["heal"]
                    if fdt[enemy]["health"] > 150:
                        fdt[enemy]["health"] = fdtcopy[enemy]["health"]
                    turnn += 1
            elif AA4:
                auc_ult.draw(screen, (scw - scw/5 - 288,sch/3))
                if auc_ult.freeze == True:
                    AA4 = False

                    fdt["Prib"]["health"] -= fdt[enemy]["attacks"]["Super"]["damage"]
                    if fdt["Prib"]["health"] <= 30:
                        turnn += 2
                    else:
                        turnn += 1
            else:
                self.screen.blit(auci, (scw - scw/5 - 288,sch/3))
    def update(self):
        if PA2:
            prib_a2.update()
        elif PA1:
            prib_a1.update()
        elif PA3:
            prib_spec.update()
        elif PA4:
            prib_ult.update()

        if BA2:
            box_a2.update()
        elif BA1:
            box_a1.update()
        elif BA3:
            box_spec.update()
        elif BA4:
            box_ult.update()

        if TA2:
            tam_a2.update()
        elif TA1:
            tam_a1.update()
        elif TA3:
            tam_spec.update()
        elif TA4:
            tam_ult.update()
        
        if AA2:
            auc_a2.update()
        elif AA1:
            auc_a1.update()
        elif AA3:
            auc_spec.update()
        elif AA4:
            auc_ult.update()
    def handle_event(self, event):
        if event.type == pg.KEYDOWN and event.key == pg.K_s and debugg:
            self.done = True
class SceneVICTORY(Scene):
    def draw(self):
        self.screen.blit(VICTORYY, (0,0))
    def handle_event(self, event):
        if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            self.done = True
            pg.quit()
class SceneLOSS(Scene):
    def draw(self):
        self.screen.blit(LLL, (0,0))
    def handle_event(self, event):
        if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            self.done = True
            pg.quit()
scenes = [
    SceneOne(screen),
    SceneTwo(screen),
    SceneThree(screen),
    SceneBattle(screen),
]

current_index = 0
current_scene = scenes[current_index]

def PribAtt(attack):
    global pr_special_boost, pr_boost, reflect_next_dmg, current_scene, current_index, enemy_index, enemy, victory, turnn
    global PA1, PA2, PA3, PA4
    if isinstance(current_scene, SceneBattle):
        target = enemies[enemy_index]
        if debugg:
            print(fdt[target]["health"])

        if player_cooldowns[attack] > 0:
            if debugg:
                print(f"{attack} is on cooldown, {player_cooldowns[attack]} turns left")
            return

        if pr_boost and pr_special_boost == 0:
            fdt["Prib"]["attacks"]["Attack"]["damage"] -= 30
            fdt["Prib"]["attacks"]["Attack 2"]["damage"] -= 30
            fdt["Prib"]["attacks"]["Super"]["damage"] -= 30
            pr_boost = False
        if target in fdt and attack in fdt["Prib"]["attacks"]:
            if attack == "Attack":
                if pr_boost:
                    pr_special_boost -= 1
                fdt[target]["health"] -= fdt["Prib"]["attacks"]["Attack"]["damage"]
                if reflect_next_dmg:
                    if fdt["Prib"]["attacks"]["Attack"]["damage"] < fdt[enemy]["health"]:
                        fdt["Prib"]["health"] -= fdt["Prib"]["attacks"]["Attack"]["damage"]*0.7
                    reflect_next_dmg = False
                prib_a1.reset()
                PA1 = True
            if attack == "Attack 2":
                if pr_boost:
                    pr_special_boost -= 1
                fdt[target]["health"] -= fdt["Prib"]["attacks"]["Attack 2"]["damage"]
                if reflect_next_dmg:
                    if debugg:
                        print(reflect_next_dmg)
                    if fdt["Prib"]["attacks"]["Attack 2"]["damage"] < fdt[enemy]["health"]:
                        fdt["Prib"]["health"] -= fdt["Prib"]["attacks"]["Attack 2"]["damage"]*0.7
                    reflect_next_dmg = False
                prib_a2.reset()
                PA2 = True
            if attack == "Special":
                pr_boost = True
                pr_special_boost = fdtcopy["Prib"]["attacks"]["Special"]["duration"]
                fdt["Prib"]["health"] += fdt["Prib"]["attacks"]["Special"]["heal"]
                fdt["Prib"]["attacks"]["Attack"]["damage"] += 30
                fdt["Prib"]["attacks"]["Attack 2"]["damage"] += 30
                fdt["Prib"]["attacks"]["Super"]["damage"] += 30
                prib_spec.reset()
                PA3 = True
            if attack == "Super":
                if pr_boost:
                    pr_special_boost -= 1
                fdt[target]["health"] -= (fdt["Prib"]["attacks"]["Super"]["damage"]*(fdt[enemy]["health"]/fdt["Prib"]["health"]))
                if reflect_next_dmg:
                    if (fdt["Prib"]["attacks"]["Super"]["damage"]*(fdt[enemy]["health"]/fdt["Prib"]["health"])) < fdt[enemy]["health"]:
                        fdt["Prib"]["health"] -= (fdt["Prib"]["attacks"]["Super"]["damage"]*(fdt[enemy]["health"]/fdt["Prib"]["health"]))*0.7
                    reflect_next_dmg = False
                prib_ult.reset()
                PA4 = True
        player_cooldowns[attack] = fdtcopy["Prib"]["attacks"][attack]["recharge"]
        for atk in player_cooldowns:
            if player_cooldowns[atk] > 0:
                player_cooldowns[atk] -= 1

        if fdt[target]["health"] <= 0:
            PA1 = PA2 = PA3 = PA4 = False
            if turnn % 2 == 0:
                turnn += 1
            enemy_index += 1
            if enemy_index < len(enemies):
                    enemy = enemies[enemy_index]
                    if debugg:
                        print(f"--- Next Enemy is: {enemy} (Index {enemy_index}) ---")
                    if target == "Tam":
                        current_index = 1 
                        current_scene = scenes[current_index]
                        
                    elif target == "Aucoin":
                        current_index = 2
                        current_scene = scenes[current_index]
                        
            else: 
                    victory = True
                    print("BOXIN IS DEEEEEEAD")
            
def AiAtt1(fighter):
    global current_scene, turnn, BA1, TA1, AA1
    if isinstance(current_scene, SceneBattle):
        if fighter in fdt:
            if fighter == "Boxin":
                box_a1.reset()
                BA1 = True
            elif fighter == "Aucoin":
                auc_a1.reset()
                AA1 = True
            elif fighter == "Tam":
                tam_a1.reset()
                TA1 = True

def AiAtt2(fighter):
    global current_scene, turnn, BA2, TA2, AA2
    if isinstance(current_scene, SceneBattle):
        if fighter in fdt:
            if fighter == "Boxin":
                box_a2.reset()
                BA2 = True
            elif fighter == "Aucoin":
                auc_a2.reset()
                AA2 = True
            elif fighter == "Tam":
                tam_a2.reset()
                TA2 = True
def AiAtt3(fighter):
    global current_scene, turnn, AA3, BA3, TA3
    if isinstance(current_scene, SceneBattle):
        if fighter in fdt:
            if fighter == "Tam":
                tam_spec.reset()
                TA3 = True
            if fighter == "Aucoin":
                auc_spec.reset()
                AA3 = True
            if fighter == "Boxin":
                box_spec.reset()
                BA3 = True
def AiAttSup(fighter):
    global turnn, reflect_next_dmg, current_scene, AA4, BA4, TA4
    if isinstance(current_scene, SceneBattle):
        if fighter in fdt:
            if fighter == "Tam":
                tam_ult.reset()
                TA4 = True
            if fighter == "Aucoin":
                auc_ult.reset()
                AA4 = True
            if fighter == "Boxin":
                box_ult.reset()
                BA4 = True

def AiTurn(enemy):
    global turnn
    attacks = {AiAtt1: "Attack", AiAtt2: "Attack 2", AiAtt3: "Special", AiAttSup: "Super"}
    
    available_attacks = []
    for func, name in attacks.items():
        if fdt[enemy]["attacks"][name]["recharge"] == 0:
            available_attacks.append(func)
            
    if available_attacks:
        rrr = rd.choice(available_attacks) 
        attack_name = attacks[rrr]
        
        rrr(enemy)  #LAUNCH ATTAAAAAAAAC
        
        # eresetcooldown
        fdt[enemy]["attacks"][attack_name]["recharge"] = fdtcopy[enemy]["attacks"][attack_name]["recharge"]
        if debugg:
            print(f"{enemy} used {attack_name}")
            print(fdt["Prib"]["health"])
    else:
        turnn += 1 #in case i'm a damn imbecile and forgot an attack

    for atk in fdt[enemy]["attacks"].values():
        if atk["recharge"] > 0:
            atk["recharge"] -= 1

# ---------- BUTTONS / TEXTS ----------

enemy_hp_bar = (16 -box.get_width() + scw - scw/5, -66 + sch/3)
enemy_hp_bar_text= (enemy_hp_bar[0] + 65,enemy_hp_bar[1] - 20)
texts = []
texts.append(Text((but1locx,but1locy), "ATTACK 2", font,(255,255,0)))
texts.append(Text((but2locx,but2locy), "SUPER", font,(255,255,0)))
texts.append(Text((but3locx,but3locy), "ATTACK", font,(255,255,0)))
texts.append(Text((but4locx,but4locy), "SPECIAL", font,(255,255,0)))
texts.append(Text(enemy_hp_bar_text, str(enemy), font,(0,0,0)))

buttons = []
buttons.append(Button(but1locx, but1locy, but1i, but1ih, lambda: PribAtt("Attack 2")))
buttons.append(Button(but2locx, but2locy, but2i, but2ih, lambda: PribAtt("Super")))
buttons.append(Button(but3locx, but3locy, but3i, but3ih, lambda: PribAtt("Attack")))
buttons.append(Button(but4locx, but4locy, but4i, but4ih, lambda: PribAtt("Special")))
exith = Button(50,50,exit, exith, ExIt)
buttons.append(exith)
dialoguesprites = []
boxindgs = Button(scw/4,sch/2 + 100, boxindg, boxindgh)
dialoguesprites.append(boxindgs)



# ------------------- MAIN LOOP -------------------
running = True
while running:
    if click_cooldown[0] > 0:
        click_cooldown[0] -= 1

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN and event.key == pg.K_t and debugg:
            turnn += 1
        if event.type == pg.KEYDOWN and event.key == pg.K_v and debugg:
            victory = True
        if event.type == pg.KEYDOWN and event.key == pg.K_h and debugg:
            print(fdt[enemy]["health"])
        current_scene.handle_event(event)

    mouse_pos = pg.mouse.get_pos()
    mouse_pressed = pg.mouse.get_pressed()
    current_scene.update()
    current_scene.draw()

    if current_scene.done:
        current_scene.done = False
        current_index = (current_index + 1) % len(scenes)
        current_scene = scenes[current_index]
        if current_index == 3: 
            if turnn % 2 == 0:
                turnn += 1
            elif turnn % 2 != 0:
                # If it's already an odd number, we don't touch it.
                pass
    if turnn % 2 == 0 and isinstance(current_scene, SceneBattle) and not (BA1 or BA2 or BA3 or BA4 or TA1 or TA2 or TA3 or TA4 or AA1 or AA2 or AA3 or AA4):
        if debugg:
            print(f"DEBUG: Calling AiTurn for {enemy}, turnn={turnn}")
        AiTurn(enemy)
    if fdt["Prib"]["health"] <= 0 and not (BA1 or BA2 or BA3 or BA4 or TA1 or TA2 or TA3 or TA4 or AA1 or AA2 or AA3 or AA4):
        MAJORL = True

    if victory or MAJORL:
        exith.update(mouse_pos, mouse_pressed)
        exith.draw(screen)
    elif isinstance(current_scene, SceneBattle): #(16 -box.get_width() + scw - scw/5,-16 + sch/3)
        screen.blit(menu1, (menu1locx, menu1locy))
        pg.draw.rect(screen, (255,0,0),(scw/2 - 60, sch - sch/3 + 40, 120, int(fdt["Prib"]["health"])*1.25))
        for b in buttons:
            b.update(mouse_pos, mouse_pressed)
            b.draw(screen)
        pg.draw.rect(screen, (255,0,0),(16 -box.get_width() + scw - scw/5, -66 + sch/3, int(fdt[enemy]["health"])*2, 45))
        texts[4].set_text(str(enemy))
        for t in texts:
            t.text_render()
            t.show("s")
            t.draw(screen)
        exith.update(mouse_pos, mouse_pressed)
        exith.draw(screen)
    else:
        exith.update(mouse_pos, mouse_pressed)
        exith.draw(screen)
    

    if victory == True:
        current_scene = SceneVICTORY(screen)
    if MAJORL == True:
        current_scene = SceneLOSS(screen)

    pg.display.flip()
    clock.tick(60)
pg.quit()
