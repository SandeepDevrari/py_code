##Final Project
import pygame as pg,random
from pygame.locals import *
class Project_Main:
    def __init__(self):
        pg.init();
        self.dragon_velocity=10;
        self.maryo_velocity=2
        self.CANVAS_WIDTH,self.CANVAS_HEIGHT=1200,600;
        self.cactus_x,self.cactus_y,self.cactus_width,self.cactus_height=-600,-100,1200,200;
        self.fire_bricks_x,self.fire_bricks_y,self.fire_bricks_width,self.fire_bricks_height=-600,300,1200,200;
        self.dragon_x,self.dragon_y,self.dragon_width,self.dragon_height=1050,250,100,86;
        self.maryo_x,self.maryo_y,self.maryo_width,self.maryo_height=50,250,50,96;
        self.BLACK=(0,0,0);
        self.done=False;
        self.fun=False;
        self.fire_list=pg.sprite.Group();
        self.direction='D';
        self.canvas=pg.display.set_mode((self.CANVAS_WIDTH,self.CANVAS_HEIGHT));
        pg.display.set_caption("Maryo");
        self.canvas.fill(self.BLACK);
        self.extra_fun();
        self.dragon_fun()
        self.maryo_fun();
        self.fla1=False;
        self.fla2=False;
        ##x,y=self.dragon_rect.centerx,self.dragon_rect.centery
        ##self.flame=Flame(x,y);
        pg.mixer.music.load('mario_theme.wav');
        pg.mixer.music.play(-1);
        self.die=pg.mixer.Sound('mario_dies.wav');
        self.time_pro=pg.time.Clock();
        ##print(self.dragon_rect.top);
        while not self.done:
            for event in pg.event.get():
                if event.type==QUIT:
                    self.done=True;
                if event.type==KEYDOWN and not self.fun:
                    if event.key==K_UP:
                        if self.maryo_rect.top>self.cactus_rect.bottom+50:
                            self.maryo_rect.centery-=30;
                            self.canvas.fill(self.BLACK);
                            self.canvas.blit(self.cactus,(self.cactus_rect.centerx,self.cactus_rect.centery,self.cactus_rect.width,self.cactus_rect.height));
                            self.canvas.blit(self.fire_bricks,(self.fire_bricks_rect.centerx,self.fire_bricks_rect.centery,self.fire_bricks_rect.width,self.fire_bricks_rect.height));
                            self.canvas.blit(self.maryo,(self.maryo_rect.centerx,self.maryo_rect.centery,self.maryo_rect.width,self.maryo_rect.height));
                        else:
                            self.fun=True;
                            pg.mixer.music.stop();
                            self.die.play(1);
                            ##print("STOPing");
                    elif event.key==K_DOWN:
                        if self.maryo_rect.bottom<self.fire_bricks_rect.top+85:
                            self.maryo_rect.centery+=30;
                            self.canvas.fill(self.BLACK);
                            self.canvas.blit(self.cactus,(self.cactus_rect.centerx,self.cactus_rect.centery,self.cactus_rect.width,self.cactus_rect.height));
                            self.canvas.blit(self.fire_bricks,(self.fire_bricks_rect.centerx,self.fire_bricks_rect.centery,self.fire_bricks_rect.width,self.fire_bricks_rect.height));
                            self.canvas.blit(self.maryo,(self.maryo_rect.centerx,self.maryo_rect.centery,self.maryo_rect.width,self.maryo_rect.height));
                        else:
                            self.fun=True;
                            pg.mixer.music.stop();
                            self.die.play(1);
                            ##print("STOPing");
            self.canvas.fill(self.BLACK);
            self.canvas.blit(self.cactus,(self.cactus_rect.centerx,self.cactus_rect.centery,self.cactus_rect.width,self.cactus_rect.height));
            self.canvas.blit(self.fire_bricks,(self.fire_bricks_rect.centerx,self.fire_bricks_rect.centery,self.fire_bricks_rect.width,self.fire_bricks_rect.height));
            ##self.canvas.blit(self.maryo,(self.maryo_rect.centerx,self.maryo_rect.centery,self.maryo_rect.width,self.maryo_rect.height));
            self.maryo_move();
            self.dragon_move();
            if self.fla1 or self.fla2:
                if self.flame1.rect.left==self.maryo_rect.right:##centerx and self.flame1.rect.centery==self.maryo_rect.centery:
                    self.fun=True;
                    pg.mixer.music.stop();
                    self.die.play(1);
                if self.fla2:
                    if self.flame2.rect.x==self.maryo_rect.centerx and self.flame2.rect.y==self.maryo_rect.centery:
                        self.fun=True;
                        pg.mixer.music.stop();
                        self.die.play(1);
            ##print(self.dragon_rect.centery);
            pg.display.update();
        pg.quit();

    def extra_fun(self):
        self.cactus=pg.image.load("cactus_bricks.png");
        self.cactus.set_colorkey((255,255,255));
        self.cactus_rect=pg.Rect(self.cactus_x,self.cactus_y,self.cactus_width,self.cactus_height);
        #self.canvas.blit(self.cactus,(self.cactus_rect.centerx,self.cactus_rect.centery,self.cactus_rect.width,self.cactus_rect.height));
        self.fire_bricks=pg.image.load("fire_bricks.png");
        self.fire_bricks.set_colorkey((255,255,255));
        self.fire_bricks_rect=pg.Rect(self.fire_bricks_x,self.fire_bricks_y,self.fire_bricks_width,self.fire_bricks_height);
        #self.canvas.blit(self.fire_bricks,(self.fire_bricks_rect.centerx,self.fire_bricks_rect.centery,self.fire_bricks_rect.width,self.fire_bricks_rect.height));

    def dragon_fun(self):
        self.dragon_rect=pg.Rect(self.dragon_x,self.fire_bricks_rect.top,self.dragon_width,self.dragon_height);
        self.dragon=pg.image.load("dragon.png");
        self.dragon.set_colorkey((255,255,255));
        ##self.canvas.blit(self.dragon,(self.dragon_rect.centerx,self.dragon_rect.centery,self.dragon_rect.width,self.dragon_rect.height));
        
    def dragon_move(self):
        if self.direction=='D' and not self.fun:
            if self.dragon_rect.top<=self.cactus_rect.bottom+50:
                ##print("hell "+str(self.dragon_rect.top))
                ##print("you "+str(self.cactus_rect.bottom));
                self.direction='I';
                self.flame1=Flame(self.dragon_rect.centerx,self.dragon_rect.centery+20);
                self.fla1=True;
            else:
                pg.time.delay(20);
                self.canvas.blit(self.dragon,(self.dragon_rect.centerx,self.dragon_rect.centery,self.dragon_rect.width,self.dragon_rect.height));
                self.dragon_rect.centery=self.dragon_rect.centery-self.dragon_velocity;
        if self.direction=='I' and not self.fun:
            if self.dragon_rect.bottom>=self.fire_bricks_rect.top+85:
                self.direction='D';
                self.flame2=Flame(self.dragon_rect.centerx,self.dragon_rect.centery-10);
                self.fla2=True;
            else:
                pg.time.delay(20);
                self.canvas.blit(self.dragon,(self.dragon_rect.centerx,self.dragon_rect.centery,self.dragon_rect.width,self.dragon_rect.height));
                self.dragon_rect.centery=self.dragon_rect.centery+self.dragon_velocity;
        #fire=Flame();
        if self.fla1:
            self.flame1.flame_move(self.canvas);
        if self.fla2:
            self.flame2.flame_move(self.canvas);
        #fire.rect.x=self.dragon_rect.centerx;
        #fire.rect.y=self.dragon_rect.centery;
        #fire.rect.width=35;
        #fire.rect.height=22;
        #self.rect.x=self.dragon_rect.centerx;
        #self.rect.y=self.dragon_rect.centery;
        #self.rect.width=35;
        #self.rect.height=22;
        #self.canvas.blit(self.image,(self.rect.x,self.rect.y,self.rect.width,self.rect.height));
        ##self.fire_list.add(fire);
        ##self.fire_list.draw(self.canvas);
        ##self.canvas.blit(fire)
        ##height=self.fire_bricks_rect.top-self.cactus_rect.bottom;
        ##if self.dragon_rect.top>self.cactus_rect.bottom:
        ###if self.dragon_rect.top>self.fire_bricks_rect.top-self.cactus_rect.bottom:
        ##    #pg.time.delay(50);
        ##    self.dragon_rect.centery=self.dra21gon_rect.centery-self.velocity-5;
        ##    self.canvas.blit(self.dragon,(self.dragon_rect.centerx,self.dragon_rect.centery,self.dragon_rect.width,self.dragon_rect.height));
        ##elif self.dragon_rect.bottom<=self.fire_bricks_rect.top:
        ##    #pg.time.delay(50);
        ##    self.dragon_rect.centery=self.dragon_rect.centery+self.velocity-10;
        ##    self.canvas.blit(self.dragon,(self.dragon_rect.centerx,self.dragon_rect.centery,self.dragon_rect.width,self.dragon_rect.height));
    def maryo_fun(self):
        ##print(self.dragon_rect.centerx); 
        self.maryo=pg.image.load("maryo.png");
        self.maryo.set_colorkey((255,255,255));
        self.maryo_rect=pg.Rect(self.maryo_x,self.maryo_y,self.maryo_width,self.maryo_height);
        #self.canvas.blit(self.maryo,(self.maryo_rect.centerx,self.maryo_rect.centery,self.maryo_rect.width,self.maryo_rect.height));

    def maryo_move(self):
        if self.maryo_rect.bottom<self.fire_bricks_rect.top+85 and not self.fun:
            self.maryo_rect.centery+=self.maryo_velocity;
        else:
            self.fun=True;
            ##print("STOP");
        self.canvas.blit(self.maryo,(self.maryo_rect.centerx,self.maryo_rect.centery,self.maryo_rect.width,self.maryo_rect.height));

"""    def flame(self):
        self.image=pg.image.load("fireball.png");
        self.image.set_colorkey((255,255,255));
        self.image = pg.transform.scale(self.image, (20,20))
        self.rect=self.image.get_rect();
        self.rect.x=self.dragon_rect.centerx;
        self.rect.y=self.dragon_rect.centery;
        ##self.canvas.blit(self.image,self.rect);
        ##self.rect.x-=20;
        ##self.canvas.blit(self.image,self.rect);

    def flame_move(self):
        self.rect.x-=20;
        self.canvas.blit(self.image,self.rect);"""
class Flame(pg.sprite.Sprite):
    def __init__(self,dragon_centerx,dragon_centery):
        super().__init__();
        self.image=pg.image.load("fireball.png");
        self.image.set_colorkey((255,255,255));
        self.image = pg.transform.scale(self.image, (20,20))
        self.rect=self.image.get_rect();
        self.rect.x=dragon_centerx;
        self.rect.y=dragon_centery;
    def flame_move(self,canvas):
        self.rect.x-=33;
        canvas.blit(self.image,self.rect);
        ##if self.rect.x==0
        ##   return True;
project=Project_Main();