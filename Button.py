import pygame, sys
pygame.init()

LETTER_FONT = pygame.font.Font("FredokaOne-Regular.otf")

class Button():

    def _init_(self, image, pos_x, pos_y, text_input):
        self.image = image
        self.x = pos_x
        self.y = pos_y
        self.text_input = text_input
        self.text = LETTER_FONT.render(self.text_input, True, "White")
        self.text_rect = self.text.get_rect(center = (self.x,self.y))
        self.base_color="black"
        self.hovering_color="green"
        self.rect = self.image.get_rect(center=(self.x,self.y))
        
    def update(self, screen):
        screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, pos):
        if pos[0] in range(self.rect.left, self.rect.right) and pos[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False
    
    def changeColor(self, pos):
	   # if pos[0] in range(self.rect.left, self.rect.right) and pos[1] in range(self.rect.top, self.rect.bottom):
            self.text = LETTER_FONT.render(self.text_input, True, "green")
            #self.text = LETTER_FONT.render(self.text_input, True, "white")
    
    

