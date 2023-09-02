##main
import pygame, sys
import random
from pygame.locals import QUIT
from pygame import mixer
from wonderwords import RandomSentence
import time
import os




pygame.init()
clock = pygame.time.Clock()
width = 1000
height = 750
screen = pygame.display.set_mode((width, height))
black = (0, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
s = RandomSentence()

punchGuyStanding = pygame.image.load("https://ibb.co/GkQ6T23")
punchGuyRight = pygame.image.load("https://ibb.co/QKDwk1b")
punchGuyLeft = pygame.image.load("https://ibb.co/fvPd4M4")

bg = pygame.image.load("./image/background.png").convert()

need_sen = True
chars = []
typed_chars = []
keys_pressed = 0
keys_right = 0
keys_wrong = 0
cur_key = ""
done = True

gameClock = 0
elapsedTime = 0
startTime = 0

sentences = ['subscribe to yogogiddap', 'matthew yu can bench three fifteen', 'lalalalalalala', 'li xing yin is a guy. tha', "asejfeihfghksdfhjgestrytysdfggsdf", "I don\’t respect anybody who can\’t tell the difference between Pepsi and Coke."]

def calculateDamage(speed, accuracy):
    damage = (200/speed**2)*(accuracy/10)
    return damage

def create_sentence():
    sen1 = s.simple_sentence()
    sen2 = s.bare_bone_sentence()
    sen = sen1 + " " + sen2
    return sen.lower()


class button:
    def __init__(self, color, x, y, width, height, text=""):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, screen, outline=None):
        # Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(
                screen,
                outline,
                (self.x - 2, self.y - 2, self.width + 4, self.height + 4),
                0,
            )

        pygame.draw.rect(
            screen, self.color, (self.x, self.y, self.width, self.height), 0
        )

        if self.text != "":
            font = pygame.font.SysFont("comicsans", 60)
            text = font.render(self.text, 1, (0, 0, 0))
            screen.blit(
                text,
                (
                    self.x + (self.width / 2 - text.get_width() / 2),
                    self.y + (self.height / 2 - text.get_height() / 2),
                ),
            )

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False


start_button = button((150, 43, 56), (width / 2) - 175, 450, 350, 100, "Start Game")
end_button = button((150, 43, 56), (width / 2) - 175, 600, 350, 100, "Quit")

font = pygame.font.Font("freesansbold.ttf", 30)
x = 150
y = 641


