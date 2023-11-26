class Button():
    def _init_(pos_x, pos_y, text_input):
        self.x = x_pos
        self.y = y_pos
        self.text_input = text_input
        self.base_color="black"
        self.hovering_color="green"
        self.draw()
        self.rect = self.text_input.get_rect(center=(self.x, self.y))
    
    def draw(self):
        text = font.render(self.text_input, True, "White")
        screen.blit(text, rect)

    def checkForInput(self, position):
		if self.x in range(self.rect.left, self.rect.right) and self.y in range(self.rect.top, self.rect.bottom):
			return True
		return False
    
	def changeColor(self, position):
		if self.x in range(self.rect.left, self.rect.right) and self.y in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)
