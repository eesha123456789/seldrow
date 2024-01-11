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
import tkinter
import pygame #user interface
import sys #allows us to exit
import random #for random answer in words

from pygame import mixer
from tkinter import *
from tkinter import ttk


pygame.init() #initializes all modules to get everything started
mixer.init() #for music


#constants

#hex colors
GREEN = "#77DD77"
YELLOW = "#FFDF00"
GREY = "#787c7e"
LIGHT_GREY = "#cfcfcf"

WIDTH, HEIGHT = 800, 660
WORDLE_BG_SIZE = (300,390)

# Different Screens Images and Pictures
BEACH_BG = pygame.image.load("bg_folder/beach_bg.JPG") 
BEACH_RECT = BEACH_BG.get_rect(center=(WIDTH//2+6, HEIGHT//2+8)) 
FOOD_BG = pygame.image.load("bg_folder/food_bg.JPG") 
FOOD_RECT = FOOD_BG.get_rect(center=(WIDTH//2+3, HEIGHT//2)) 
CATS_BG = pygame.image.load("bg_folder/cats_bg.JPG") 
CATS_RECT = CATS_BG.get_rect(center=(WIDTH//2, HEIGHT//2)) 
BACKGROUND = pygame.image.load("blankwordle.png")
# makes bg smaller
BACKGROUND = pygame.transform.scale(BACKGROUND, WORDLE_BG_SIZE)
BACKGROUND_RECT = BACKGROUND.get_rect(center=(WIDTH//2, HEIGHT//2-100)) 


WORDLE_WIN = pygame.image.load("bg_folder/wordle_win.png") 
WORDLE_WIN_RECT = WORDLE_WIN.get_rect(center=(WIDTH//2, HEIGHT//2)) 
WORDLE_LOSS = pygame.image.load("bg_folder/wordle_loss.png") 
WORDLE_LOSS_RECT = WORDLE_LOSS.get_rect(center=(WIDTH//2, HEIGHT//2)) 


#sound effects
eating = pygame.mixer.Sound("sounds/Eating.wav")
congrats = pygame.mixer.Sound("sounds/Congrats.wav")
error = pygame.mixer.Sound("sounds/Error.wav")
meow = pygame.mixer.Sound("sounds/Meow.wav")
water = pygame.mixer.Sound("sounds/Water.wav")
womp = pygame.mixer.Sound("sounds/Womp.wav")
elevator = pygame.mixer.Sound("sounds/Elevator.wav")
play_BG_Sounds=True

def soundCorrect(bg):
    if game_result == "":
        if bg == "nature":
            water.play()
        if bg == "food":
            eating.play()
        if bg == "animals":
            meow.play()
   
def backgroundSounds(bg):
    if bg == "nature":
        natureBG_Sound= pygame.mixer.Sound("Sounds/PapaPizzaria.wav")
        natureBG_Sound.play(-1)
    elif bg == "food":
        foodBG_Sound= pygame.mixer.Sound("sounds/PapaPizzaria.wav")
        foodBG_Sound.play()
    elif bg == "animals":
        animalsBG_Sound= pygame.mixer.Sound("sounds/PapaPizzaria.wav")
        animalsBG_Sound.play(-1)


#Variables for set up of dislay window (how it looks)
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Seldrow!")

SCREEN.fill("white")

# 2nd parameter is the font size
LETTER_FONT = pygame.font.Font("fonts/FredokaOne-Regular.otf", 50)
DISPLAY_FONT = pygame.font.Font("fonts/FredokaOne-Regular.otf", 30)
RESULT_FONT = pygame.font.Font("fonts/FredokaOne-Regular.otf", 60)
KEYBOARD_FONT = pygame.font.Font("fonts/Square.ttf", 30)
wordle_start = False

def initialWordle():
    BG_TEXT1 = DISPLAY_FONT.render("""Welcome to Seldrow! Pick a background.""", True, "black", "white")
    BG_TEXT_RECT1 = BG_TEXT1.get_rect()
    BG_TEXT_RECT1.center = (WIDTH // 2, HEIGHT // 2-100)
    SCREEN.blit(BG_TEXT1,BG_TEXT_RECT1)
    BG_TEXT2 = DISPLAY_FONT.render("""Press 1 for a beachy vibe""", True, "black", "white")
    BG_TEXT_RECT2 = BG_TEXT2.get_rect()
    BG_TEXT_RECT2.center = (WIDTH // 2, HEIGHT // 2-50)
    SCREEN.blit(BG_TEXT2,BG_TEXT_RECT2)
    BG_TEXT3 = DISPLAY_FONT.render("""Press 2 if you're hungry""", True, "black", "white")
    BG_TEXT_RECT3 = BG_TEXT3.get_rect()
    BG_TEXT_RECT3.center = (WIDTH // 2, HEIGHT // 2)
    SCREEN.blit(BG_TEXT3,BG_TEXT_RECT3)
    BG_TEXT4 = DISPLAY_FONT.render("""Press 3 if you're a furry""", True, "black", "white")
    BG_TEXT_RECT4 = BG_TEXT4.get_rect()
    BG_TEXT_RECT4.center = (WIDTH // 2, HEIGHT // 2+50)
    SCREEN.blit(BG_TEXT4,BG_TEXT_RECT4)
    BG_TEXT5 = DISPLAY_FONT.render("""Press 0 if your BORRINGG (lameeee)""", True, "black", "white")
    BG_TEXT_RECT5 = BG_TEXT5.get_rect()
    BG_TEXT_RECT5.center = (WIDTH // 2, HEIGHT // 2+100)
    SCREEN.blit(BG_TEXT5,BG_TEXT_RECT5)
initialWordle()


pygame.display.update() #whole window is updated

#distance from the left for the first letter
letter_x_pos = 205
#distance from the top of the screen fro the first row
letter_y_pos = 52
#between each letter in a row
LETTER_X_SPACING = 83
#between each row
LETTER_Y_SPACING = 20
LETTER_SIZE = 69

# Global variables
words = []
guesses_count = 0

# guesses variable stores all guesses, which are lists of letters..
guesses = [[]] * 6

current_guess = []
current_guess_string = ""
game_result = ""

#Main Menu Button
#WORDLE_POS_MOUSE = pygame.mouse.get_pos()
#WORDLE_MAIN_MENU=button.Button()

class WordleLetter:
    def __init__(self, text, bg_pos):
        self.text = text
        self.bg_color = "white"
        self.text_color = "black"
        self.bg_pos = bg_pos
        self.bg_x = bg_pos[0]
        self.bg_y = bg_pos[1]
        self.bg_rect = (self.bg_x, self.bg_y, LETTER_SIZE, LETTER_SIZE) #left, top, width, height 
        #might need more tuning to center the letters
        self.text_pos = (self.bg_x + 30, self.bg_y + 30)

        self.surface = LETTER_FONT.render(self.text, True, self.text_color)
        self.text_rect = self.surface.get_rect(center = self.text_pos)

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

#keyboard variables

#distance from the left for the first letter
kb_x_pos = 110
#distance from the top of the screen fro the first row
kb_y_pos = 400
#between each letter in a row
KEY_X_SPACING = 10
#between each row
KEY_Y_SPACING = 10
KEY_HEIGHT = 60
KEY_WIDTH = 50

class Key:
    def __init__(self, name, key_pos):
        self.name = name
        self.key_color = LIGHT_GREY
        self.letter_color = "black"
        self.key_pos = key_pos
        self.key_x = key_pos[0]
        self.key_y = key_pos[1]

        self.key_rect = (self.key_x, self.key_y, KEY_WIDTH, KEY_HEIGHT) #left, top, width, height 
        #might need more tuning to center the letters
        self.letter_pos = (self.key_x + 25, self.key_y + 30)

        self.surface = KEYBOARD_FONT .render(self.name, True, self.letter_color)
        self.letter_rect = self.surface.get_rect(center = self.letter_pos)
        
    def drawKey(self):
        pygame.draw.rect(SCREEN, self.key_color, self.key_rect)
        self.surface = KEYBOARD_FONT .render(self.name, True, self.letter_color)
        SCREEN.blit(self.surface, self.letter_rect)

        pygame.display.update()

    def update(self, bgColor):
        self.key_color = bgColor
        self.drawKey()


class Keyboard:
    def __init__(self):
        self.keys = {}

    def drawKeyboard(self):
        global kb_x_pos, kb_y_pos
        alphabet = "qwertyuiopasdfghjklzxcvbnm"
        for letter in alphabet:
            key = Key(letter, (kb_x_pos,kb_y_pos))
            self.keys[letter] = key
            key.drawKey()
            kb_x_pos += KEY_WIDTH + KEY_X_SPACING

            if letter == "p":
                kb_y_pos += KEY_HEIGHT + KEY_Y_SPACING
                #x pos is good now
                kb_x_pos = 140

            if letter == "l":
                kb_y_pos += KEY_HEIGHT + KEY_Y_SPACING
                kb_x_pos = 200

    def updateKey(self, letter, keyColor):
        key = self.keys[letter]
        key.update(keyColor)
keyboard = Keyboard()


def check_guess(guess, answer):
    # note: must use global keyword to change global variables in function
    global current_guess, guesses_count, current_guess_string, game_result, letter_x_pos, letter_y_pos

    all_correct = True
    used_letters = ""
    
    #iterate through each letter in the guess
    for i in range(5):
        cur_letter = guess[i].text.lower()
        if cur_letter == answer[i]:
            guess[i].bg_color = GREEN
            guess[i].text_color = "white"
            used_letters += cur_letter
            #keyboard
            keyboard.updateKey(cur_letter, GREEN)
            
        elif cur_letter in answer and cur_letter not in used_letters:
            guess[i].bg_color = YELLOW
            guess[i].text_color = "white"
            all_correct = False
            #keyboard
            keyboard.updateKey(cur_letter, YELLOW)

        else: #letter not in answer
            guess[i].bg_color = GREY
            guess[i].text_color = "white"
            all_correct = False
            #keyboard
            keyboard.updateKey(cur_letter, GREY)

        
        guess[i].draw()
        pygame.display.update()

    if all_correct == True:
        game_result = "W"
        end_display()
    elif all_correct == False and guesses_count >= 5:
        game_result = "L"
        end_display()

    guesses_count += 1
    letter_x_pos = 205
    letter_y_pos += LETTER_Y_SPACING
    current_guess = []
    current_guess_string = ""
        

def add_new_letter():
    #adds new letter to the guess
    global letter_x_pos, current_guess_string, current_guess, guesses, letter_y_pos
    new_letter = WordleLetter(key_pressed, (letter_x_pos, guesses_count * 80 + letter_y_pos))
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
    current_guess_string = current_guess_string[:-1]
    #need to double check this
    del(guesses[guesses_count - 1][len(current_guess) - 1])
    letter_x_pos -= LETTER_X_SPACING 
    #just added
    current_guess[len(current_guess) - 1].bg_color = "white"
    current_guess[len(current_guess) - 1].text_color = "white"
    current_guess[len(current_guess) - 1].draw()
    
    pygame.display.update()
    current_guess.pop()

def reset():
    #resets variables after each game
    global guesses_count, current_answer, guesses, current_guess, current_guess_string, game_result, wordle_start, letter_y_pos, kb_x_pos, kb_y_pos
    
    SCREEN.fill("white")
    initialWordle()
    if wordle_start == True:
        wordle_start = False
    pygame.display.update()
    
    letter_y_pos = 52
    guesses_count = 0
    current_answer = ""
    guesses = [[]] * 6
    current_guess = []
    current_guess_string = ""
    game_result = ""
    play_BG_Sounds=True

    #keyboard variables
    kb_x_pos = 110
    kb_y_pos = 400
    
def end_display():
    if game_result == "W":
        SCREEN.blit(WORDLE_WIN, WORDLE_WIN_RECT)
        congrats.play()
    elif game_result == "L":
        SCREEN.blit(WORDLE_LOSS, WORDLE_LOSS_RECT)
        LOSS_TEXT = LETTER_FONT.render("""Welcome to Seldrow! Pick a background.)""", True, "black", "white")
        LOSS_TEXT_RECT = LOSS_TEXT.get_rect()
        LOSS_TEXT_RECT.center = (WIDTH // 2, HEIGHT // 2 + 40)
        answer_display = RESULT_FONT.render(current_answer, True, "black", "white")
        answer_display_rect = answer_display.get_rect()
        answer_display_rect.center = (WIDTH // 2, HEIGHT // 2-30)
        SCREEN.blit(answer_display, answer_display_rect)
        womp.play()
    pygame.display.update()
    

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if wordle_start == False:
            cur_bg = ""
            elevator.play(-1)
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                cur_bg = "nature"
                SCREEN.fill("white")
                SCREEN.blit(BEACH_BG, BEACH_RECT)
                keyboard.drawKeyboard()
                with open("wordLists/nature.txt", "r") as natureWordsFile:
                    natureWords = natureWordsFile.read().splitlines()
                current_answer = random.choice(natureWords)
                wordle_start = True
                
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_2:
                cur_bg = "food"
                SCREEN.fill("white")
                SCREEN.blit(FOOD_BG, FOOD_RECT)
                keyboard.drawKeyboard()
                with open("wordLists/food.txt", "r") as foodWordsFile:
                    foodWords = foodWordsFile.read().splitlines()
                current_answer = random.choice(foodWords)
                wordle_start = True
                
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_3:
                cur_bg = "animals"
                SCREEN.fill("white")
                SCREEN.blit(CATS_BG, CATS_RECT)
                keyboard.drawKeyboard()
                with open("wordLists/animals.txt", "r") as animalWordsFile:
                    animalWords = animalWordsFile.read().splitlines()
                current_answer = random.choice(animalWords)
                wordle_start = True
                
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_0:
                SCREEN.fill("white")
                SCREEN.blit(BACKGROUND, BACKGROUND_RECT)
                keyboard.drawKeyboard()
                with open("wordLists/words.txt", "r") as allWordsFile:
                    allWords = allWordsFile.read().splitlines()
                current_answer = random.choice(allWords)
                wordle_start = True
                
            pygame.display.update()
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #    if beach_button.checkForInput(WORDLE_POS_MOUSE):
            #       SCREEN.blit(BEACH_BG, BEACH_BG.get_rect())
        if wordle_start == True:
            elevator.stop()
            if(play_BG_Sounds==True):
                backgroundSounds(cur_bg)
                play_BG_Sounds=False
            if game_result != "":
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    reset()
            if event.type == pygame.KEYDOWN:
                print(event.key)
                print(current_answer)
                if event.key == pygame.K_RETURN:
                    #if game is finished
                    if game_result != "":
                        end_display()
                    else:
                        if len(current_guess_string) == 5:
                            temp = False
                            with open("wordLists/words.txt",'r') as text_file:
                                lines = text_file.read().splitlines()
                            for line in lines:
                                if current_guess_string == line:
                                    check_guess(current_guess, current_answer)
                                    soundCorrect(cur_bg)
                                    temp = True
                            if temp == False:
                                error.play()
                                errorPopup = tkinter.Tk()
                                placement = ttk.Frame(errorPopup, padding=75)
                                placement.grid()
                                ttk.Label(placement, background= "yellow", font="Times", text="Please enter a valid word.").grid(column=0, row=0)
                                ttk.Button(placement, text="Ok", padding=10, command=errorPopup.destroy).grid(column=0, row=2)
                                errorPopup.mainloop()           
                
                elif event.key == pygame.K_BACKSPACE:
                    if len(current_guess_string) > 0:
                        delete_letter()
                else:
                    key_pressed = event.unicode.lower()
                    if key_pressed in "abcdefghijklmnopqrstuvwxyz" and key_pressed != "":
                        if len(current_guess_string) < 5:
                            add_new_letter()

            
       

