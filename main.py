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
mixer.music.load("xiexie.mp3")
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

bg = pygame.image.load("background.png").convert_alpha()
punchGuyStanding = pygame.image.load("punchguy_right.png").convert_alpha()
punchGuyPunchLeft = pygame.image.load(
    "punch_guy_punching_with_left_punch_hand.png"
).convert_alpha()
punchGuyPunchRight = pygame.image.load(
    "punch_guy_punching_with_right_punch_hand.png"
).convert_alpha()
wizardLeft = pygame.image.load("wizard_left.png").convert_alpha()
logo = pygame.image.load("Typing_Tussle_2.png").convert_alpha()

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
dmg_display = False


sentences = [
    "the cat sleeps on the warm, sunny windowsill.",
    "reading a book by candlelight is quite calming.",
    "rainy days bring a sense of peace and coziness.",
    "the forest hides secrets waiting to be discovered.",
    "cooking together creates cherished family memories.",
    "music lifts our spirits and soothes our hearts.",
    "morning walks refresh the mind and body.",
    "stars twinkle like diamonds in the night sky.",
    "a cup of tea warms the coldest of evenings.",
    "small acts of kindness can change the world.",
    "the river flows gently, whispering ancient stories.",
    "a smile can brighten even the darkest days.",
    "finding joy in simple things is true happiness.",
    "painting allows emotions to flow freely on canvas.",
    "birdsong heralds the arrival of a new day.",
    "a handwritten letter holds sentimental treasures.",
    "sunsets paint the sky with hues of gold.",
    "clouds dance lazily in the vast blue canvas.",
    "childhood memories are a treasure chest of happiness.",
    "curiosity leads to discoveries beyond imagination.",
    "gardens bloom with colors, a living masterpiece.",
    "trees sway in the gentle breeze, a tranquil sight.",
    "a cozy blanket and book invite peaceful moments.",
    "morning dew glistens like a thousand tiny diamonds.",
    "a quiet forest walk soothes the weary soul.",
    "kindness ripples outward, changing lives forever.",
    "family gatherings create bonds that never break.",
    "a hearty meal warms both body and spirit.",
    "autumn leaves whisper secrets in the wind.",
    "starry nights hold the promise of dreams fulfilled.",
    "the smell of fresh-baked bread is pure comfort.",
    "childhood laughter echoes in the heart forever.",
    "a clear sky reveals a universe of wonders.",
    "a good book can transport you to new worlds.",
    "every sunset paints a unique masterpiece.",
    "morning birdsong greets the day with joy.",
    "the simple life often holds the greatest riches.",
]


def calculateDamage(speed, accuracy):
    damage = round((200 / speed**2) * (accuracy))
    return damage


