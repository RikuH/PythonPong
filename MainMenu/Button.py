import pygame
import sys
BLACK  = (0,0,0)

class button(pygame.sprite.Sprite):
    def __init__(self, color, width, height, x, y):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.rect = self.image.get_rect()

        self.rect.x = x - width / 2
        self.rect.y = y - height / 2


    def drawText(self, button, label, win):
        font = pygame.font.SysFont("comicsansms", 40)
        text = font.render(label, True, (0, 0, 0))    
        win.blit(text, (button.rect.x, button.rect.y))
