import pygame
pygame.init()

LETTER_FONT = pygame.font.Font("FredokaOne-Regular.otf")

class Button():

    def _init_(self, pos_x, pos_y, text_input):
        self.x = pos_x
        self.y = pos_y
        self.text_input = text_input
        self.base_color="black"
        self.hovering_color="green"
        self.draw()
        self.rect = self.text_input.get_rect(center=(self.x, self.y))
    
    def update(self, screen):
        text = LETTER_FONT.render(self.text_input, True, "White")
        screen.blit(text, self.rect)

    def checkForInput(self, pos_x, pos_y):
        if pos_x in range(self.rect.left, self.rect.right) and pos_y in range(self.rect.top, self.rect.bottom):
            return True
        return False
    
    def changeColor(self, pos_x, pos_y):
	    if pos_x in range(self.rect.left, self.rect.right) and pos_y in range(self.rect.top, self.rect.bottom):
		    self.text_input = self.LETTER_FONT.render(self.text_input, True, self.hovering_color)       
            #self.text_input = self.LETTER_FONT.render(self.text_input, True, self.base_color)

