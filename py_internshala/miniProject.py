##min Project on Python 3 using Pygame
##Simple GUI Program
import pygame as pg
from pygame.locals import *
class MiniProject:
    def __init__(self):
        pg.init()
        canvas=pg.display.set_mode((800,600))
        pg.display.set_caption("Mini Project")
        WHITE=(255,255,255)
        BLACK=(0,0,0)
        canvas.fill(WHITE)
        done=False
        area_x=400
        area_y=300
        clock_time=pg.time.Clock()
        txt_object=pg.font.SysFont('Calibri',14,True,False)
        txt=txt_object.render("x: "+str(area_x)+" y: "+str(area_y),True,BLACK)
        canvas.blit(txt,(3,3))
        ball=pg.image.load('ball.jpg').convert()
        canvas.blit(ball,(area_x,area_y,100,98))
        while not done:
            for event in pg.event.get():
                if event.type==KEYDOWN:
                    if event.key==K_UP and area_y>0:
                        area_y=area_y-10
                        canvas.fill(WHITE)
                        txt=txt_object.render("x: "+str(area_x)+" y: "+str(area_y),True,BLACK)
                        canvas.blit(txt,(3,3))
                        canvas.blit(ball,(area_x,area_y,100,98))
                    elif event.key==K_DOWN and area_y<600:
                        area_y=area_y+10
                        canvas.fill(WHITE)
                        txt=txt_object.render("x: "+str(area_x)+" y: "+str(area_y),True,BLACK)
                        canvas.blit(txt,(3,3))
                        canvas.blit(ball,(area_x,area_y,100,98))
                    elif event.key==K_RIGHT and area_x<800:
                        area_x=area_x+10
                        canvas.fill(WHITE)
                        txt=txt_object.render("x: "+str(area_x)+" y: "+str(area_y),True,BLACK)
                        canvas.blit(txt,(3,3))
                        canvas.blit(ball,(area_x,area_y,100,98))
                    elif event.key==K_LEFT and area_x>0:
                        area_x=area_x-10
                        canvas.fill(WHITE)
                        txt=txt_object.render("x: "+str(area_x)+" y: "+str(area_y),True,BLACK)
                        canvas.blit(txt,(3,3))
                        canvas.blit(ball,(area_x,area_y,100,98))
                if event.type==QUIT:
                    pg.quit()
                    done=True
            pg.display.update()
            clock_time.tick(30)
        pg.quit()

mini_object=MiniProject()