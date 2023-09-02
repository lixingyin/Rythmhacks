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
    color = (255, 255, 255)
    while True:
        pygame.draw.rect(screen, color, (40, 40, 60, 60))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q: 
                    print("The Q button was pressed")
                    color = (255, 0, 0)
                elif event.key == pygame.K_w:
                    print("The W button was pressed")
                elif event.key == pygame.K_e:
                    print("The E button was pressed")
                elif event.key == pygame.K_r:
                    print("The R button was pressed")
                elif event.key == pygame.K_t:
                    print("The T button was pressed")
                elif event.key == pygame.K_y:
                    print("The Y button was pressed")
                elif event.key == pygame.K_u:
                    print("The U button was pressed")
                elif event.key == pygame.K_i:
                    print("The I button was pressed")
                elif event.key == pygame.K_o:
                    print("The O button was pressed")
                elif event.key == pygame.K_p:
                    print("The P button was pressed")
                elif event.key == pygame.K_a:
                    print("The A button was pressed")
                elif event.key == pygame.K_s:
                    print("The S button was pressed")
                elif event.key == pygame.K_d:
                    print("The D button was pressed")
                elif event.key == pygame.K_f:
                    print("The F button was pressed")
                elif event.key == pygame.K_g:
                    print("The G button was pressed")
                elif event.key == pygame.K_h:
                    print("The H button was pressed")
                elif event.key == pygame.K_j:
                    print("The J button was pressed")
                elif event.key == pygame.K_k:
                    print("The K button was pressed")
                elif event.key == pygame.K_l:
                    print("The L button was pressed")
                elif event.key == pygame.K_z:
                    print("The Z button was pressed")
                elif event.key == pygame.K_x:
                    print("The X button was pressed")
                elif event.key == pygame.K_c:
                    print("The C button was pressed")
                elif event.key == pygame.K_v:
                    print("The V button was pressed")
                elif event.key == pygame.K_b:
                    print("The B button was pressed")
                elif event.key == pygame.K_n:
                    print("The N button was pressed")
                elif event.key == pygame.K_m:
                    print("The M button was pressed")
            if event.type == QUIT:
                pygame.quit()
def game_play():
    pass

while True:
    if introScreen == True:
        main_menu()

    elif introScreen == False:
        game_play()