def display_damage(damage):
    damage_text = font.render(f"Damage: {damage}", True, (255, 255, 255))
    damage_rect = damage_text.get_rect(center=(width // 2, 50))
    screen.blit(damage_text, damage_rect)


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
restart_button = button((150, 43, 56), (100), 600, 350, 100, "Play Again")
quit_button = button((150, 43, 56), (500), 600, 350, 100, "Quit")
gameover = pygame.image.load("gameover.png")
gameover = pygame.transform.scale2x(gameover)
start_time = pygame.time.get_ticks()

titlefont = pygame.font.SysFont("papyrus", 140)
font = pygame.font.Font("freesansbold.ttf", 30)
monofont = pygame.font.SysFont("lucidasans", 35)
font2 = pygame.font.Font("freesansbold.ttf", 50)
x = 150
y = 641
player1_health = 300
player1_hel = pygame.Rect(50, 30, 40, 40)
player1_bar = pygame.Rect((player1_hel.x), 90, player1_health, 30)
player1_max_bar = pygame.Rect((player1_hel.x), 90, 300, 30)
player2_health = 100
player2_hel = pygame.Rect(650, 30, 40, 40)
player2_bar = pygame.Rect((player2_hel.x), 90, player2_health, 30)
player2_max_bar = pygame.Rect((player2_hel.x), 90, 300, 30)
enter = pygame.image.load("enter.png")


def end(player1, player2):
    if player1 > player2:
        winner = "Player 1!"
    elif player2 > player1:
        winner = "Player 2!"

    while True:
        pygame.display.update()
        screen.fill((0, 0, 0))
        quit_button.draw(screen, (0, 0, 0))
        restart_button.draw(screen, (0, 0, 0))
        winner_text = monofont.render(winner, True, black, (132, 206, 235))
        winner_textRect0 = winner_text.get_rect()
        winner_textRect0.center = (width // 2, 600)
        screen.blit(gameover, (100, 50))

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if event.type == QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_button.isOver(pos):
                    pygame.time.delay(3000)
                    main_game(
                        need_sen,
                        done,
                        keys_right,
                        keys_wrong,
                        typed_chars,
                        chars,
                        startTime,
                        attack,
                        player,
                        cur_key,
                    )
                if quit_button.isOver(pos):
                    pygame.quit()


def main_game(
    need_sen,
    done,
    keys_right,
    keys_wrong,
    typed_chars,
    chars,
    startTime,
    attack,
    player,
    cur_key,
):
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
        screen.fill((135, 206, 235))  # load background colour
        screen.blit(text0, textRect0)
        screen.blit(bg, (0, 0))  # load background image
        screen.blit(enter, ((200), height - 105))
        pygame.draw.rect(screen, (220, 20, 60), player1_bar)
        pygame.draw.rect(screen, (225, 225, 225), player1_max_bar, 2)
        pygame.draw.rect(screen, (220, 20, 60), player2_bar)
        pygame.draw.rect(screen, (225, 225, 225), player2_max_bar, 2)
        if attack == False:
            guy = screen.blit(punchGuyStanding, (guyX, guyY))
            pygame.mixer.Channel(1).play(pygame.mixer.Sound("HIYAH.mp3"))

        elif attack == True:
            # guy.kill()
            # guy.set_alpha(0)
            pygame.mixer.Channel(1).play(pygame.mixer.Sound("HIYAH.mp3"))
            punchGuy = screen.blit(punchGuyPunchRight, (guyX, guyY))
        # time.sleep(3)

        screen.blit(wizardLeft, (550, 125))
        timetext = font2.render(str(gameClock), True, black, (34, 126, 145))
        timetextrect = timetext.get_rect()
        timetextrect.center = (width // 2, 50)
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
                if keys == pygame.K_COMMA:
                    cur_key = ","
                if (keys == pygame.K_RETURN) and (keys_right + 1 == len(chars)):
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("HIYAH.mp3"))

                    done = True

                if cur_key == chars[keys_right] and keys_right != len(chars) - 1:
                    if cur_key == "i" or cur_key == "l" or cur_key == "j":
                        underline.x += 12
                        keys_right += 1
                    elif cur_key == "a":
                        underline.x += 21
                        keys_right += 1
                    elif cur_key == "f" or cur_key == "t":
                        underline.x += 13
                        keys_right += 1
                    elif cur_key == "r":
                        underline.x += 12
                        keys_right += 1
                    elif cur_key == " ":
                        underline.x += 12
                        keys_right += 1
                    elif cur_key == "h":
                        underline.x += 19
                        keys_right += 1
                    elif cur_key == "m":
                        underline.x += 32
                        keys_right += 1
                    elif cur_key == "w":
                        underline.x += 27
                        keys_right += 1
                    elif cur_key == "v":
                        underline.x += 18
                        keys_right += 1
                    elif cur_key == "b":
                        underline.x += 20.5
                        keys_right += 1
                    elif cur_key == "g":
                        underline.x += 24
                        keys_right += 1
                    elif cur_key == "n":
                        underline.x += 22
                        keys_right += 1
                    elif cur_key == "p" or cur_key == "q":
                        underline.x += 22.5
                        keys_right += 1
                    elif cur_key == "o":
                        underline.x += 22
                        keys_right += 1
                    elif cur_key == ",":
                        underline.x += 12
                        keys_right += 1
                    elif cur_key == "e":
                        underline.x += 15
                        keys_right += 1
                    else:
                        underline.x += 20
                        keys_right += 1
                    typed_chars.append(cur_key)

                else:
                    keys_wrong += 1

            # Tells user how much damage done, swtitches player each enter with a delay, game over when health is 0, play again button or quit,
            # Tell user damage and tell which players turn it now is
            if done:
                if player1_bar.width <= 1 or player2_bar.width <= 1:
                    chars.clear()
                    typed_chars.clear()
                    keys_right = 0
                    keys_wrong = 0
                    need_sen = True
                    gameClock = 0
                    attack = True
                    end(player1_health, player2_health)

                else:
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("HIYAH.mp3"))
                    accuracy = round((keys_right / (keys_right + keys_wrong)) * 100)
                    print("accuracy", accuracy)
                    print("Speed =", len(chars), "/", gameClock)
                    damage = calculateDamage(gameClock, accuracy)
                    print("Damage", damage)
                    if player == 1:
                        player2_bar.width -= damage / 2
                    elif player == 2:
                        player1_bar.width -= damage / 2
                    chars.clear()
                    typed_chars.clear()
                    keys_right = 0
                    keys_wrong = 0
                    need_sen = True
                    gameClock = 0
                    attack = True
                    if player == 1:
                        player = 2
                    elif player == 2:
                        player = 1

        pygame.display.update()


# Next steps, find time and make user know when they get smth right, then set up hte turn based stuff


def main_menu():
    while True:
        pygame.display.update()
        screen.fill((202, 228, 241))
        start_button.draw(screen, (0, 0, 0))
        end_button.draw(screen, (0, 0, 0))
        title = titlefont.render("Typing Tussle", True, "white", (202, 228, 241))
        titleRect = title.get_rect()
        titleRect.center = (500, 120)
        screen.blit(title, titleRect)
        screen.blit(logo, (250, 10))
        logo.set_alpha(100)

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                startTime = time.time()
                if start_button.isOver(pos):
                    main_game(
                        need_sen,
                        done,
                        keys_right,
                        keys_wrong,
                        typed_chars,
                        chars,
                        startTime,
                        attack,
                        player,
                        cur_key,
                    )
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
