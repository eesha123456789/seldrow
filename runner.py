"""
class Main:
    words = []
    file = open("words.txt", "r")
    words = file.read.splitlines()

//use this
    words = []
    with open("words.txt", "r") as file:
        words = file.read().splitlines()
    answer = random.choice(words)
"""
from array import *
import pygame #user interface
import sys #allows us to exit
import random #for random answer in words

import main_menu 
from button import Button

pygame.init() #initializes all modules to get everything started


#constants

#hex colors
GREEN = "#77DD77"
YELLOW = "#fdfd96"
GREY = "#787c7e"
OUTLINE = "#cfcfcf"

WIDTH, HEIGHT = 800, 660

# Different Screens Images and Pictures
BEACH_BG = pygame.image.load("bg_folder/beach_bg.JPG") 
BEACH_RECT = BEACH_BG.get_rect(center=(WIDTH//2, HEIGHT//2)) 
FOOD_BG = pygame.image.load("bg_folder/food_bg.JPG") 
FOOD_RECT = FOOD_BG.get_rect(center=(WIDTH//2, HEIGHT//2)) 
CATS_BG = pygame.image.load("bg_folder/cats_bg.JPG") 
CATS_RECT = CATS_BG.get_rect(center=(WIDTH//2, HEIGHT//2)) 
BACKGROUND = pygame.image.load("blankwordle.png")
BACKGROUND_RECT = BACKGROUND.get_rect(center=(WIDTH//2, HEIGHT//2)) 

WORDLE_WIN = pygame.image.load("bg_folder/wordle_win.png") 
WORDLE_WIN_RECT = WORDLE_WIN.get_rect(center=(WIDTH//2, HEIGHT//2)) 
WORDLE_LOSS = pygame.image.load("bg_folder/wordle_loss.png") 
WORDLE_LOSS_RECT = WORDLE_LOSS.get_rect(center=(WIDTH//2, HEIGHT//2)) 


#Variables for set up of dislay window (how it looks)
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Seldrow!")

SCREEN.fill("white")


LETTER_FONT = pygame.font.Font("FredokaOne-Regular.otf")
wordle_start = False
def initialWordle():
    BG_TEXT1 = LETTER_FONT.render("""Welcome to Seldrow! Pick a background.""", True, "black", "white")
    BG_TEXT_RECT1 = BG_TEXT1.get_rect()
    BG_TEXT_RECT1.center = (WIDTH // 2, HEIGHT // 2-40)
    SCREEN.blit(BG_TEXT1,BG_TEXT_RECT1)
    BG_TEXT2 = LETTER_FONT.render("""Press 1 for a beachy vibe""", True, "black", "white")
    BG_TEXT_RECT2 = BG_TEXT2.get_rect()
    BG_TEXT_RECT2.center = (WIDTH // 2, HEIGHT // 2-20)
    SCREEN.blit(BG_TEXT2,BG_TEXT_RECT2)
    BG_TEXT3 = LETTER_FONT.render("""Press 2 if you're hungry""", True, "black", "white")
    BG_TEXT_RECT3 = BG_TEXT3.get_rect()
    BG_TEXT_RECT3.center = (WIDTH // 2, HEIGHT // 2)
    SCREEN.blit(BG_TEXT3,BG_TEXT_RECT3)
    BG_TEXT4 = LETTER_FONT.render("""Press 3 if you're a furry""", True, "black", "white")
    BG_TEXT_RECT4 = BG_TEXT4.get_rect()
    BG_TEXT_RECT4.center = (WIDTH // 2, HEIGHT // 2+20)
    SCREEN.blit(BG_TEXT4,BG_TEXT_RECT4)
    BG_TEXT5 = LETTER_FONT.render("""Press b if your BORRINGG (lameeee)""", True, "black", "white")
    BG_TEXT_RECT5 = BG_TEXT5.get_rect()
    BG_TEXT_RECT5.center = (WIDTH // 2, HEIGHT // 2+40)
    SCREEN.blit(BG_TEXT5,BG_TEXT_RECT5)
initialWordle()

#If we need buttons
"""button_surface = pygame.image.load("bg_folder/button.jpg")
button_surface = pygame.transform.scale(button_surface, (250, 100))
beach_button=Button()
beach_button._init_(button_surface, 150, 100, "Beach Background")
SCREEN.blit(button_surface, beach_button)

food_button=Button()
food_button._init_(button_surface, 150, 300, "Food Background")
SCREEN.blit(button_surface, food_button)

words_button=Button()
words_button._init_(button_surface, 150, 500, "Words Background")
SCREEN.blit(button_surface, words_button)"""


pygame.display.update() #whole window is updated


LETTER_X_SPACING = 80
LETTER_Y_SPACING = 10
LETTER_SIZE = 70

# Global variables

#not sure if this is is right
words = []
with open("words.txt", "r") as file:
    words = file.read().splitlines()
current_answer = random.choice(words)

guesses_count = 0

# guesses is a 2D list storing all the guesses, which are lists of letters.
# The list will be iterated through so each letter in each guess will be drawn on the screen.
guesses = [[]] * 6

#value needs to be tuned
letter_x_pos = 100
current_guess = []
current_guess_string = ""


game_result = ""

wordle_start = False

#Main Menu Button
WORDLE_POS_MOUSE = pygame.mouse.get_pos()
#WORDLE_MAIN_MENU=button.Button()


class WordleLetter:
    def __init__(self, text, bg_position):
        self.bg_color = "white"
        self.text_color = "black"
        self.bg_position = bg_position
        self.bg_x = bg_position[0]
        self.bg_y = bg_position[1]
        self.text = text
        self.bg_rect = (self.bg_x, self.bg_y, LETTER_SIZE, LETTER_SIZE) #left, top, width, height 
        self.text_position = (self.bg_x, self.bg_y)
        self.surface = LETTER_FONT.render(self.text, True, self.text_color)
        self.text_rect = self.surface.get_rect(center=self.text_position)

    def draw(self):
        # Puts the letter on the screen at the desired positions.
        pygame.draw.rect(SCREEN, self.bg_color, self.bg_rect)
        self.surface = LETTER_FONT.render(self.text, True, self.text_color)
        SCREEN.blit(self.surface, self.text_rect)

        #For Main Menu
        #WORDLE_MAIN_MENU = button.Button(pos = (400,300), text_input = "Main Menu")
        #WORDLE_MAIN_MENU.changeColor(WORDLE_POS_MOUSE)
        #WORDLE_MAIN_MENU.update(SCREEN)
        
        
        pygame.display.update()

    def delete(self):
        # Fills the letter's spot with the default square, emptying it.
        pygame.draw.rect(SCREEN, "white", self.bg_rect)
        pygame.draw.rect(SCREEN, OUTLINE, self.bg_rect, 3) #last parameter is the width of the border
        pygame.display.update()
    
def check_guess(guess, answer):
    # note: must use global keyword to change global variables in function
    global current_guess, guesses_count, current_guess_string, game_result, letter_x_pos

    all_correct = True
    
    #iterate through each letter in the guess
    for i in range(5):
        cur_letter = guess[i]
        if cur_letter == answer[i]:
            cur_letter.bg_color = GREEN
            cur_letter.text_color = "white"
        elif cur_letter in answer:
            cur_letter.bg_color = YELLOW
            cur_letter.text_color = "white"
            all_correct = False
        else: #letter not in answer
            cur_letter.bg_color = GREY
            cur_letter.text_color = "white"
            all_correct = False

        pygame.display.update()

    if all_correct == True:
        game_result = "W"
    else:
        game_result = "L"

    guesses_count += 1
    letter_x_pos = 100
    current_guess = []
    current_guess_string = ""
        

def add_new_letter():
    #adds new letter to the guess
    global letter_x_pos, current_guess_string, current_guess, guesses
    new_letter = WordleLetter(key_pressed, (letter_x_pos, guesses_count * 80 + LETTER_Y_SPACING))
    letter_x_pos += LETTER_X_SPACING
    current_guess_string += key_pressed
    current_guess.append(new_letter)
    guesses[guesses_count - 1].append(new_letter)

    for i in guesses:
        for j in i:
            j.draw()
    

def delete_letter():
    #deletes letter from guess
    global letter_x_pos, current_guess_string, current_guess, guesses
    current_guess.pop()
    current_guess_string = current_guess_string[:-1]
    #need to double check this
    del(guesses[guesses_count - 1][len(current_guess) - 1])
    letter_x_pos -= LETTER_X_SPACING  
    pygame.display.update()

def end_display():
    if game_result == "W":
        SCREEN.blit(WORDLE_WIN, WORDLE_WIN_RECT)
    elif game_result == "L":
        SCREEN.blit(WORDLE_LOSS, WORDLE_LOSS_RECT)
        LOSS_TEXT = LETTER_FONT.render("""Welcome to Seldrow! Pick a background.)""", True, "black", "white")
        LOSS_TEXT_RECT = LOSS_TEXT.get_rect()
        LOSS_TEXT_RECT.center = (WIDTH // 2, HEIGHT // 2+40)
    pygame.display.update()
    if event.type == pygame.KEYDOWN and event.key == pygame.K_ENTER:
        reset()

    
    
def reset():
    #resets variables after each game
    global guesses_count, current_answer, guesses, current_guess, current_guess_string, game_result, wordle_start
    
    SCREEN.fill("white")
    initialWordle()
    wordle_start = False
    pygame.display.update()

    guesses_count = 0
    current_answer = random.choice(words)
    guesses = [[]] * 6
    current_guess = []
    current_guess_string = ""
    game_result = ""
    

while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if wordle_start == False:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                    SCREEN.blit(BEACH_BG, BEACH_RECT)
                    wordle_start == True
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_2:
                    SCREEN.fill("white")
                    SCREEN.blit(FOOD_BG, FOOD_RECT)
                    wordle_start == True
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_3:
                    SCREEN.blit(CATS_BG, CATS_RECT)
                    wordle_start == True
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_b:
                    SCREEN.blit(BACKGROUND, BACKGROUND_RECT)
                    wordle_start == True
                pygame.display.update()
           # if event.type == pygame.MOUSEBUTTONDOWN:
            #    if beach_button.checkForInput(WORDLE_POS_MOUSE):
             #       SCREEN.blit(BEACH_BG, BEACH_BG.get_rect())
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if wordle_start == False:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                    SCREEN.fill("white")
                    SCREEN.blit(BEACH_BG, BEACH_RECT)
                    wordle_start = True
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_2:
                    SCREEN.fill("white")
                    SCREEN.blit(FOOD_BG, FOOD_RECT)
                    wordle_start = True
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_3:
                    SCREEN.fill("white")
                    SCREEN.blit(CATS_BG, CATS_RECT)
                    wordle_start = True
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_KP_ENTER:
                    SCREEN.fill("white")
                    SCREEN.blit(BACKGROUND, BACKGROUND_RECT)
                    wordle_start = True
                pygame.display.update()
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #    if beach_button.checkForInput(WORDLE_POS_MOUSE):
                #       SCREEN.blit(BEACH_BG, BEACH_BG.get_rect())

            if event.type == pygame.KEYDOWN:
                print(event.key)
                if event.key == pygame.K_RETURN:
                    #if game is finished
                    if game_result != "":
                        end_display()
                    else:
                        if len(current_guess_string) == 5:
                            check_guess(current_guess, current_answer)
                
                elif event.key == pygame.K_BACKSPACE:
                    if len(current_guess_string) > 0:
                        delete_letter()
                else:
                    key_pressed = event.unicode.lower()
                    if key_pressed in "abcdefghijklmnopqrstuvwxyz" and key_pressed != "":
                        if len(current_guess_string) < 5:
                            add_new_letter()

            
       

