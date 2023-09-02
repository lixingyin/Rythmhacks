##main
import pygame, sys
import random
from pygame.locals import QUIT
from pygame import mixer

pygame.init()
clock = pygame.time.Clock()
width = 1000
height = 600
screen = pygame.display.set_mode((width, height))

introScreen = True
def main_menu():
    while True:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
def game_play():
    pass

while True:
    if introScreen == True:
        main_menu()

    elif introScreen == False:
        game_play()