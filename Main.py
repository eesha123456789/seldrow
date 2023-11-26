import pygame, sys
from button import Button
pygame.init()

pygame.display.set_caption("Main Menu")
SCREEN = pygame.display.set_mode(1000,1000) #check dimensions
LETTER_FONT = pygame.font.Font("FredokaOne-Regular.otf")

def wordle():
    while True:
        WORDLE_POS_MOUSE = pygame.mouse.get_pos()
        SCREEN.fill("white")

        WORDLE_MAIN_MENU = Button(pos_x = 10, pos_y = 10, text_input = "Main Menu", font = LETTER_FONT, base_color = "Black")
        WORDLE_MAIN_MENU.changeColor(WORDLE_POS_MOUSE)
        WORDLE_MAIN_MENU.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if WORDLE_MAIN_MENU.checkForInput(WORDLE_POS_MOUSE):
                    main_menu()

        pygame.display.update()

def store():
    while True:
        STORE_POS_MOUSE = pygame.mouse.getpos()
        SCREEN.fill("white")

        STORE_MAIN_MENU = Button(pos_x = 10, pos_y = 10, text_input = "Main Menu", font = LETTER_FONT, base_color = "Black")
        STORE_MAIN_MENU.changeColor(STORE_POS_MOUSE)
        STORE_MAIN_MENU.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if STORE_MAIN_MENU.checkForInput(STORE_POS_MOUSE):
                    main_menu()

        pygame.display.update()     

def main_menu():
    while True:
        SCREEN.blit (BG, (0,0))

        MENU_POS_MOUSE = pygame.mouse.get_pos()   
        MENU_TEXT = LETTER_FONT.render("MAIN MENU", True, "black")
        MENU_RECT = MENU_TEXT.get_erct(center=(100,100)) #check

        WORDLE_BUTTON = Button(pos_x = 10, pos_y = 10, text_input = "Main Menu", font = LETTER_FONT, base_color = "Black")
        STORE_BUTTON = Button(pos_x = 10, pos_y = 10, text_input = "Main Menu", font = LETTER_FONT, base_color = "Black")

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if WORDLE_BUTTON.checkForInput(MENU_POS_MOUSE):
                    play()
                if STORE_BUTTON.checkForInput(MENU_POS_MOUSE):
                    store()

        pygame.display.update()

main_menu()
       