from numpy import square
import pygame
from square import Square
pygame.init()

pygame.display.set_caption("Sudoku")
screen = pygame.display.set_mode((810,810))
 
grid = []
for x in range(0, 9):
    for y in range(0,9):
        grid.append(Square(screen, (x*90), (y*90)))

def eventLoop():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            for sqr in grid:
                mx, my = pygame.mouse.get_pos()
                sqr.doFocus(mx, my)
        
        if event.type == pygame.KEYDOWN:
            for sqr in grid:
                sqr.updateText(pygame.key.name(event.key))


while True:
    eventLoop()
    screen.fill((0,0,0))

    for sqr in grid:
        sqr.blit_me()

    pygame.display.flip()
