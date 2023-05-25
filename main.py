import pygame as pygame

from Label import Label

window = pygame.display.set_mode((500, 500))
color = (200, 255, 255)
window.fill(color)
clock = pygame.time.Clock()
YELLOW = (255, 255, 0)
DARK_BLUE = (0, 0, 100)
BLUE = (80, 80, 255)
cards = []
num_cards = 4
x = 70
for i in range(num_cards):
    new_card = Label(x, 170, 70, 100, YELLOW)
    new_card.outline(BLUE, 10)
    new_card.set_text('CLICK', 26)
    cards.append(new_card)
    x = x + 100
while True:
    pygame.display.update()
