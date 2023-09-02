##main
import pygame, sys
import random
from pygame.locals import QUIT
from pygame import mixer

pygame.init()
clock = pygame.time.Clock()
width = 1000
height = 600
done = True
screen = pygame.display.set_mode((width, height))



    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()


pygame.quit()
