import pygame
import sys
from pygame import sprite

pygame.init()


WIDTH = 1100
HEIGHT = 650

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")

background = pygame.image.load("background.png").convert()

background = pygame.transform.scale(
    background,
    (WIDTH, HEIGHT)
)


class Widget(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, text):
        super().__init__()

        self.image = pygame.Surface((width, height))
        self.image.fill((0, 0, 0))

        font = pygame.font.Font(None, 32)
        text_image = font.render(text, True, (255, 255, 255))

        text_rect = text_image.get_rect(
            center=self.image.get_rect().center
        )

        self.image.blit(text_image, text_rect)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


widgets = pygame.sprite.Group()

widgets.add(Widget(10, 100, 150, 60, "Ticket 1"))
widgets.add(Widget(10, 170, 150, 60, "Ticket 2"))
widgets.add(Widget(10, 240, 150, 60, "Ticket 3"))
widgets.add(Widget(10, 310, 150, 60, "Ticket 4"))
widgets.add(Widget(10, 380, 150, 60, "Ticket 5"))
running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            for widget in widgets:
                if widget.rect.collidepoint(event.pos):
                    print("Нажат виджет")


    screen.blit(background, (0, 0))

    widgets.draw(screen)

    pygame.display.flip()


pygame.quit()
sys.exit()