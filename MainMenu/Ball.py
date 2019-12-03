import pygame
from random import randint

BLACK = (0, 0, 0)

class ball(pygame.sprite.Sprite):
    def __init__(self, color, width, height, windowWidth, WindowHeight):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.velocity = [randint(6, 12), randint(-8, 8)]
        #self.velocity = [randint(16, 20), randint(-80, 80)]

        self.rect = self.image.get_rect()

        self.rect.x = windowWidth / 2
        self.rect.y = WindowHeight / 2

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-2, 2)

