import pygame
from Button import Button
import runner
pygame.init()

pygame.display.set_caption("Main Menu")
SCREEN = pygame.display.set_mode((700,650)) #check dimensions
SCREEN.fill("white")
LETTER_FONT = pygame.font.Font("FredokaOne-Regular.otf")

def wordle():
    while True:
        SCREEN.fill("white")
        pygame.display.update()   
        runner.wordle_main()

def store():
    while True:
        STORE_POS_MOUSE = pygame.mouse.get_pos()
        SCREEN.fill("white")

        STORE_MAIN_MENU = Button(pos = (10,10), text_input = "Main Menu")
        STORE_MAIN_MENU.changeColor(STORE_POS_MOUSE)
        STORE_MAIN_MENU.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
               # if STORE_MAIN_MENU.checkForInput(STORE_POS_MOUSE):
                    #main_menu_main()
                pygame.display.update()     

def main_menu_main():
    while True:
        SCREEN.blit(SCREEN, (700,650))

        MENU_POS_MOUSE = pygame.mouse.get_pos()   
        MENU_TEXT = LETTER_FONT.render("MAIN MENU", True, "black")
        MENU_RECT = MENU_TEXT.get_rect(center=(100,100)) #check

        WORDLE_BUTTON = Button(pos = (300,300), text_input = "Main Menu")
        STORE_BUTTON = Button(pos = (300,300), text_input = "Main Menu")

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if WORDLE_BUTTON.checkForInput(MENU_POS_MOUSE):
                    wordle()
                if STORE_BUTTON.checkForInput(MENU_POS_MOUSE):
                    store()

        pygame.display.update()

       