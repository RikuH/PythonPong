import pygame
from random import randint

BLACK = (0, 0, 0)

_width = 0
_height = 0

class Special(pygame.sprite.Sprite):
    def __init__(self, color, width, height, windowWidth, WindowHeight):
        super().__init__()

        _width = width
        _height = height
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.rect = self.image.get_rect()

        self.rect.x = randint(100, windowWidth - 100)
        self.rect.y = randint(100, WindowHeight - 100)
    


