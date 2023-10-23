class Main:
    words = []
    file = open("words.txt", "r")
    words = file.read.splitlines()


import pygame #user interface
import sys #variables and functions
import random #for random answerWord in words
from words import* 

pygame.init();

#constants

#hex colors
GREEN = "#6aaa64"
YELLOW = "#c9b458"
GREY = "#787c7e"
OUTLINE = "#d3d6da"
FILLED_OUTLINE = "#878a8c"

WidthWIDTH, HEIGHT = 633, 900


#Variables for set up of dislay window (how it looks)
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
BACKGROUND = pygame.image.load("assets/Starting Tiles.png")  #adds background image
BACKGROUND_RECT = BACKGROUND.get_rect(center=(317, 300)) 
ICON = pygame.image.load("assets/Icon.png")

pygame.display.set_caption("Seldrow!")
pygame.display.set_icon(ICON)


ALPHABET = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]

#GUESSED_LETTER_FONT = pygame.font.Font("assets/FreeSansBold.otf", 50)
#AVAILABLE_LETTER_FONT = pygame.font.Font("assets/FreeSansBold.otf", 25)

SCREEN.fill("white")
SCREEN.blit(BACKGROUND, BACKGROUND_RECT) #place image onto the screen
pygame.display.update() #whole window is updated

LETTER_X_SPACING = 85
LETTER_Y_SPACING = 12
LETTER_SIZE = 75
LETTER_FONT = pygame.font.Font("FredokaOne-Regualr.otf")

# Global variables

guesses_count = 0

# guesses is a 2D list storing all the guesses, which are lists of letters.
# The list will be iterated through so each letter in each guess will be drawn on the screen.
guesses = [[]] * 6

current_guess = []
current_guess_string = ""
current_letter_bg_x = 110

game_result = ""




class Wordle:
    def__init__(self, text, bg_position):
        self.bg_color = "white"
        self.text_color="black"
        self.bg_position = bg_position
        self.bg_x = bg_position[0]
        self.bg_y = bg_position[1]
        self.text = text
        self.bg_rect = (self.bg_x, self.bg_y, LETTER_SIZE, LETTER_SIZE) #left, top, width, height 
        self.text_position = (self.bg_x+36, self.bg_y+34)
        self.text_surface = LETTER_FONT.render(self.text, True, self.text_color)
        self.text_rect = self.text_surface.get_rect(center=self.text_position)

    def draw(self):
        # Puts the letter and text on the screen at the desired positions.
        pygame.draw.rect(SCREEN, self.bg_color, self.bg_rect)
        if self.bg_color == "white":
            pygame.draw.rect(SCREEN, FILLED_OUTLINE, self.bg_rect, 3)
        self.text_surface = LETTER_FONT.render(self.text, True, self.text_color)
        SCREEN.blit(self.text_surface, self.text_rect)
        pygame.display.update()

     def delete(self):
        # Fills the letter's spot with the default square, emptying it.
        pygame.draw.rect(SCREEN, "white", self.bg_rect)
        pygame.draw.rect(SCREEN, OUTLINE, self.bg_rect, 3) #last parameter is the width of the border
        pygame.display.update()

 
