import pygame,sys
from pygame.locals import *
pygame.init()
DISPLAYSURF=pygame.display.set_mode((400,300),0,32)
pygame.display.set_caption('Hello Ji')
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()