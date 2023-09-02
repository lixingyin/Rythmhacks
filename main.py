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

while done:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    print("Move the character forwards")
                elif event.key == pygame.K_s:
                    print("Move the character backwards")
                elif event.key == pygame.K_a:
                    print("Move the character left")
                elif event.key == pygame.K_d:
                    print("Move the character right")
        if event.type == QUIT:
            pygame.quit()
