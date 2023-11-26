import pygame
pygame.init()

LETTER_FONT = pygame.font.Font("FredokaOne-Regular.otf")

class Button():

    def _init_(self, pos, text_input):
        self.x = pos[0]
        self.y = pos[1]
        self.text_input = text_input
        self.base_color="black"
        self.hovering_color="green"
        self.draw()
        self.rect = self.text_input.get_rect(10,10)
    #center=(self.x_pos, self.y_pos)
    def update(self, screen):
        text = LETTER_FONT.render(self.text_input, True, "Black")
        screen.blit(text, self.rect)

    def checkForInput(self, pos):
        if pos[0] in range(self.rect.left, self.rect.right) and pos[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False
    
    def changeColor(self, pos):
	    if pos[0] in range(self.rect.left, self.rect.right) and pos[1] in range(self.rect.top, self.rect.bottom):
		    self.text_input = self.LETTER_FONT.render(self.text_input, True, self.hovering_color)       
            #self.text_input = self.LETTER_FONT.render(self.text_input, True, self.base_color)

