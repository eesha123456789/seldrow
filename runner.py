"""
class Main:
    words = []
    file = open("words.txt", "r")
    words = file.read.splitlines()

//use this
    words = []
    with open("words.txt", "r") as file:
        words = file.read().splitlines()
    wordAnswer = random.choice(words)
"""

import pygame #user interface
import sys #variables and functions
import random #for random answer in words text file
import sys #allows us to exit
import random #for random answerWord in words

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


#Variables for set up of dislay window (how it looks)
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
BACKGROUND = pygame.image.load("blankwordle.png")  #adds background image
BACKGROUND_RECT = BACKGROUND.get_rect(center=(500, 300)) 

pygame.display.set_caption("Seldrow!")

SCREEN.fill("white")

# Different Screens
BEACH_BG = pygame.image.load("bg_folder/beach_bg.jpg") 
FOOD_BG = pygame.image.load("bg_folder/food_bg.jpg") 
WORDS_BG = pygame.image.load("bg_folder/words_bg.PNG") 

button_surface = pygame.image.load("bg_folder/button.jpg")
button_surface = pygame.transform.scale(button_surface, (250, 100))
beach_button=Button()
beach_button._init_(button_surface, 150, 100, "Beach Background")
SCREEN.blit(button_surface, beach_button)

food_button=Button()
food_button._init_(button_surface, 150, 300, "Food Background")
SCREEN.blit(button_surface, food_button)

words_button=Button()
words_button._init_(button_surface, 150, 500, "Words Background")
SCREEN.blit(button_surface, words_button)



SCREEN.blit(BACKGROUND, BACKGROUND_RECT) #place image onto the screen

pygame.display.update() #whole window is updated


LETTER_X_SPACING = 0
LETTER_Y_SPACING = 0
LETTER_SIZE = 0
LETTER_FONT = pygame.font.Font("FredokaOne-Regular.otf")

# Global variables

guesses_count = 0

# guesses is a 2D list storing all the guesses, which are lists of letters.
# The list will be iterated through so each letter in each guess will be drawn on the screen.
guesses = [[]] * 6

current_guess = []
current_guess_string = ""

game_result = ""


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
        self.text_surface = LETTER_FONT.render(self.text, True, self.text_color)
        self.text_rect = self.text_surface.get_rect(center=self.text_position)

    def draw(self):
        # Puts the letter on the screen at the desired positions.
        pygame.draw.rect(SCREEN, self.bg_color, self.bg_rect)
        self.text_surface = LETTER_FONT.render(self.text, True, self.text_color)
        SCREEN.blit(self.text_surface, self.text_rect)
        

        
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
    global current_guess, guesses_count, current_guess_string, game_result

    all_correct = True
    
    #iterate through each letter in the guess
    for i in range(5):
        cur_letter = guess[i].lower()
        if guess[i] == answer[i]:
            guess[i].bg_color = GREEN
            guess[i].text_color = "white"
        elif guess[i] in answer:
            guess[i].bg_color = YELLOW
            guess[i].text_color = "white"
            all_correct = False
        else: #letter not in answer
            guess[i].bg_color = GREY
            guess[i].text_color = "white"
            all_correct = False

        pygame.display.update

    if all_correct == True:
        game_result = "W"
    else:
        game_result = "L"

    guesses_count += 1
    current_guess = []
    current_guess_string = ""
        

#def add_new_letter():
    #adds new letter to the guess

#def delete_letter():
    #deletes letter from guess

#def reset():
    #resets variables
    

while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if beach_button.checkForInput(WORDLE_POS_MOUSE):
                    SCREEN.blit(BEACH_BG, BEACH_BG.get_rect())
       
