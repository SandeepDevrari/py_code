import pygame,sys
from pygame.locals import *
pygame.init()
DISPLAYSURF=pygame.display.set_mode((500,500))
pygame.display.set_caption("testing")
DISPLAYSURF.fill((255,255,255))
pygame.draw.line(DISPLAYSURF,(0,0,0,100),(0,0),(500,0),5)
pygame.draw.line(DISPLAYSURF,(0,0,0,100),(500,0),(500,500),5)
pygame.draw.line(DISPLAYSURF,(0,0,0,100),(500,500),(0,500),5)
pygame.draw.line(DISPLAYSURF,(0,0,0,100),(0,500),(0,0),5)
pygame.draw.circle(DISPLAYSURF,(255,255,0,50),(250,250),240,0)
pygame.draw.circle(DISPLAYSURF,(55,55,55),(150,170),40,0)
pygame.draw.circle(DISPLAYSURF,(55,55,55),(350,170),40,0)
pygame.draw.rect(DISPLAYSURF,(55,55,55),(160,350,170,50),0)
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit(0)
    pygame.display.update()