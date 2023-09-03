##main
import pygame, sys
import random
from pygame.locals import QUIT
from pygame import mixer
from wonderwords import RandomSentence
import time
import os
from pygame import mixer

# music
mixer.init()
mixer.music.load('xiexie.mp3')
mixer.music.set_volume(0.5)
mixer.music.play()

pygame.init()
clock = pygame.time.Clock()
width = 1000
height = 750
screen = pygame.display.set_mode((width, height), pygame.SRCALPHA)

# screen.set_colorkey((0, 0, 0))

black = (0, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
s = RandomSentence()

bg = pygame.image.load("./image/background.png").convert_alpha()
punchGuyStanding = pygame.image.load("./image/punchguy_right.png").convert_alpha()
punchGuyPunchLeft = pygame.image.load("./image/punch guy punching with left punch hand.png").convert_alpha()
punchGuyPunchRight = pygame.image.load("./image/punch guy punching with right punch hand.png").convert_alpha()
wizardLeft = pygame.image.load("./image/wizard_left.png").convert_alpha()

need_sen = True
chars = []
typed_chars = []
keys_pressed = 0
keys_right = 0
keys_wrong = 0
cur_key = ""
done = True
player = 1
guyX = 170
guyY = 130

gameClock = 0
elapsedTime = 0
startTime = 0
attack = False


sentences = ['do not subscribe to yogogiddap', 'matthew yu can bench three fifteen', 'lalalalalalala', 'lixing yin does not need his phone', "asejfeihfghksdfhjgestrytysdfggsdf", "jasmine xu", "when is the next hackathon", "alicehacks sucks", "gary is the most best xvi year old"]

def calculateDamage(speed, accuracy):
    damage = (200/speed**2)*(accuracy)
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
monofont = pygame.font.SysFont("lucidasans.ttf", 45)
font2 = pygame.font.Font("freesansbold.ttf", 50)
x = 150
y = 641

def main_game(need_sen, done, keys_right, keys_wrong, typed_chars, chars,startTime, attack, player, cur_key=''):
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

        text0 = monofont.render(sentence, True, black, (132, 206, 235))
        textRect0 = text0.get_rect()
        textRect0.center = (width // 2, height - 125)
        screen.fill((135, 206, 235)) #load background colour
        screen.blit(text0, textRect0)
        screen.blit(bg, (0, 0)) #load background image
        if attack == False:
            guy = screen.blit(punchGuyStanding, (guyX, guyY))
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('HIYAH.mp3'))

        elif attack == True:
            # guy.kill()
            # guy.set_alpha(0)
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('HIYAH.mp3'))
            punchGuy = screen.blit(punchGuyPunchRight, (guyX, guyY))
        # time.sleep(3)

            
        screen.blit(wizardLeft, (550, 125))
        timetext = font2.render(str(gameClock), True, black, ( 34, 126, 145))
        timetextrect = timetext.get_rect()
        timetextrect.center = (width //2, 50 )
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
                screen.blit(punchGuyPunchLeft, (170, 130))

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
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound('HIYAH.mp3'))
                    
                    done = True

                if cur_key == chars[keys_right] and keys_right != len(chars)-1:
                    print("current key",cur_key)
                    if cur_key == "i" or cur_key == "l" or cur_key == "j" or cur_key == "t":
                        underline.x += 10
                        print("small jump")
                        keys_right += 1
                    elif cur_key == "w" or cur_key == "m":
                        print("big jump")
                        underline.x += 18
                        keys_right += 1
                    else:
                        underline.x += 14.5
                        keys_right += 1
                    typed_chars.append(cur_key)

                else:
                    keys_wrong += 1

                


            if done:
                pygame.mixer.Channel(1).play(pygame.mixer.Sound('HIYAH.mp3'))
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
                attack = True
                if player == 1:
                    print("current player",player)
                    damageText2 = font2.render(str(damage),True,black,(255,255,255))
                    damageTextRect2 = damageText2.get_rect()
                    damageTextRect2.center = (550,150)
                    player = 2
                elif player == 2:
                    print("current player",player)
                    damageText = font2.render(str(damage),True,black,(255,255,255))
                    damageTextRect = damageText.get_rect()
                    damageTextRect.center = (170,150)
                    player = 1

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
                main_game(need_sen, done, keys_right, keys_wrong, typed_chars, chars,startTime, attack, player)
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
