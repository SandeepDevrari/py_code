import pygame as pg, random
from pygame.locals import *
class Sprite_class:
    def __init__(self):
        pg.init();
        canvas=pg.display.set_mode((800,600));
        WHITE=(255,255,255);
        BLACK=(0,0,0);
        RED=(255,0,0);
        canvas.fill(WHITE);
        pg.display.set_caption("Sprite");
        block_list=pg.sprite.Group();
        sprite_list=pg.sprite.Group();
        for i in range(15):
            block=Sprite_Main(20,15,BLACK);
            block.rect.x=random.randrange(800);
            block.rect.y=random.randrange(5);
            block_list.add(block);
            sprite_list.add(block);
        player=Sprite_Main(20,15,RED);
        sprite_list.add(player);
        done=False;
        clock=pg.time.Clock();
        score=0;
        ##timer=pg.time.set_timer(50);
        while not done:
            for event in pg.event.get():
                if event.type==QUIT:
                    done=True;
            canvas.fill(WHITE);
            pos=pg.mouse.get_pos();
            player.rect.x=pos[0];
            player.rect.y=pos[1];
            block_hit_list=pg.sprite.spritecollide(player,block_list,True);
            for block in block_hit_list:
                score+=1;
                print(score);
            sprite_list.draw(canvas);
            clock.tick(30);
            pg.display.flip();
        pg.quit();

class Sprite_Main(pg.sprite.Sprite):
    def __init__(self,width,height,color):
        super().__init__();
        self.image=pg.Surface([width,height]);
        self.image.fill(color);
        self.rect=self.image.get_rect();
obj=Sprite_class();