def main_game(need_sen, done, keys_right, keys_wrong, typed_chars, chars,startTime):
    screen.fill((0, 0, 0))
    pygame.display.flip()
    gameClock = 0
    while True:
        elapsedTime = time.time() - startTime
        if elapsedTime >= 1:
            gameClock = gameClock + 1
            startTime = time.time()
        if need_sen == True:
            sentence = random.choice(sentences)
            for char in sentence:
                chars.append(char)
            need_sen = False

        text0 = font.render(sentence, True, black, (132, 206, 235))
        textRect0 = text0.get_rect()
        textRect0.center = (width // 2, height - 125)
        screen.fill((135, 206, 235)) #load backgrund colour
        screen.blit(text0, textRect0)
        screen.blit(bg, (0, 0)) #load background image
        timetext = font.render(str(gameClock), True, black, (132,206, 235))
        timetextrect = timetext.get_rect()
        screen.blit(timetext, timetextrect)
        if done:
            underline = pygame.Rect(
                textRect0.bottomleft[0], textRect0.bottomleft[1] - 2, 10, 5
            )
            done = False
        else:
            underline = pygame.Rect(underline.x, underline.y, 10, 5)

        pygame.draw.line(screen, black, (0, 562.5), (1000, 562.5), 3)
        pygame.draw.rect(screen, (128, 128, 128), underline)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                print(chars)
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                keys = event.key

                if keys == pygame.K_a:
                    cur_key = "a"
                if keys == pygame.K_b:
                    cur_key = "b"
                if keys == pygame.K_c:
                    cur_key = "c"
                if keys == pygame.K_d:
                    cur_key = "d"
                if keys == pygame.K_e:
                    cur_key = "e"
                if keys == pygame.K_f:
                    cur_key = "f"
                if keys == pygame.K_g:
                    cur_key = "g"
                if keys == pygame.K_h:
                    cur_key = "h"
                if keys == pygame.K_i:
                    cur_key = "i"
                if keys == pygame.K_j:
                    cur_key = "j"
                if keys == pygame.K_k:
                    cur_key = "k"
                if keys == pygame.K_l:
                    cur_key = "l"
                if keys == pygame.K_m:
                    cur_key = "m"
                if keys == pygame.K_n:
                    cur_key = "n"
                if keys == pygame.K_o:
                    cur_key = "o"
                if keys == pygame.K_p:
                    cur_key = "p"
                if keys == pygame.K_q:
                    cur_key = "q"
                if keys == pygame.K_r:
                    cur_key = "r"
                if keys == pygame.K_s:
                    cur_key = "s"
                if keys == pygame.K_t:
                    cur_key = "t"
                if keys == pygame.K_u:
                    cur_key = "u"
                if keys == pygame.K_v:
                    cur_key = "v"
                if keys == pygame.K_w:
                    cur_key = "w"
                if keys == pygame.K_x:
                    cur_key = "x"
                if keys == pygame.K_y:
                    cur_key = "y"
                if keys == pygame.K_z:
                    cur_key = "z"
                if keys == pygame.K_PERIOD:
                    cur_key = "."
                if keys == pygame.K_MINUS:
                    cur_key = "-"
                if keys == pygame.K_SPACE:
                    cur_key = " "
                if (keys == pygame.K_RETURN) and (keys_right+1 == len(chars)):
                    done = True

                elif cur_key == chars[keys_right] and keys_right != len(chars)-1:
                    if chars[keys_right + 1] == 'l' or chars[keys_right + 1] == "t" or chars[keys_right + 1] == "i" or chars[keys_right + 1] == "o" or chars[keys_right + 1] == " ":
                        underline.x += 12
                        keys_right += 1
                    elif chars[keys_right + 1] == "c" or chars[keys_right + 1] == "d" or chars[keys_right + 1] == "j" or chars[keys_right + 1] == "q":
                        underline.x += 15
                        keys_right += 1
                    else:
                        keys_right += 1
                        underline.x += 16
                    typed_chars.append(cur_key)

                else:
                    keys_wrong += 1

                


            if done:
                accuracy = (round((keys_right/(keys_right + keys_wrong) ) * 100))
                print("accuracy",accuracy)
                print("Speed =",len(chars),"/",gameClock)
                damage = calculateDamage(gameClock,accuracy)
                print('Damage',damage)
                chars.clear()
                typed_chars.clear()           
                keys_right = 0
                keys_wrong = 0
                need_sen = True
                gameClock = 0
        pygame.display.update()


# Next steps, find time and make user know when they get smth right, then set up hte turn based stuff

def animation():
    pass    

def main_menu():
    while True:
        pygame.display.update()
        screen.fill((202, 228, 241))
        start_button.draw(screen, (0, 0, 0))
        end_button.draw(screen, (0, 0, 0))

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                startTime = time.time()
                main_game(need_sen, done, keys_right, keys_wrong, typed_chars, chars,startTime)
                if end_button.isOver(pos):
                    pygame.quit()

main_menu() 

# # importing required library
# import pygame

# # activate the pygame library .
# pygame.init()
# X = 600
# Y = 600

# # create the display surface object
# # of specific dimension..e(X, Y).
# scrn = pygame.display.set_mode((X, Y))

# # set the pygame window name
# pygame.display.set_caption('image')

# # create a surface object, image is drawn on it.

# # Using blit to copy content from one surface to other
# scrn.blit(imp, (0, 0))

# # paint screen one time
# pygame.display.flip()
# status = True
# while (status):

# # iterate over the list of Event objects
# # that was returned by pygame.event.get() method.
# 	for i in pygame.event.get():

# 		# if event object type is QUIT
# 		# then quitting the pygame
# 		# and program both.
# 		if i.type == pygame.QUIT:
# 			status = False

# # deactivates the pygame library
# pygame.quit()
