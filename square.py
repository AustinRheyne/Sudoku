import pygame
pygame.font.init()
myFont = pygame.font.SysFont("Comic Sans MS", 80)

class Square:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.image = pygame.image.load("images/Square.png")
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.focused = False
        self.value = ""
        
        self.text = myFont.render(self.value, False, (0,0,0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = self.rect.center

    def doFocus(self, mx, my):
        if self.rect.left < mx < self.rect.right and self.rect.top < my < self.rect.bottom:
            self.focused = True
            self.image = pygame.image.load("images/SelectedSquare.png")
        else:
            self.focused = False
            self.image = pygame.image.load("images/Square.png")

    def updateText(self, new_letter):
        if self.focused and new_letter in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            self.value = new_letter
            self.text = myFont.render(self.value, False, (0,0,0))
            self.text_rect = self.text.get_rect()
            self.text_rect.center = self.rect.center


    def blit_me(self):
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.text, self.text_rect)