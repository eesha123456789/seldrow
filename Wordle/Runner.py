class Main:
    words = []
    file = open("words.txt", "r")
    words = file.read.splitlines()


import pygame
import sys
import random
from words import*

pygame.init();

#constants

GREEN = "#6aaa64"
YELLOW = "#c9b458"
GREY = "#787c7e"
OUTLINE = "#d3d6da"
FILLED_OUTLINE = "#878a8c"

WidthWIDTH, HEIGHT = 633, 900

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
BACKGROUND = pygame.image.load("assets/Starting Tiles.png")
BACKGROUND_RECT = BACKGROUND.get_rect(center=(317, 300))
ICON = pygame.image.load("assets/Icon.png")

pygame.display.set_caption("Seldrow!")
pygame.display.set_icon(ICON)


ALPHABET = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]

#GUESSED_LETTER_FONT = pygame.font.Font("assets/FreeSansBold.otf", 50)
#AVAILABLE_LETTER_FONT = pygame.font.Font("assets/FreeSansBold.otf", 25)

SCREEN.fill("white")
SCREEN.blit(BACKGROUND, BACKGROUND_RECT)
pygame.display.update()

LETTER_X_SPACING = 85
LETTER_Y_SPACING = 12
LETTER_SIZE = 75

# Global variables

guesses_count = 0

# guesses is a 2D list storing all the guesses, which are lists of letters.
# The list will be iterated through so each letter in each guess will be drawn on the screen.
guesses = [[]] * 6

current_guess = []
current_guess_string = ""
current_letter_bg_x = 110

game_result = ""

lass Wordle:
    def __init__(self, x, y, letter):
        self.x = x
        self.y = y
        self.text = letter
        self.rect = (x, y, 57, 75)
        self.bg_color = OUTLINE

    def draw(self):
        pygame.draw.rect(SCREEN, self.bg_color, self.rect)
        self.text_surface = AVAILABLE_LETTER_FONT.render(self.text, True, "blue")
        self.text_rect = self.text_surface.get_rect(center=(self.x+27, self.y+30))
        SCREEN.blit(self.text_surface, self.text_rect)
        pygame.display.update()