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
import asyncio


pygame.init() #initializes all modules to get everything started
mixer.init() #for music

#firebase database
import firebase_admin
from firebase_admin import db,credentials

#autheticate to firebase
cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred,{"databaseURL":"https://seldrow-326de-default-rtdb.firebaseio.com/"})

ref = db.reference("/")
ref.get()

#constants

#hex colors
GREEN = "#77DD77"
YELLOW = "#FFDF00"
GREY = "#787c7e"
LIGHT_GREY = "#cfcfcf"

#make this bigger so we can have a menu on top of the screen
WIDTH, HEIGHT = 800, 660
WORDLE_BG_SIZE = (300,390)
#Variables for set up of dislay window (how it looks)
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Seldrow!")


# Different Screens Images and Pictures
NATURE_BG = pygame.image.load("bg_folder/nature_bg.png") 
NATURE_BG = pygame.transform.scale(NATURE_BG, (600,400))
NATURE_RECT = NATURE_BG.get_rect(center=(WIDTH//2, HEIGHT//2-120)) 

FOOD_BG = pygame.image.load("bg_folder/food_bg.png") 
FOOD_BG = pygame.transform.scale(FOOD_BG, (600,400))
FOOD_RECT = FOOD_BG.get_rect(center=(WIDTH//2, HEIGHT//2-120)) 

CATS_BG = pygame.image.load("bg_folder/cats_bg.png") 
CATS_BG = pygame.transform.scale(CATS_BG, (600,400))
CATS_RECT = CATS_BG.get_rect(center=(WIDTH//2, HEIGHT//2-120)) 

BACKGROUND = pygame.image.load("bg_folder/blankwordle.png")
BACKGROUND = pygame.transform.scale(BACKGROUND, WORDLE_BG_SIZE)
BACKGROUND_RECT = BACKGROUND.get_rect(center=(WIDTH//2, HEIGHT//2-120)) 


WORDLE_WIN = pygame.image.load("bg_folder/wordle_win.png") 
WORDLE_WIN_RECT = WORDLE_WIN.get_rect(center=(WIDTH//2, HEIGHT//2)) 
WORDLE_LOSS = pygame.image.load("bg_folder/wordle_loss.png") 
WORDLE_LOSS_RECT = WORDLE_LOSS.get_rect(center=(WIDTH//2, HEIGHT//2)) 

#us!!
EESHA_PIC = pygame.image.load("image_folder/eesha.png")
EESHA_PIC = pygame.transform.scale(EESHA_PIC, (220,500))
EESHA_RECT = EESHA_PIC.get_rect(center = ((WIDTH * 4)//5, HEIGHT//2 + 50))

SOPHIA_PIC = pygame.image.load("image_folder/sophia.png")
SOPHIA_PIC = pygame.transform.scale(SOPHIA_PIC, (220,460))
SOPHIA_RECT = SOPHIA_PIC.get_rect(center = (WIDTH //5, HEIGHT//2 + 70))

#database images (including coin tracker)
COIN_TRACKER = pygame.image.load("image_folder/coin.png")
COIN_TRACKER = pygame.transform.scale(COIN_TRACKER, (180, 60))
COIN_TRACKER_RECT = COIN_TRACKER.get_rect(center = (WIDTH-100, HEIGHT-50))

#sound effects
eating = pygame.mixer.Sound("sounds/Eating.wav")
congrats = pygame.mixer.Sound("sounds/Congrats.wav")
error = pygame.mixer.Sound("sounds/Error.wav")
meow = pygame.mixer.Sound("sounds/Meow.wav")
water = pygame.mixer.Sound("sounds/Water.wav")
womp = pygame.mixer.Sound("sounds/Womp.wav")
elevator = pygame.mixer.Sound("sounds/Elevator.wav")

#bg SOunds
natureBG_Sound= pygame.mixer.Sound("Sounds/LionKing.wav")
foodBG_Sound= pygame.mixer.Sound("sounds/PapaPizzaria.wav")        
animalsBG_Sound= pygame.mixer.Sound("sounds/Nyan_Cat.wav")
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
        natureBG_Sound.set_volume(2)
        natureBG_Sound.play(-1)
    elif bg == "food":
        foodBG_Sound.play(-1)
    elif bg == "animals":
        animalsBG_Sound.set_volume(2)
        animalsBG_Sound.play(-1)



# 2nd parameter is the font size
LETTER_FONT = pygame.font.Font("fonts/FredokaOne-Regular.otf", 40)
DISPLAY_FONT = pygame.font.Font("fonts/FredokaOne-Regular.otf", 30)
SMALL_DISPLAY_FONT = pygame.font.Font("fonts/FredokaOne-Regular.otf", 18)
RESULT_FONT = pygame.font.Font("fonts/FredokaOne-Regular.otf", 60)
KEYBOARD_FONT = pygame.font.Font("fonts/Square.ttf", 30)
TITLE_FONT = pygame.font.Font("fonts/Aloevera-OVoWO.ttf", 100)
LOGIN_FONT = pygame.font.Font("fonts/Aloevera-OVoWO.ttf", 30)
wordle_start = False

def initialWordle():
    BG_TEXT1 = DISPLAY_FONT.render("""Welcome to Seldrow! Pick a background.""", True, "black", "white")
    BG_TEXT_RECT1 = BG_TEXT1.get_rect()
    BG_TEXT_RECT1.center = (WIDTH // 2, HEIGHT // 2-100)
    SCREEN.blit(BG_TEXT1,BG_TEXT_RECT1)
    BG_TEXT2 = DISPLAY_FONT.render("""Press 1 to enter jumanji""", True, "black", "white")
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



#distance from the left for the first letter
letter_x_pos = 257
#distance from the top of the screen fro the first row
letter_y_pos = 13
#between each letter in a row
LETTER_X_SPACING = 9
#between each row
LETTER_Y_SPACING = -11
LETTER_SIZE = 50

# Global variables
words = []
guesses_count = 0

#helps with preventing yellow square when the letter has alr been guessed correctly
used_letters = ""

# guesses variable stores all guesses, which are lists of letters..
guesses = [[]] * 6

current_guess = []
current_guess_string = ""
game_result = ""

#database global variables
name = ""
coins = 0

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
        self.text_pos = (self.bg_x + 25, self.bg_y + 25)

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
kb_y_pos = 430
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

    def getColor(self):
        return self.key_color

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

    def getKey(self, letter):
        return self.keys[letter]

keyboard = Keyboard()


def check_guess(guess, answer):
    # note: must use global keyword to change global variables in function
    global current_guess, guesses_count, current_guess_string, game_result, letter_x_pos, letter_y_pos, used_letters

    all_correct = True
    
    #helps with preventing yellow square when the letter has alr been guessed correctly
    used_letters = guess[0].text.lower() + guess[1].text.lower() + guess[2].text.lower() + guess[3].text.lower() + guess[4].text.lower()
    #iterate through each letter in the guess
    for i in range(5):
        cur_letter = guess[i].text.lower()
        #number of the same letter in a word
        num_letters = 0

        for letter in used_letters:
            if letter == cur_letter:
                num_letters += 1

        if cur_letter == answer[i]:
            guess[i].bg_color = GREEN
            guess[i].text_color = "white"
            #keyboard
            keyboard.updateKey(cur_letter, GREEN)
        
        # what should we do if there's two same letters in a word
        elif cur_letter in answer:
            used_num = 0
            for letter in used_letters:
                if letter == cur_letter:
                    used_num += 1
            if used_num <= num_letters:
                guess[i].bg_color = YELLOW
                guess[i].text_color = "white"
                all_correct = False
                #keyboard
                if keyboard.getKey(cur_letter).getColor() != GREEN:
                    keyboard.updateKey(cur_letter, YELLOW)
            else:
                guess[i].bg_color = GREY
                guess[i].text_color = "white"
                all_correct = False
                #keyboard
                if keyboard.getKey(cur_letter).getColor() != GREEN:
                    keyboard.updateKey(cur_letter, GREY)
                
        else: #letter not in answer
            guess[i].bg_color = GREY
            guess[i].text_color = "white"
            all_correct = False
            #keyboard
            if keyboard.getKey(cur_letter).getColor() != GREEN:
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
    letter_x_pos = 257
    letter_y_pos += (LETTER_Y_SPACING)
    current_guess = []
    current_guess_string = ""
        

def add_new_letter():
    #adds new letter to the guess
    global letter_x_pos, current_guess_string, current_guess, guesses, letter_y_pos
    new_letter = WordleLetter(key_pressed, (letter_x_pos, guesses_count * 80 + letter_y_pos))
    letter_x_pos += (LETTER_X_SPACING + LETTER_SIZE)
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
    letter_x_pos -= (LETTER_X_SPACING + LETTER_SIZE)
    #just added
    current_guess[len(current_guess) - 1].bg_color = "white"
    current_guess[len(current_guess) - 1].text_color = "white"
    current_guess[len(current_guess) - 1].draw()
    
    pygame.display.update()
    current_guess.pop()

def reset():
    #resets variables after each game
    global guesses_count, current_answer, guesses, current_guess, current_guess_string, game_result, wordle_start, letter_y_pos, kb_x_pos, kb_y_pos, play_BG_Sounds, used_letters
    
    SCREEN.fill("white")
    initialWordle()
    if wordle_start == True:
        wordle_start = False
    pygame.display.update()
    
    letter_y_pos = 13
    guesses_count = 0
    current_answer = ""
    guesses = [[]] * 6
    current_guess = []
    current_guess_string = ""
    game_result = ""
    play_BG_Sounds = True
    used_letters = ""

    #keyboard variables
    kb_x_pos = 110
    kb_y_pos = 430
    
def end_display():
    foodBG_Sound.stop()
    natureBG_Sound.stop()
    animalsBG_Sound.stop()
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

def login():
    global state, name, coins
    username = ""
    new_name = ""
    color_active = pygame.Color('lightskyblue3')
    color_passive = pygame.Color("gray15")
    color1 = color_passive
    color2 = color_passive
    active1 = False
    active2 = False
    
    while state=="login":
        NAME_RECT = pygame.Rect((WIDTH/2)-100,300,200,40)
        NEW_NAME_RECT = pygame.Rect((WIDTH/2)-100,500,200,40)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if  event.type == pygame.MOUSEBUTTONDOWN:
                if NAME_RECT.collidepoint(event.pos):
                    active1 = True
                    active2 = False
                    new_name=""
                elif NEW_NAME_RECT.collidepoint(event.pos):
                    active2 = True
                    active1 = False
                    username=""
                else:
                    active1 = False
                    active2 = False
                    
            if(event.type == pygame.KEYDOWN):
                if event.key == pygame.K_RETURN:
                    #check to see if username exists for both active 1 and active two
                    if active1 and username!="":
                        state ="wordle"
                        name = username
                        coins = db.reference("/Players/" + name + "/Coins").get()
                        wordle()
                    elif active2 and new_name!="":
                        state ="wordle"  
                        name = new_name
                        db.reference("/Players/").update({new_name: {"Coins":0}})
                        coins = db.reference("/Players/" + name + "/Coins").get()
                        wordle()
                if active1:
                    if event.key == pygame.K_BACKSPACE:
                        username = username[:-1]
                    else:
                        username += event.unicode
                elif active2:
                    if(event.type == pygame.KEYDOWN):
                        if event.key == pygame.K_BACKSPACE:
                            new_name = new_name[:-1]
                        else:
                            new_name += event.unicode
            
        SCREEN.fill("white")
        if active1:
            color1 = color_active
        elif active2:
            color2 = color_active
        else:
            color1 = color_passive
            color2 = color_passive
        pygame.draw.rect(SCREEN, color1, NAME_RECT, 2)
        NAME_TEXT = DISPLAY_FONT.render(username, True,"black")
        SCREEN.blit(NAME_TEXT,NAME_RECT)
        NAME_RECT.w = max(100,NAME_TEXT.get_width()+10)
        
        pygame.draw.rect(SCREEN, color2, NEW_NAME_RECT, 2)
        NEW_NAME_TEXT = DISPLAY_FONT.render(new_name, True,"black")
        SCREEN.blit(NEW_NAME_TEXT,NEW_NAME_RECT)
        NEW_NAME_RECT.w = max(100,NEW_NAME_TEXT.get_width()+10)
        
        TITLE_TEXT = TITLE_FONT.render("""seldrow""", True, "pink", "white")
        TITLE_TEXT_RECT = TITLE_TEXT.get_rect()
        TITLE_TEXT_RECT.center = (WIDTH // 2, HEIGHT - 550)
        SCREEN.blit(TITLE_TEXT, TITLE_TEXT_RECT)

        #idk if we should uselogin font here or display font
        LOGIN_TEXT = LOGIN_FONT.render("""Login""", True, "black", "white")
        LOGIN_TEXT_RECT = LOGIN_TEXT.get_rect()
        LOGIN_TEXT_RECT.center = (WIDTH // 2, HEIGHT // 2 - 100)
        SCREEN.blit(LOGIN_TEXT,LOGIN_TEXT_RECT)
        
        LOGIN_TEXT_2 = SMALL_DISPLAY_FONT.render("""enter your username""", True, "black", "white")
        LOGIN_TEXT_2_RECT = LOGIN_TEXT_2.get_rect()
        LOGIN_TEXT_2_RECT.center = (WIDTH // 2, HEIGHT // 2 - 65)
        SCREEN.blit(LOGIN_TEXT_2,LOGIN_TEXT_2_RECT)
        
        SIGNUP_TEXT = LOGIN_FONT.render("""Sign Up""", True, "black", "white")
        SIGNUP_TEXT_RECT = SIGNUP_TEXT.get_rect()
        SIGNUP_TEXT_RECT.center = (WIDTH // 2, HEIGHT // 2 + 100)
        SCREEN.blit(SIGNUP_TEXT,SIGNUP_TEXT_RECT)

        SIGNUP_TEXT_2 = SMALL_DISPLAY_FONT.render("""create new username""", True, "black", "white")
        SIGNUP_TEXT_2_RECT = SIGNUP_TEXT_2.get_rect()
        SIGNUP_TEXT_2_RECT.center = (WIDTH // 2, HEIGHT // 2 + 125)
        SCREEN.blit(SIGNUP_TEXT_2,SIGNUP_TEXT_2_RECT)

        SIGNUP_TEXT_3 = SMALL_DISPLAY_FONT.render("""(case sensitive)""", True, "black", "white")
        SIGNUP_TEXT_3_RECT = SIGNUP_TEXT_3.get_rect()
        SIGNUP_TEXT_3_RECT.center = (WIDTH // 2, HEIGHT // 2 + 150)
        SCREEN.blit(SIGNUP_TEXT_3,SIGNUP_TEXT_3_RECT)

        SCREEN.blit(EESHA_PIC, EESHA_RECT)
        SCREEN.blit(SOPHIA_PIC, SOPHIA_RECT)
        
        pygame.display.update()
 
def wordle():
    global wordle_start, play_BG_Sounds, key_pressed, current_answer, coins
    SCREEN.fill("White")
    while state =="wordle":
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if wordle_start == False:
                initialWordle()
                cur_bg = ""
                elevator.set_volume(0.4)
                elevator.play()
                SCREEN.blit(COIN_TRACKER, COIN_TRACKER_RECT)
                
                print(coins)
                COINS_TEXT = LOGIN_FONT.render(str(coins), True, "black", "pink")
                COINS_TEXT_RECT = COINS_TEXT.get_rect()
                COINS_TEXT_RECT.center = (WIDTH-75, HEIGHT-45)
                SCREEN.blit(COINS_TEXT,COINS_TEXT_RECT)
                
                if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                    cur_bg = "nature"
                    SCREEN.fill("white")
                    SCREEN.blit(NATURE_BG, NATURE_RECT)
                    SCREEN.blit(COIN_TRACKER, COIN_TRACKER_RECT)
                    keyboard.drawKeyboard()
                    with open("wordLists/nature.txt", "r") as natureWordsFile:
                        natureWords = natureWordsFile.read().splitlines()
                    current_answer = random.choice(natureWords)
                    wordle_start = True
                    
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_2:
                    cur_bg = "food"
                    SCREEN.fill("white")
                    SCREEN.blit(FOOD_BG, FOOD_RECT)
                    SCREEN.blit(COIN_TRACKER, COIN_TRACKER_RECT)
                    keyboard.drawKeyboard()
                    with open("wordLists/food.txt", "r") as foodWordsFile:
                        foodWords = foodWordsFile.read().splitlines()
                    current_answer = random.choice(foodWords)
                    wordle_start = True
                    
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_3:
                    cur_bg = "animals"
                    SCREEN.fill("white")
                    SCREEN.blit(CATS_BG, CATS_RECT)
                    SCREEN.blit(COIN_TRACKER, COIN_TRACKER_RECT)
                    keyboard.drawKeyboard()
                    with open("wordLists/animals.txt", "r") as animalWordsFile:
                        animalWords = animalWordsFile.read().splitlines()
                    current_answer = random.choice(animalWords)
                    wordle_start = True
                    
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_0:
                    SCREEN.fill("white")
                    SCREEN.blit(BACKGROUND, BACKGROUND_RECT)
                    SCREEN.blit(COIN_TRACKER, COIN_TRACKER_RECT)
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
                    #print(event.key)
                    if event.key == pygame.K_RETURN:
                        print(current_answer)
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

state="login"
async def main():
    while True:
        login()
        await asyncio.sleep(0)

asyncio.run(main())
        

